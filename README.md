# Tech Archive API

## **Bem Vindo!**

Para iniciar sua API localmente execute os seguintes comandos, nesta ordem:

> iniciar Banco de Dados

```sh
psql -u user_name
CREATE DATABASE techarchive;
```

> Configurar o ambiente

```sh
Create .env file
copy content of .env.example to .env
rename you user_name and password in .env
```

> Configurar e instalar dependencias

```sh
python -m venv venv
pip install -r requirements.txt
flask db upgrade
flask run
```

# Rotas

## Base URL

```
localhost:5000
```

## Base Header

```
Content-Type: application/json
```

# Endpoints

# Usuários

## POST /login -> Autentica o usuário

body

```json
{
  "user": "teste",
  "password": "1234"
}
```

## POST /user -> Cria um usuário

body

```json
{
  "name": "Nome Completo",
  "description": "breve descrição",
  "email": "email.example@gmail.com",
  "password": "123456"
}
```

## GET /users -> Retorna uma um lista com todos os usuarios cadastrados

headers

```
Authorization: <TOKEN>
```

## GET /user/:id -> Retorna o usuario pelo seu id

headers

```
Authorization: <TOKEN>
```

## DELETE /user/:id -> Deleta o usuario pelo seu id

headers

```
Authorization: <TOKEN>
```

## PATCH /user/:id -> Atualiza o usuario com o user_id(\*todos os parametros são opcionais)

headers

```
Authorization: <TOKEN>
```

body

```json
{
  "name": "Nome Completo",
	"description": "breve descrição",
	"email": "email.example@gmail.com",
	"password": "123456"
  }
}
```

# Noticias

## GET /news -> Retorna todas as noticías

## GET /news/:user_id/ -> Retorna todas as noticias de um usuário

headers

```
Authorization: <TOKEN>
```

## GET /news/:user_id/:news_id/ -> Retorna a noticia de um usuário por id

headers

```
Authorization: <TOKEN>
```

## PATCH /news/:user_id/:news_id -> Modifica a noticia de um usuário por id

Just send what you want to change.

headers

```
Authorization: <TOKEN>
```

body

```json
{
  "news": {
    "title": "Livro",
    "author": "Author",
    "content": "Long text",
    "upvotes": 1,
    "downvotes": 1,
    "idle_time": 1,
    "theme": "Computers,Programming",
    "approved": bool
  }
}
```

## DELETE /news/:user_id/:news_id -> Deleta a noticia de um usuário por id

headers

```
Authorization: <TOKEN>
```

## POST /news/:user_id/ -> Cria uma notícia

headers

```
Authorization: <TOKEN>
```

body

```json
{
  "news": {
    "title": "Livro",
    "author": "Author",
    "content": "Long text",
    "upvotes": 1,
    "downvotes": 1,
    "idle_time": 1,
    "theme": "Computers,Programming",
    "approved": bool
  }
}
```
