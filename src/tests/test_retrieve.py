import pytest

class TestRetrieve(object):

    @pytest.mark.api
    @pytest.mark.parametrize("title, expected", [
        ("明仁", True),
    ])
    def test_merge_node(self, title, expected):
        from controllers.retrieve import merge_node
        merge_node(title)
        # graph = Graph()
        # result = graph.nodes_in_paragraph(text)
        # assert result == expected




