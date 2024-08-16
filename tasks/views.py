from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Retorna uma lista de todas as tarefas.",
        responses={
            200: openapi.Response(
                description="Lista de Tarefas",
                examples={
                    "application/json": [
                        {
                            "id": 1,
                            "title": "Comprar pão",
                            "description": "Comprar pão na padaria",
                            "due_date": "2024-12-31",
                            "created_at": "2024-08-16T12:00:00Z",
                            "updated_at": "2024-08-16T12:00:00Z"
                        }
                    ]
                },
                schema=TaskSerializer(many=True)
            ),
            401: "Unauthorized"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Cria uma nova tarefa.",
        request_body=TaskSerializer,
        responses={
            201: openapi.Response(
                description="Tarefa Criada",
                examples={
                    "application/json": {
                        "id": 2,
                        "title": "Lavar o carro",
                        "description": "Lavar o carro no sábado",
                        "due_date": "2024-12-25",
                        "created_at": "2024-08-16T13:00:00Z",
                        "updated_at": "2024-08-16T13:00:00Z"
                    }
                },
                schema=TaskSerializer
            ),
            400: "Bad Request",
            401: "Unauthorized"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_description="Recupera uma tarefa específica pelo ID.",
        responses={
            200: openapi.Response(
                description="Tarefa Recuperada",
                examples={
                    "application/json": {
                        "id": 1,
                        "title": "Comprar pão",
                        "description": "Comprar pão na padaria",
                        "due_date": "2024-12-31",
                        "created_at": "2024-08-16T12:00:00Z",
                        "updated_at": "2024-08-16T12:00:00Z"
                    }
                },
                schema=TaskSerializer
            ),
            404: "Not Found",
            401: "Unauthorized"
        }
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Atualiza uma tarefa existente pelo ID.",
        request_body=TaskSerializer,
        responses={
            200: openapi.Response(
                description="Tarefa Atualizada",
                examples={
                    "application/json": {
                        "id": 1,
                        "title": "Comprar pão integral",
                        "description": "Comprar pão integral na padaria",
                        "due_date": "2024-12-31",
                        "created_at": "2024-08-16T12:00:00Z",
                        "updated_at": "2024-08-16T14:00:00Z"
                    }
                },
                schema=TaskSerializer
            ),
            404: "Not Found",
            401: "Unauthorized"
        }
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Deleta uma tarefa existente pelo ID.",
        responses={
            204: "No Content",
            404: "Not Found",
            401: "Unauthorized"
        }
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)


# View para renderizar um template HTML
def home(request):
    return render(request, 'home.html')


