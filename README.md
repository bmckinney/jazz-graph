# jazz-graph
jazz discography represented as a neo4j graph

#### example queries
```
// artists & performances in session(s)
MATCH (s:Session { name: "Kind of Blue: Miles Davis Sextet" })-[:HAS_PERFORMANCE]->(p)<-[:PARTICIPATED_IN]-(a)
RETURN s, a, p;

// artists & performances in album(s)
MATCH (r:Release { name: "Kind of Blue" })-[:HAS_TRACK]->(p)<-[:PARTICIPATED_IN]-(a)
RETURN r, a, p;

// sessions by an artist
MATCH (a:Artist{ name: "Miles Davis"})-[:PARTICIPATED_IN]->(p)<-[:HAS_PERFORMANCE]-(s:Session)-[:HAS_LOCATION]->(l)
return DISTINCT s.name, s.date, l.name, l.venue;

```
