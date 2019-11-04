import pytest
from repositories.neo4j_repository import Neo4jRepository

class TestMecabRepository(object):

    @pytest.mark.api
    @pytest.mark.parametrize("node, expected", [
        ({'name': 'テストのためのNode', 'label': 'TestLabel'}, True),
    ])
    def test_create_node(self, node, expected):
        neo4j = Neo4jRepository()
        created = neo4j.create_node(node['name'], node['label'])
        deleted = neo4j.delete_node(node['name'], node['label'])
        # assert created == expected

