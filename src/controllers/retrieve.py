def read_wikipedia(title):
    from repositories.wikipedia_repository import WikipediaRepository
    wikipedia = WikipediaRepository()
    sanitized_text = wikipedia.read_text(title)

    from libs.text_utils import TextUtils
    text_utils = TextUtils()
    return text_utils.split2sentences(sanitized_text)


def read_node(title):
    lines = read_wikipedia(title)

    from services.graph import Graph
    graph = Graph()

    node_origins = []
    for sentence in lines:
        node_origins.extend(graph.nodes_in_paragraph(sentence))

    return node_origins

def merge_node(title):
    node_origins = read_node(title)

    from repositories.neo4j_repository import Neo4jRepository
    neo4j = Neo4jRepository()
    for node in node_origins:
        # print(node)
        neo4j.create_node(node['name'], node['label'])
        neo4j.delete_node(node['name'], node['label'])

