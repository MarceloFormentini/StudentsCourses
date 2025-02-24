import random
from src.model.config.connection import DBConnectionHandler
from src.model.entities.eventos_link import EventosLink
from src.model.repositories.interface.eventos_link_repository import EventosLinkRepositoryInterface

class EventosLinkRepository(EventosLinkRepositoryInterface):
	def insert(self, evento_id: int, subcriber_id: int) -> None:
		with DBConnectionHandler() as db:
			try:
				link_final = ''.join(random.choices('0123456789ABCDEF', k=7))
				formated_link = f'evento-{evento_id}-{subcriber_id}-{link_final}'
				new_evento_link = EventosLink(
					evento_id=evento_id,
					inscrito_id=subcriber_id,
					link=formated_link
				)
				db.session.add(new_evento_link)
				db.session.commit()
			except Exception as e:
				db.session.rollback()
				raise e

	def select_event_link(self, event_id: int, subcriber_id: int) -> EventosLink:
		with DBConnectionHandler() as db:
			data = (
				db.session
				.query(EventosLink)
				.filter(
					EventosLink.evento_id == event_id,
					EventosLink.inscrito_id == subcriber_id
				)
				.one_or_none()
			)
			return data