import pytest
from repositories.cabocha_repository import CabochaRepository

class TestCabochaRepository(object):

    @pytest.mark.parametrize("sentence, expected", [
        ("浅田真央は伊藤の衣装を着用して競技に臨んだこともあり、「みどりさんの衣装を着るといつも調子がいい」と語っていた", True),
    ])
    def test_parse(self, sentence, expected):
        # cabocha = CabochaRepository()
        # result = cabocha.parse(sentence)
        # print(result)
        # # assert result == expected
        None

