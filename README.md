# Fast_api_Beck

Configuração Inicial
Para começar, você precisa ter o Python 3.6 ou superior instalado na sua máquina. Com o Python pronto, instale o FastAPI e o Uvicorn, que é um servidor ASGI que vai servir nossa aplicação FastAPI. Você também precisará de um token de acesso à API do OpenAI para consultar o ChatGPT 3.5 Turbo.

apí_key= https://platform.openai.com/api-keys


Trabalhei 4 horas por dia nessas tasks para simular meu real desempenho em uma situação cotidiana, não sabia muito sobre fastAPi então foi além de um desenvolvimento um aprendizado, lendo documentação e resolvendo os bugs.



projeto/
│
├── alembic/                 # Diretório de configurações do Alembic 
│   ├── versions/            # Scripts de migração
│   └── alembic.ini          # Configuração do Alembic
│
├── app/                     # Código-fonte da aplicação
│   ├── __init__.py
│   ├── main.py              # Arquivo principal do FastAPI
│   ├── models.py            # Modelos SQLAlchemy para o banco de dados
│   └── schemas.py           # Modelos Pydantic para a validação de dados
│
└── .env                     # Arquivo para variáveis de ambiente 
