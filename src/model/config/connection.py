from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# classe responsável por gerencial a conexão com o banco de dados
class DBConnectionHandler:
	def __init__(self):
		self.__connection_string = "sqlite:///schema.db"
		self.__engine = self.__create_database_engine()
		self.session = None

	def __create_database_engine(self):
		engine = create_engine(self.__connection_string)
		return engine

	def __enter__(self):
		session_make = sessionmaker(bind=self.__engine)
		self.session = session_make()
		return self

	# os parametros exc_type, exc_value e traceback são utilizados para tratar exceções
	# caso ocorram dentro do bloco with
	def __exit__(self, exc_type, exc_value, traceback):
		self.session.close()