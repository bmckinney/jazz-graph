MERGE (a:Annotation{ uuid: 'e1da4f9c-7665-4cda-a081-520ee5ccb57a' })
SET a.name = 'Interview with Roy Haynes by Marc Myers for JazzWax.com'
SET a.date = '2008'
SET a.type = 'Interview'
SET a.databases = ['https://www.jazzwax.com/2024/11/roy-haynes-1925-2024.html']
SET a.content = "Marc Myers: No, no. It's just that I can hear your sensitivity and the conversation you're striking up on the spot with the musicians you're recording with.  Roy Haynes: That’s very true. I do do a lot of listening. I recently heard a Mary Lou Williams recording on the radio from 1970 with me on drums. It was a live recording. As I listened to it recently, I could feel myself listening to what she was doing, trying to catch up with her on drums, listening to see what direction she was going in. It was the first time I had ever heard what you're talking about. Joe Fields produced it. He was supposed to send me some more money. You can put that in there. [laughing]";

MATCH (p:Person {name: 'Roy Haynes'})
MATCH (a:Annotation{ uuid: 'e1da4f9c-7665-4cda-a081-520ee5ccb57a' })
MERGE (p)-[:CREATED { role: 'interviewee' }]->(a);

MERGE (person_f4de34178ad0:Person{ uuid: '4080f6a3-0cc0-47e4-af3a-f4de34178ad0' })
SET person_f4de34178ad0.name = 'Marc Myers'
SET person_f4de34178ad0.gender = 'Male'
SET person_f4de34178ad0.disambiguation = 'music journalist'
SET person_f4de34178ad0.birth_date = '1956-09-04'
SET person_f4de34178ad0.discogs = 'https://www.discogs.com/artist/2656380'
SET person_f4de34178ad0.wikidata = 'https://www.wikidata.org/wiki/Q6755774'
SET person_f4de34178ad0.musicbrainz = 'https://musicbrainz.org/artist/4080f6a3-0cc0-47e4-af3a-f4de34178ad0'
SET person_f4de34178ad0.source = 'musicbrainz.org';

MATCH (p:Person {name: 'Marc Myers'})
MATCH (a:Annotation{ uuid: 'e1da4f9c-7665-4cda-a081-520ee5ccb57a' })
MERGE (p)-[:CREATED { role: 'interviewer' }]->(a);

MATCH (r:Release {name: 'A Grand Night for Swinging'})
MATCH (a:Annotation{ uuid: 'e1da4f9c-7665-4cda-a081-520ee5ccb57a' })
MERGE (r)-[:HAS_ANNOTATION]->(a);