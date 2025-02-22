from src.model.config.connection import DBConnectionHandler
from src.model.entities.eventos import Eventos

class EventosRepository:
	def insert(self, event_name: str) -> None:
		with DBConnectionHandler() as db:
			try:
				new_evento = Eventos(nome=event_name)
				db.session.add(new_evento)
				db.session.commit()
			except Exception as e:
				db.session.rollback()
				raise e

	def select_event(self, event_name: str) -> Eventos:
		with DBConnectionHandler() as db:
			data = db.session.query(Eventos).filter(Eventos.nome == event_name).one_or_none()
			return data