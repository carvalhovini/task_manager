from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken

class TaskAPITests(APITestCase):

    def setUp(self):
        # Cria um usuário para os testes
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        # Gera um token JWT para o usuário
        refresh = RefreshToken.for_user(self.user)
        self.access_token = str(refresh.access_token)

        # Configura a autenticação para o cliente de testes
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

        # URL para o endpoint de listagem e criação de tarefas
        self.task_list_create_url = reverse('task-list-create')

    def test_create_task(self):
        """Testa a criação de uma nova tarefa"""
        data = {
            "title": "Test Task",
            "description": "This is a test task",
            "due_date": "2024-12-31"
        }
        response = self.client.post(self.task_list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_list_tasks(self):
        """Testa a listagem de todas as tarefas"""
        Task.objects.create(title="Task 1", description="Description 1", due_date="2024-12-31")
        Task.objects.create(title="Task 2", description="Description 2", due_date="2024-12-31")
        response = self.client.get(self.task_list_create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_task_by_id(self):
        """Testa a recuperação de uma tarefa específica pelo ID"""
        task = Task.objects.create(title="Task 1", description="Description 1", due_date="2024-12-31")
        url = reverse('task-detail', kwargs={'id': task.id})
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], task.title)

    def test_update_task(self):
        """Testa a atualização de uma tarefa existente"""
        task = Task.objects.create(title="Task 1", description="Description 1", due_date="2024-12-31")
        url = reverse('task-detail', kwargs={'id': task.id})
        data = {
            "title": "Updated Task",
            "description": "Updated description",
            "due_date": "2025-01-01"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, "Updated Task")
        self.assertEqual(task.description, "Updated description")

    def test_delete_task(self):
        """Testa a exclusão de uma tarefa"""
        task = Task.objects.create(title="Task 1", description="Description 1", due_date="2024-12-31")
        url = reverse('task-detail', kwargs={'id': task.id})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_unauthenticated_access(self):
        """Testa acesso sem autenticação"""
        # Remove as credenciais para simular acesso não autenticado
        self.client.credentials()
        response = self.client.get(self.task_list_create_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_task_with_missing_fields(self):
        """Testa a criação de uma tarefa com campos obrigatórios ausentes"""
        data = {
            "description": "This task is missing a title",
            "due_date": "2024-12-31"
        }
        response = self.client.post(self.task_list_create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)

    def test_task_validation(self):
        """Testa validações de campos obrigatórios"""
        response = self.client.post(self.task_list_create_url, {}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)
        self.assertIn('description', response.data)
        self.assertIn('due_date', response.data)
