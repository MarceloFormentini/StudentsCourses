from cerberus import Validator

def events_creator_validator(request: any):
	body_validator = Validator({
		'data': {
			'type': 'dict',
			'schema':{
				'name':{'type': 'string', 'required': True, 'empty': False}
			}
		}
	})

	response = body_validator.validate(request.json)
	print(body_validator.errors)
	return response