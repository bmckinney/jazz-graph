
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

MERGE (v:Video{ uuid: '7d8a4069-4882-4da9-b10f-e9b20ee6d254' })
SET v.name = 'Stan Getz - Jazz Goes To College'
SET v.date = '1966-11-14'
SET v.duration = '49.56'
SET v.creator = 'BBC Four'
SET v.links = ['https://www.youtube.com/watch?v=70OuKeCOU5U'];

MATCH (e:Event {name: 'Stan Getz - Jazz Goes To College'})
MATCH (v:Video{ uuid: '7d8a4069-4882-4da9-b10f-e9b20ee6d254' })
MERGE (e)-[:HAS_VIDEO]->(v);

"""
)