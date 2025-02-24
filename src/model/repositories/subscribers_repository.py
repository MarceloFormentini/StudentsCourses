from sqlalchemy import func, desc
from src.model.config.connection import DBConnectionHandler
from src.model.entities.inscritos import Inscritos
from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface

class SubscribersRepository(SubscribersRepositoryInterface):
	def insert(self, subscriber_info: dict) -> None:
		with DBConnectionHandler() as db:
			try:

				new_subscriber = Inscritos(
					nome=subscriber_info.get('nome'),
					email=subscriber_info.get('email'),
					link=subscriber_info.get('link'),
					evento_id=subscriber_info.get('evento_id')
				)

				db.session.add(new_subscriber)
				db.session.commit()

			except Exception as e:
				db.session.rollback()
				raise e

	def select_subscriber(self, email: str, evento_id: int) -> Inscritos:
		with DBConnectionHandler() as db:
			data = (
				db.session
				.query(Inscritos)
				.filter(
					Inscritos.email == email,
					Inscritos.evento_id == evento_id
				)
				.one_or_none())
			return data

	def select_subscribers_by_link(self, link: str, evento_id: int) -> list:
		with DBConnectionHandler() as db:
			data = (
				db.session
				.query(Inscritos)
				.filter(
					Inscritos.link == link, 
					Inscritos.evento_id == evento_id
				)
				.all())
			return data

	def get_ranking(self, evento_id: int) -> list:
		with DBConnectionHandler() as db:
			data = (
				db.session
				.query(
					Inscritos.link,
					func.count(Inscritos.link).label('total')
				)
				.filter(
					Inscritos.evento_id == evento_id,
					Inscritos.link.isnot(None)
				)
				.group_by(Inscritos.link)
				.order_by(desc('total'))
				.all())
			return data