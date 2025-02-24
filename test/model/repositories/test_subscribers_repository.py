import pytest
from src.model.repositories.subscribers_repository import SubscribersRepository

# marcação para pular o teste
@pytest.mark.skip(reason="Teste de integração - inserir no banco de dados")
def test_insert_subscribers():
	subscriber_info = {
		'nome': 'Marcelo Formentini',
		'email': 'marceloformentini74@gmail.com',
		'evento_id': 1
	}
	subscribers_repo = SubscribersRepository()
	subscribers_repo.insert(subscriber_info)

def test_select_subscribers():
	subscriber_email = 'marceloformentini74@gmail.com'
	subscriber_evento_id = 1
	subscribers_repo = SubscribersRepository()
	subscriber = subscribers_repo.select_subscriber(subscriber_email, subscriber_evento_id)
	assert subscriber.email == subscriber_email
	assert subscriber.evento_id == subscriber_evento_id