from neo4j import GraphDatabase


class Graph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    # populate hand-code data into graph database
    def manual_populate(self):
        with self.driver.session() as session:
            result = session.write_transaction(self._manual_populate)
            return "success"

    # TODO: improve cypher import statement
    @staticmethod
    def _manual_populate(tx):
        tx.run(
            "CREATE (:Method)<-[:_RELATED]-(:`Sub-category`)<-[:_RELATED]-(`Machine Learning`:`Root `)-["":_RELATED"
            "]->(:`Sub-category`)-[:_RELATED]->(:Method)-[:prerequisite]->(`Deep RL`:Method),""(`Machine Learning`)-["
            ":_RELATED]->(:`Sub-category`)-[:_RELATED]->(`Deep RL`)")

    # TODO: create methods for searching database for a given node + relation with a given property
    def cypher_search(self):
        pass


# if __name__ == "__main__":
uri = "bolt://3.84.92.216:7687"
user = "neo4j"
password = "exchanges-appraisals-intercoms"
app = Graph(uri, user, password)
print(app.manual_populate())
app.close()
