class Neo4jRepository(object):

    def __init__(self):
        import os
        from os.path import join, dirname
        from dotenv import load_dotenv
        from neo4j import GraphDatabase

        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)

        uri = os.environ.get("NEO4J_URL")
        user = os.environ.get("NEO4J_ID")
        password = os.environ.get("NEO4J_PW")

        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def create_node(self, name, label):
        with self._driver.session() as session:
            result = session.write_transaction(self._merge_and_return_node, name, label)
        return result

    def delete_node(self, name, label):
        with self._driver.session() as session:
            result = session.write_transaction(self._delete_and_return_node, name, label)
        return result

    @staticmethod
    def _merge_and_return_node(tx, name, label):
        result = tx.run("MERGE (n:%s {name: $name}) RETURN n" % (label), name=name)
        return result.single()[0]

    @staticmethod
    def _delete_and_return_node(tx, name, label):
        result = tx.run("MATCH (n:%s {name: $name}) DETACH DELETE n RETURN n" % (label), name=name)
        return result.single()[0]
