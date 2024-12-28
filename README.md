# jazz-graph
jazz discography represented as a structured property graph

## Kuzudb Implementation

[https://kuzudb.com/](https://kuzudb.com/)

## Adding new releases

### 1. Import a release from musicbrainz

```
poetry run python3 ./import/import-musicbrainz-release.py 065a2ee7-f9a2-4eb6-b8c0-722909072753 > ./cql/petrucciani-jazz-club-montmartre.cql
```

### 2. Import CQL into KuzuDB

```
cd kuzu
python3 ./utils/cql_to_kuzu.py
sudo bash ./utils/import_all_into_kuzu.sh
```

### 3. Synchronize local KuzuDB to remote 

```
scp -r /absolute_path/kuzu_db user@kuzu.example.com:/home/docker
```

### 4. Restart the KuzuDB explorer

```
docker restart <container_id_or_name>
```

## Example cypher queries using the KuzuDB CLI

### What are the songs and performers on "The Roy Haynes Trio" release?
```
kuzu> MATCH (r:Release {name: "The Roy Haynes Trio"})-[:HAS_TRACK]->(p:Performance) 
      MATCH (p)<-[part:PARTICIPATED_IN]-(person:Person) 
      RETURN p.name AS track, collect(person.name + "(" + part.instruments[1] + ")") AS performers;
┌───────────────────────┬──────────────────────────────────────────────────────────────┐
│ track                 │ performers                                                   │
│ STRING                │ STRING[]                                                     │
├───────────────────────┼──────────────────────────────────────────────────────────────┤
│ Wail                  │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Question and Answer   │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Shulie a Bop          │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Dear Old Stockholm    │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ It's Easy to Remember │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Prelude to a Kiss     │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Sippin' at Bells      │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Bright Mississippi    │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Folk Song             │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
│ Green Chimneys        │ [John Patitucci(bass),Danilo Pérez(piano),Roy Haynes(drums)] │
└───────────────────────┴──────────────────────────────────────────────────────────────┘
(10 tuples)
(2 columns)
Time: 1.15ms (compiling), 5.65ms (executing)

```

### What songs did Roy Haynes perform on September 10, 1999 and where?
```
kuzu> MATCH (a:Person{ name: "Roy Haynes"})-[:PARTICIPATED_IN]->(p:Performance{begin_date: "1999-09-10"})-[:HAS_PLACE]->(plc:Place)
      RETURN DISTINCT p.name, p.begin_date, plc.name;
┌────────────────────┬──────────────┬────────────────────┐
│ p.name             │ p.begin_date │ plc.name           │
│ STRING             │ STRING       │ STRING             │
├────────────────────┼──────────────┼────────────────────┤
│ Green Chimneys     │ 1999-09-10   │ Scullers Jazz Club │
│ Prelude to a Kiss  │ 1999-09-10   │ Scullers Jazz Club │
│ Sippin' at Bells   │ 1999-09-10   │ Scullers Jazz Club │
│ Bright Mississippi │ 1999-09-10   │ Scullers Jazz Club │
└────────────────────┴──────────────┴────────────────────┘
(4 tuples)
(3 columns)
Time: 1.49ms (compiling), 9.42ms (executing)

```

### What bassists did Roy Haynes perform the most with?
```
kuzu> MATCH (p1:Person {name: "Roy Haynes"})-[:PARTICIPATED_IN]->(perf:Performance)<-[part:PARTICIPATED_IN]-(p2:Person) 
      WHERE "bass" IN part.instruments RETURN p2.name, COUNT(*) AS numberOfPerformances 
      ORDER BY numberOfPerformances DESC LIMIT 5;
┌───────────────────┬──────────────────────┐
│ p2.name           │ numberOfPerformances │
│ STRING            │ INT64                │
├───────────────────┼──────────────────────┤
│ Christian McBride │ 12                   │
│ Gary Peacock      │ 12                   │
│ John Patitucci    │ 10                   │
│ Paul Chambers     │ 10                   │
│ David Wong        │ 10                   │
└───────────────────┴──────────────────────┘
(5 tuples)
(2 columns)
Time: 1.76ms (compiling), 4.56ms (executing)

```

### What bassists did Roy Haynes perform the most with in 1960?
```
kuzu> MATCH (p1:Person {name: "Roy Haynes"})-[:PARTICIPATED_IN]->(perf:Performance)<-[part:PARTICIPATED_IN]-(p2:Person) 
      WHERE "bass" IN part.instruments AND perf.begin_date STARTS WITH "1960" RETURN p2.name, COUNT(*) AS numberOfPerformances 
      ORDER BY numberOfPerformances DESC LIMIT 5;
┌─────────────────┬──────────────────────┐
│ p2.name         │ numberOfPerformances │
│ STRING          │ INT64                │
├─────────────────┼──────────────────────┤
│ Eddie DeHaas    │ 7                    │
│ George Duvivier │ 6                    │
│ Paul Chambers   │ 4                    │
└─────────────────┴──────────────────────┘
(3 tuples)
(2 columns)
Time: 1.79ms (compiling), 4.68ms (executing)

```

### When did Roy Haynes record at Rudy Van Gelder's studio and how many performances?
```
kuzu> MATCH (person:Person {name: "Roy Haynes"})-[part:PARTICIPATED_IN]->(performance:Performance)-[hp:HAS_PLACE]->(place:Place {name: "Van Gelder Studio"}) 
      RETURN DISTINCT hp.begin_date as dates, place.name as place, count(performance) as performances
      ORDER BY dates ASC;
┌────────────┬───────────────────┬──────────────┐
│ dates      │ place             │ performances │
│ STRING     │ STRING            │ INT64        │
├────────────┼───────────────────┼──────────────┤
│ 1958-11-14 │ Van Gelder Studio │ 6            │
│ 1960-05-27 │ Van Gelder Studio │ 6            │
│ 1960-07-05 │ Van Gelder Studio │ 7            │
│ 1960-12-21 │ Van Gelder Studio │ 5            │
│ 1961-02-23 │ Van Gelder Studio │ 6            │
│ 1961-03-14 │ Van Gelder Studio │ 7            │
│ 1962-05-16 │ Van Gelder Studio │ 4            │
│ 1962-05-23 │ Van Gelder Studio │ 3            │
│ 1963-04-10 │ Van Gelder Studio │ 6            │
│ 1963-11-08 │ Van Gelder Studio │ 7            │
│ 1963-11-10 │ Van Gelder Studio │ 5            │
│ 1963-12-13 │ Van Gelder Studio │ 7            │
└────────────┴───────────────────┴──────────────┘
(12 tuples)
(3 columns)
Time: 1.94ms (compiling), 8.21ms (executing)

```

### What Monk compositions has Roy Haynes performed?
```
kuzu> MATCH (person:Person {name: "Roy Haynes"})-[part:PARTICIPATED_IN]->(performance:Performance)-[:PERFORMANCE_OF]->(work:Work)<-[:COMPOSED]-(composer:Person {name: "Thelonious Monk"})
      RETURN DISTINCT work.name;
┌──────────────────────┐
│ work.name            │
│ STRING               │
├──────────────────────┤
│ Rhythm-a-Ning        │
│ ’Round Midnight      │
│ Eronel               │
│ Think of One         │
│ Little Rootie Tootie │
│ Reflections          │
│ Hackensack           │
│ Ask Me Now           │
│ Green Chimneys       │
│ Nutty                │
│          ·           │
│          ·           │
│          ·           │
│ Epistrophy           │
│ Bemsha Swing         │
│ Trinkle Tinkle       │
│ Let’s Cool One       │
│ Off Minor            │
│ Blue Monk            │
│ Misterioso           │
│ Bright Mississippi   │
│ Light Blue           │
│ In Walked Bud        │
└──────────────────────┘
(21 tuples, 20 shown)
(1 column)
Time: 3.84ms (compiling), 3.42ms (executing)
```

### What performances has Roy Haynes performed in with a trio?
```
kuzu> MATCH (p:Person)-[r:PARTICIPATED_IN]->(perf:Performance) 
      WHERE 'musician' IN r.roles 
      WITH perf, COLLECT(p.name) AS person_coll, COUNT(p) AS performerCount 
      WHERE performerCount = 3 AND "Roy Haynes" in person_coll
      RETURN perf.name, person_coll;
┌────────────────────────────┬──────────────────────────────────────────────┐
│ perf.name                  │ person_coll                                  │
│ STRING                     │ STRING[]                                     │
├────────────────────────────┼──────────────────────────────────────────────┤
│ Salt Peanuts               │ [Roy Haynes,Charles Mingus,Bud Powell]       │
│ Trio Improvisation, Part 3 │ [Chick Corea,Roy Haynes,Miroslav Vitouš]     │
│ Eronel                     │ [Chick Corea,Roy Haynes,Miroslav Vitouš]     │
│ Cold Bordeaux Blues        │ [Roy Haynes,Duke Jordan,Wilbur Little]       │
│ Flight to Japan            │ [Roy Haynes,Duke Jordan,Wilbur Little]       │
│ Cinco y quatro             │ [Jaki Byard,Ron Carter,Roy Haynes]           │
│ Sweet and Lovely           │ [Roy Haynes,Eddie DeHaas,Richard Wyands]     │
│ Bebop                      │ [Kenny Barron,Charlie Haden,Roy Haynes]      │
│ Never Too Far Away         │ [Roy Haynes,Dave Holland,Pat Metheny]        │
│ Sippin' at Bells           │ [Roy Haynes,Danilo Pérez,John Patitucci]     │
│             ·              │                      ·                       │
│             ·              │                      ·                       │
│             ·              │                      ·                       │
│ Spanish Moods              │ [Hampton Hawes,Roy Haynes,Cecil McBee]       │
│ To My Wife                 │ [Jaki Byard,Ron Carter,Roy Haynes]           │
│ Wanton Spirit              │ [Kenny Barron,Charlie Haden,Roy Haynes]      │
│ Love Letters               │ [Roy Haynes,Dave Holland,John Scofield]      │
│ Lover Come Back to Me      │ [Roy Haynes,Oscar Pettiford,Bud Powell]      │
│ Speak Low                  │ [Roy Haynes,Eddie DeHaas,Richard Wyands]     │
│ Processional               │ [George Cables,Roy Haynes,Kenneth Nash]      │
│ Think of One               │ [Chick Corea,Roy Haynes,Miroslav Vitouš]     │
│ Mr. KJ                     │ [Roy Haynes,Gary Peacock,Michel Petrucciani] │
│ I've Got You Under My Skin │ [Roy Haynes,Charles Mingus,Bud Powell]       │
└────────────────────────────┴──────────────────────────────────────────────┘
(123 tuples, 20 shown)
(2 columns)
Time: 0.98ms (compiling), 17.62ms (executing)
```


### What trios has Roy Haynes performed in and how often?
```
kuzu> MATCH (p:Person)-[r:PARTICIPATED_IN]->(perf:Performance) 
      WHERE 'musician' IN r.roles 
      WITH perf, COLLECT(p.name) AS person_coll, COUNT(p) AS performerCount 
      WHERE performerCount = 3 AND "Roy Haynes" in person_coll
      WITH count(perf) AS perf_count, person_coll as trio
      ORDER BY perf_count DESC LIMIT 100
      RETURN DISTINCT trio, perf_count;
┌──────────────────────────────────────────────┬────────────┐
│ trio                                         │ perf_count │
│ STRING[]                                     │ INT64      │
├──────────────────────────────────────────────┼────────────┤
│ [Chick Corea,Roy Haynes,Miroslav Vitouš]     │ 20         │
│ [Roy Haynes,Gary Peacock,Michel Petrucciani] │ 12         │
│ [Roy Haynes,Duke Jordan,Wilbur Little]       │ 11         │
│ [Kenny Barron,Charlie Haden,Roy Haynes]      │ 10         │
│ [Roy Haynes,Danilo Pérez,John Patitucci]     │ 10         │
│ [Roy Haynes,Dave Holland,Pat Metheny]        │ 9          │
│ [Roy Haynes,Oscar Pettiford,Bud Powell]      │ 8          │
│ [Jaki Byard,Ron Carter,Roy Haynes]           │ 7          │
│ [Roy Haynes,Eddie DeHaas,Richard Wyands]     │ 7          │
│ [Roy Haynes,Charles Mingus,Bud Powell]       │ 6          │
│                      ·                       │     ·      │
│                      ·                       │     ·      │
│                      ·                       │     ·      │
│ [Hampton Hawes,Roy Haynes,Cecil McBee]       │ 4          │
│ [Roy Haynes,Fred Lacey,Rodney Richardson]    │ 3          │
│ [Roy Haynes,Dave Holland,John Scofield]      │ 2          │
│ [Roy Haynes,Tommy Potter,Bud Powell]         │ 2          │
│ [Kenny Barron,Roy Haynes,Christian McBride]  │ 1          │
│ [Richard Davis,Roy Haynes,Andrew Hill]       │ 1          │
│ [Roy Haynes,Chick Corea,Miroslav Vitouš]     │ 1          │
│ [Adrian Acia,Joe Benjamin,Roy Haynes]        │ 1          │
│ [Chick Corea,Roy Haynes,Christian McBride]   │ 1          │
│ [George Cables,Roy Haynes,Kenneth Nash]      │ 1          │
└──────────────────────────────────────────────┴────────────┘
(21 tuples, 20 shown)
(2 columns)
Time: 1.20ms (compiling), 13.60ms (executing)

```

### Shortest path queries

#### What is the single shortest path between Roy Haynes and Chick Corea?
```
kuzu> MATCH p = (a)-[part:PARTICIPATED_IN* SHORTEST 1..3 ]-(b)
      WHERE a.name = 'Roy Haynes' AND b.name = 'Chick Corea'
      RETURN length(part) AS length;
┌────────┐
│ length │
│ INT64  │
├────────┤
│ 2      │
└────────┘
(1 tuple)
(1 column)
Time: 1.93ms (compiling), 4.72ms (executing)
```

#### How many shortest paths are there between Roy Haynes and Chick Corea?
```
kuzu> MATCH p = (a)-[part:PARTICIPATED_IN* ALL SHORTEST 1..3 ]-(b)
      WHERE a.name = 'Roy Haynes' AND b.name = 'Chick Corea'
      RETURN COUNT(*) AS num_shortest_path;
┌───────────────────┐
│ num_shortest_path │
│ INT64             │
├───────────────────┤
│ 53                │
└───────────────────┘
(1 tuple)
(1 column)
Time: 2.04ms (compiling), 5.46ms (executing)
```

