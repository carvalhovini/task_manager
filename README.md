# Testando a API do Gerenciamento de Tarefas com Postman

## 1. Execute o Servidor Django

Antes de iniciar os testes, certifique-se de que o servidor Django está em execução.

### Passos:

1. Abra o terminal no VSCode.
2. Navegue até o diretório do seu projeto.
3. Execute o comando para iniciar o servidor:

    ```bash
    python manage.py runserver
    ```

4. Verifique se a aplicação está acessível no navegador através de [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## 2. Obter o Token JWT

Para acessar os endpoints protegidos, você precisará de um token JWT.

### 2.1 Obter o Token

1. No Postman, adicione uma nova requisição.
2. Nomeie a requisição como `Obter Token JWT`.
3. Configure a requisição da seguinte forma:
    - **Método:** POST
    - **URL:** `http://127.0.0.1:8000/api/token/`
    - **Body:**

    ```json
    {
        "username": "seu_username",
        "password": "sua_senha"
    }
    ```

4. Clique em "Send" e copie o valor do token de acesso (`access`).

## 3. Testar Endpoints com o Token JWT

### 3.1 Listar Tarefas

1. No Postman, crie uma nova requisição chamada `Listar Tarefas`.
2. Configure a requisição da seguinte forma:
    - **Método:** GET
    - **URL:** `http://127.0.0.1:8000/api/tasks/`
    - **Headers:**
        - **Key:** Authorization
        - **Value:** Bearer `{seu_token_jwt}`

3. Clique em "Send" para ver a lista de tarefas.

### 3.2 Criar Tarefa

1. No Postman, crie uma nova requisição chamada `Criar Tarefa`.
2. Configure a requisição da seguinte forma:
    - **Método:** POST
    - **URL:** `http://127.0.0.1:8000/api/tasks/`
    - **Headers:**
        - **Key:** Authorization
        - **Value:** Bearer `{seu_token_jwt}`
    - **Body:**

    ```json
    {
        "title": "Nova Tarefa",
        "description": "Descrição da tarefa",
        "due_date": "2024-12-31"
    }
    ```

3. Clique em "Send" para criar uma nova tarefa.

### 3.3 Outras Operações

1. Crie requisições para Atualizar, Deletar, e Obter Tarefa por ID, repetindo os passos anteriores e ajustando o método HTTP e o endpoint conforme necessário.

## 4. Verificar a Documentação com Swagger

1. Acesse [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/) no navegador para ver a documentação da API gerada automaticamente.
2. Teste as operações diretamente através da interface Swagger.

## 5. Finalização e Debugging

1. Se encontrar algum erro, utilize o console no VSCode e o Postman para identificar o problema.
2. Verifique os logs no terminal do VSCode para mensagens de erro.

Com esses passos, você será capaz de configurar o ambiente, testar os endpoints da API e depurar problemas de maneira eficaz!
