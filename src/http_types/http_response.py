import json

class HttpResponse:
	def __init__(self, body: dict, status_code: int) -> None:
		self.body = body
		self.status_code = status_code

	def to_dict(self) -> dict:
		return {
			'body': self.body,
			'status_code': self.status_code
		}

	def to_json(self) -> str:
		return json.dumps(self.to_dict())