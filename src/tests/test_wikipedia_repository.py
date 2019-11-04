import pytest
from repositories.wikipedia_repository import WikipediaRepository

class TestWikipediaRepository(object):

    @pytest.mark.api
    @pytest.mark.parametrize("title, expected", [
        ("明仁", "明仁は、日本の第125代天皇、上皇。称号は繼宮、お印は榮。敬称は陛下。勲等は大勲位菊花章頸飾。"),
    ])
    def test_read_text(self, title, expected):
        wikipedia = WikipediaRepository()
        result = wikipedia.read_text(title)
        assert type(result) is str





