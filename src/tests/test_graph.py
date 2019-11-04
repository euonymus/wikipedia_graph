import pytest
from services.graph import Graph

class TestGraph(object):

    @pytest.mark.parametrize("text, expected", [
        ("サン・マイクロシステムズは、アンディ・ベクトルシャイムがアメリカ合衆国カリフォルニアに本社を置いていたコンピュータの製造・ソフトウェア開発・ITサービス企業である。鈴木さんは苗字です。", [{'name': 'サン・マイクロシステムズ', 'label': 'Organization'}, {'name': 'アンディ・ベクトルシャイム', 'label': 'Person'}, {'name': 'アメリカ合衆国', 'label': 'Country'}, {'name': 'カリフォルニア', 'label': 'Area'}, {'name': 'ソフトウェア開発', 'label': 'Thing'}, {'name': 'IT', 'label': 'Thing'}]),
    ])
    def test_nodes_in_paragraph(self, text, expected):
        graph = Graph()
        result = graph.nodes_in_paragraph(text)
        assert result == expected




