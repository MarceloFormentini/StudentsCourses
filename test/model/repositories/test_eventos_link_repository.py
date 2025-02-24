import pytest
from src.model.repositories.eventos_link_repository import EventosLinkRepository

@pytest.mark.skip(reason="Teste de integração - inserir no banco de dados")
def test_insert_eventos_link():
	repository = EventosLinkRepository()
	repository.insert(1, 3)