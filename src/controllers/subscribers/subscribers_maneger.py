from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.model.repositories.interface.subscribers_repository import SubscribersRepositoryInterface

class SubscriberManeger:
	def __init__(self, subscribers_repository: SubscribersRepositoryInterface):
		self.__subscribers_repository = subscribers_repository

	def get_subscriber_by_link(self, http_request: HttpRequest) -> HttpResponse:
		link = http_request.param['link']
		event_id = http_request.param['event_id']
		subscribers = self.__subscribers_repository.select_subscribers_by_link(link, event_id)
		return self.__format_subscriber_response(subscribers)

	def get_event_ranking(self, http_request: HttpRequest) -> HttpResponse:
		event_id = http_request.param['event_id']
		ranking = self.__subscribers_repository.get_ranking(event_id)
		return self.__format_ranking_response(ranking)

	def __format_subscriber_response(self, subscriber: list) -> HttpResponse:
		formated_subscriber = []
		for sub in subscriber:
			formated_subscriber.append({
				'nome': sub.nome,
				'email': sub.email,
			})

		return HttpResponse(
			status_code=200,
			body={
				'message': 'Subscriber found',
				'data': {
					'Type': 'Subscriber',
					'count': len(formated_subscriber),
					'subscribers': formated_subscriber
				}
			}
		)

	def __format_ranking_response(self, ranking: list) -> HttpResponse:
		formated_ranking = []
		for rank in ranking:
			formated_ranking.append({
				'link': rank.link,
				'total_subscribers': rank.total
			})

		return HttpResponse(
			status_code=200,
			body={
				'message': 'Ranking found',
				'data': {
					'Type': 'Ranking',
					'count': len(formated_ranking),
					'ranking': formated_ranking
				}
			}
		)