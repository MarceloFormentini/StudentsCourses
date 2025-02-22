# Sistema para inscrever nossos alunos em eventos.

Banco de dados utilizados é o SQLite. Na pasta  init temos o script da criação das tabelas.

No terminal de comando, na pasta do projeto, execute o comando:
```
python3
```
Com isso entra no CLI (Comand Line Interface) do Python. Execute os comandos:
```
import sqlite3
sqllite3.connect('schema.db')
```
Com isso é gerado o banco de dados. Acessar o banco de dados através e executar o script de criação das tabelas.

## Configuração
1. Criar ambiente virtual
  - Link: https://pypi.org/project/virtualenv/
  - Documentação sobre ambiente virtual: https://docs.python.org/3.13/library/venv.html
  - Comando:
  ```
  pip3 install virtualenv
  ```
  - Ativar ambiente virtual
  ```
  python3 -m venv venv
  ```
  - Comando para acessar o ambiente virtual
  ```
  . venv/bin/activate
  ```
  - Com isso pode ser instalado bibliotecas no ambiente virtual e não na prpria máquina.
  - Lib para teste unitário: https://pypi.org/project/pytest/. Comando:
  ```
  pip3 install pytest
  ```
  - Adicionar a lib do Flask - https://pypi.org/project/Flask/
  ```
  pip install Flask
  ```
  - Adicionar a ORM SQLAlchemy - https://pypi.org/project/SQLAlchemy/, Documentação: https://www.sqlalchemy.org/
  ```
  pip3 install SQLAlchemy
  ```
  - Comando para gerar as dependencias instaladas.
  ```
  pip3 freeze > requirements.txt
  ```
  - Lib para validação - https://pypi.org/project/Cerberus
  ```
  pip install Cerberus
  ```
