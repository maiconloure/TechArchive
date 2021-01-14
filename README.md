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
