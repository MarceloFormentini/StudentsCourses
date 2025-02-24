from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface

class SubscribersCreator:
	def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
		self.__subscribers_repository = subscribers_repository

	def create(self, http_request: HttpRequest) -> HttpResponse:
		subscribers_info = http_request.body['data']
		subscriber_email = subscribers_info['email']
		subscriber_evento_id = subscribers_info['evento_id']

		self.__check_subscriber(subscriber_email, subscriber_evento_id)
		self.__insert_subscriber(subscribers_info)
		return self.__format_response(subscribers_info)

	def __check_subscriber(self, subscriber_email: str, subscriber_evento_id: int) -> None:
		response = self.__subscribers_repository.select_subscriber(subscriber_email, subscriber_evento_id)
		if response:
			raise Exception("Subscriber already exists")

	def __insert_subscriber(self, subscriber_info: dict) -> None:
		self.__subscribers_repository.insert(subscriber_info)

	def __format_response(self, subscribers_info: dict) -> HttpResponse:
		return HttpResponse(
			body={
				"message": "Subcriber created successfully",
				"data": {
					"Type": "Subcriber",
					"count": 1,
					"atributes": subscribers_info
				}
			},
			status_code=201
		)