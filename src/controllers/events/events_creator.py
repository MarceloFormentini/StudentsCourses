from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.eventos_repository import EventosRepositoryInterface

class EventsCreator:
	def __init__(self, event_repository: EventosRepositoryInterface):
		self.__event_repository = event_repository

	def create(self, http_request: HttpRequest) -> HttpResponse:
		events_info = http_request.body['data']
		event_name = events_info['name']
		self.__check_event(event_name)
		self.__insert_event(event_name)
		return self.__format_response(event_name)

	def __check_event(self, event_name: str) -> None:
		response = self.__event_repository.select_event(event_name)
		if response:
			raise Exception("Event already exists")
		
	def __insert_event(self, event_name: str) -> None:
		self.__event_repository.insert(event_name)

	def __format_response(self, event_name: str) -> HttpResponse:
		return HttpResponse(
			body={
				"message": "Event created successfully",
				"data": {
					"Type": "Event",
					"count": 1,
					"atributes": {
						"name": event_name
					}
				}
			},
			status_code=201
		)