# jazz-graph
jazz discography represented as a neo4j graph



#### What are the songs and performers on "The Roy Haynes Trio" release?
```
MATCH (r:Release { name: "The Roy Haynes Trio" })-[:HAS_TRACK]->(p)<-[:PARTICIPATED_IN]-(a)
RETURN r, a, p;
```
![Alt text](https://github.com/bmckinney/jazz-graph/blob/master/screenshots/haynes-trio-release.png?raw=true "Roy Haynes Trio Release")

#### What songs did Roy Haynes perform on September 10, 1999 and where?
```
MATCH (a:Person{ name: "Roy Haynes"})-[:PARTICIPATED_IN]->(p:Performance{begin: "1999-09-10"})-[:HAS_PLACE]->(plc:Place)
return DISTINCT p.name, p.begin, plc.name;
```
![Alt text](https://github.com/bmckinney/jazz-graph/blob/master/screenshots/haynes-trio-scullers-session.png?raw=true "Roy Haynes Trio Scullers Session")
