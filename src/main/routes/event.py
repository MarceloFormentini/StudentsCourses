from flask import Blueprint, jsonify, request
from src.http_types.http_request import HttpRequest
from src.model.repositories.eventos_repository import EventosRepository
from src.validators.events_creator_validator import events_creator_validator

from src.controllers.events.events_creator import EventsCreator

# agregador de rotas
event_route_bp = Blueprint('event_route', __name__)

@event_route_bp.route('/event', methods=['POST'])
def create_new_event():

	events_creator_validator(request=request)

	http_request = HttpRequest(body=request.json)

	event_repository = EventosRepository()
	events_creator = EventsCreator(event_repository=event_repository)

	http_response = events_creator.create(http_request=http_request)

	return jsonify(http_response.body), http_response.status_code