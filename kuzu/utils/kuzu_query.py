import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

# Execute Cypher query
response = conn.execute(
    """
    MATCH (n)-[r]->(m) RETURN n, r, m
    """
)
while response.has_next():
    print(response.get_next())