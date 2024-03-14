# API MVT

A API MVT é uma aplicação que recebe dados do Node-RED e os armazena em um banco de dados. Ele fornece uma interface para visualizar os dados recebidos.

## Instalação

Siga estas etapas para instalar e configurar a API MVT em seu ambiente local:

1. Clone o repositório:

```
git clone https://github.com/VitorHmaia/api_nodered.git
```

2. Acesse o diretório da aplicação:

```
cd api_mvt
```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

```
python -m venv venv
```

- No Windows:

```
venv\Scripts\activate
```

- No macOS e Linux:

```
source venv/bin/activate
```

4. Instale as dependências do projeto:

```
pip install -r requirements.txt
```

5. Aplique as migrações do banco de dados:

```
python manage.py migrate
```

6. Inicie o servidor:

```
python manage.py runserver
```

7. Acesse a API em seu navegador ou usando ferramentas como Postman:

```
http://localhost:8000/api/dados/
```

## Como usar

- A API MVT recebe dados do Node-RED e os armazena em um banco de dados.
- Os dados podem ser acessados através da interface da API em `/api/dados/`.
- Você pode visualizar os últimos 10 registros na página inicial em `/`.

## Tecnologias Utilizadas

- Python
- Django
- Django REST Framework
