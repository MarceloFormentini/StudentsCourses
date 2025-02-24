import pytest
from src.model.repositories.eventos_repository import EventosRepository

# marcação para pular o teste
@pytest.mark.skip(reason="Teste de integração - inserir no banco de dados")
def test_insert_eventos():
	event_name = "EventoTeste"
	eventos_repo = EventosRepository()
	eventos_repo.insert(event_name)

# @pytest.mark.skip(reason="Teste de integração - consulta ao banco de dados")
def test_select_eventos():
	event_name = "EventoTeste"
	eventos_repo = EventosRepository()
	event = eventos_repo.select_event(event_name)
	assert event.nome == event_name