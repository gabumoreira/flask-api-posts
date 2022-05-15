# flask-crud

Essa é uma api utilizando o microframework Flask, existe uma conexão com banco de dados SQLite3. A porta padrão é a 5000.

Ela possui o dominio da posts, as rotas disponiveis são:

|Rota   | Verbo | Descrição
|--     | --    | --
|/posts | GET   | Lista todos os posts criados
|/posts | POST  | Insere um novo post

Modelo:
```json
{
    "title": "Titulo do post",
    "content": "Texto do post",
    "created": "2022-05-15 19:38:52",
    "id": 37,
}
```

## setup

Para executar a API é necessario instalar as dependencias do arquivo requirements.txt: 

```
pip install requirements.txt
```

## run

Para subir a API é necessarios subir o banco de dados:

```
python data/init_db.py
```

Sera criado o arquivo data/database.py, depois para subir a API é só rodar o seguinte comando:

```
python api.py
```

## postman

Tem uma collection com exemplos na pasta /postman.

