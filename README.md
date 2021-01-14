# Tech Archive API

## **Bem Vindo!**

Para iniciar sua API localmente execute os seguintes comandos, nesta ordem:

>iniciar Banco de Dados
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

## POST /login

body

```json
{
  "user": "teste",
  "password": "1234"
}
```

## post /user/create

body

```json
{
  "user": {
    "name": "name",
    "admin": bool,
    "email": "test@test.com",
    "password": "1234"
  }
}
```

## GET /users

headers

```
Authorization: <TOKEN>
```

## GET /users/:id

headers

```
Authorization: <TOKEN>
```

## DELETE /users/:id

headers

```
Authorization: <TOKEN>
```

## PATCH /users/:id

Just send what you want to change.

headers

```
Authorization: <TOKEN>
```

body

```json
{
  "user": {
    "name": "name",
    "email": "test@test.com",
    "password": "1234"
  }
}
```

# Noticias

## GET /news

## GET /news/:user_id/:news_id/

headers

```
Authorization: <TOKEN>
```

## PATCH /news/:user_id/:news_id

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

## DELETE /news/:user_id/:news_id

headers

```
Authorization: <TOKEN>
```

## POST /news/:user_id/create/

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

## #**Rotas prontas**

> ## User

```sh
GET /users/ -> retorna uma um lista com todos os usuarios cadastrados

GET /users/user_id -> retorna o usuario pelo seu id
```

```sh
> POST /users/ -> Cria um usuário

{
	"name": "Nome Completo",
	"description": "breve descrição",
	"email": "email.example@gmail.com",
	"password": "123456"
}
```

```sh
> PATCH /users/user_id -> Atualiza o usuario com o user_id(*todos os parametros são opcionais)

{
	"name": "Nome Completo",
	"description": "breve descrição",
	"email": "email.example@gmail.com",
	"password": "123456"
}
```

```sh
> DELETE /users/user_id -> Delete o usuario com o user_id
```
