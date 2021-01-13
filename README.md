# Tech Archive Api

## Bem Vindo!

- Verifique os requisitos para configurar o ambiente!
- Projeto em construção ideias são bem vindas!
- Configure o ambiente com .env

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
