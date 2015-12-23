// ---------------------------------------------------------------------------------
// ----- NODES ---------------------------------------------------------------------
// ---------------------------------------------------------------------------------

// artists
CREATE 
	(a1:Artist{
		uuid:'96af5214-891d-4c6e-9859-7944d9aab4dd', 
		name:'Miles Davis', 
		birth_date: '1926-05-26',
		death_date: '1991-08-21',
		genres: ['jazz'],
		gender: 'male',
		links: ['https://en.wikipedia.org/wiki/Miles_Davis','http://www.milesdavis.com/'],
		primary_instrument:'trumpet'}),
	(a2:Artist{uuid:'3804ccca-e5ec-4092-9cb2-2f8c159c73f6', name:'Cannonball Adderley', primary_instrument:'alto saxophone'}),
	(a3:Artist{uuid:'c547ecab-99d1-4708-a71e-b83d763d915c', name:'John Coltrane', primary_instrument:'tenor saxophone'}),
	(a4:Artist{uuid:'a0e9df5e-af97-487f-b3b4-ed83047dd8f6', name:'Wynton Kelly', primary_instrument:'piano'}),
	(a5:Artist{uuid:'671487a9-f769-4686-b29f-c27a021524ee', name:'Bill Evans', primary_instrument:'piano'}),
	(a6:Artist{uuid:'07685d0e-5e2f-4db5-81d2-3df3fa7c211f', name:'Paul Chambers', primary_instrument:'double bass'}),
	(a7:Artist{uuid:'09986808-0d8b-4338-a3f0-fa92bd083f06', name:'Jimmy Cobb', primary_instrument:'drums'})

// producers, engineers
CREATE 
	(a8:Artist{uuid:'2f7962ec-e058-4983-8ad9-d904f653daf6', name:'Teo Macero'}),
	(a9:Artist{uuid:'7fe93d1d-0e79-4966-9e8a-d58766864fb5', name:'Irving Townsend'}),
	(a10:Artist{uuid:'74b2c99e-1b70-479a-ba38-dccd7738280f', name:'Fred Plaut'}),
	(a11:Artist{uuid:'48d3c6e4-cb6e-48a8-8b3b-98c032bfe986', name:'Robert Herridge', links:['https://en.wikipedia.org/wiki/Robert_Herridge']}),
	(a12:Artist{uuid:'4232fb5c-709f-4853-9b14-d1dc2b0ff40a', name:'Gil Evans'})

// works
CREATE 
	(w1:Work{uuid:'18d0fa18-8342-4f07-9dd5-7f833d61d114', name:'Freddie Freeloader'}),
	(w2:Work{uuid:'3a0f600f-05e6-41b8-abff-8275b6db28df', name:'So What'}),
	(w3:Work{uuid:'70d60ab8-e27d-420a-8873-db9e3945b0bc', name:'Blue In Green'}),
	(w4:Work{uuid:'7de56ecc-8658-475a-8dcf-36edcfd182aa', name:'Flamenco Sketches'}),
	(w5:Work{uuid:'e3068fac-fff5-4352-b173-101215e99ea7', name:'All Blues'})

// performances
CREATE 
	(p1:Performance{uuid:'6b7e1912-6807-4542-9972-a9935c8633f3', name:'Freddie Freeloader', matrix:'CO62290-4', duration:'9:36'}),
	(p2:Performance{uuid:'ae3adad4-b6df-42de-8680-1da3e85a55d1', name:'So What', matrix:'CO62291-3', duration:'9:05'}),
	(p3:Performance{uuid:'c24e95f8-87e3-4c3c-9446-6627a86a11d2', name:'Blue In Green', matrix:'CO62292-5', duration:'5:29'}),
	(p4:Performance{uuid:'0e59ee35-35fc-40f2-8002-7f4e027ccf81', name:'Flamenco Sketches', matrix:'CO62293-6', duration:'9:21'}),
	(p5:Performance{uuid:'e98815f2-68c7-4b30-b734-909da715edf6', name:'All Blues', matrix:'CO62294-1', duration:'11:33'}),
	(p6:Performance{uuid:'88059b0d-d74d-41b0-a698-9077837a3faa', name:'So What'})

// sessions
CREATE 
	(s1:Session{
		uuid:'10202790-4ffd-4f8a-a3b5-0f8c3b265704', 
		name:'Kind of Blue: Miles Davis Sextet', 
		date:'1959-03-02', 
		type:'recording session'}),
	(s2:Session{
		uuid:'b91a5e28-d4f8-4c83-b9f3-2f5a658d2f51', 
		name:'Kind of Blue: Miles Davis Sextet', 
		date:'1959-04-22', 
		type:'recording session'}),
	(s3:Session{
		uuid:'cccc57ec-a06b-4566-8414-793d44668bf0', 
		name:'Miles Davis at The Robert Herridge Theater - The Sound of Miles Davis Live', 
		date:'1959-04-03', 
		type:'television appearance'})

// albums
CREATE 
	(alb1:Album{
		uuid:'7416678c-f49a-49b2-bc8c-05cb8ba1bc6a', 
		name:'Kind of Blue', 
		discode:'Columbia CL 1355', 
		date:'1959-07-17', 
		duration:'45:44', 
		links:['https://en.wikipedia.org/wiki/Kind_of_Blue', 'http://www.jazzdisco.org/miles-davis/catalog/#columbia-cl-1355']
	})

// labels
CREATE (lab1:Label{uuid:'fd2f2b6f-c478-43da-9628-eba4b8af7587', name:'Columbia Records', links:['https://en.wikipedia.org/wiki/Columbia_Records']})

// locations
CREATE (loc1:Location{name:'New York City', country:'United States', lat:'40.712784', lng:'-74.005941', venue:'Columbia 30th Street Studios', links:['https://en.wikipedia.org/wiki/CBS_30th_Street_Studio']})
CREATE (loc2:Location{name:'New York City', country:'United States', lat:'40.712784', lng:'-74.005941', venue:'CBS Studio 1, The Robert Herridge Theatre'})


// ---------------------------------------------------------------------------------
// ----- RELATIONSHIPS -------------------------------------------------------------
// ---------------------------------------------------------------------------------

// artist - work
CREATE 
	(a1)-[:COMPOSED]->(w1),
	(a1)-[:COMPOSED]->(w2),
	(a1)-[:COMPOSED]->(w3),
	(a1)-[:COMPOSED]->(w4),
	(a1)-[:COMPOSED]->(w5),
	(a5)-[:COMPOSED]->(w3),
	(a5)-[:COMPOSED]->(w4)

// artist - performance

// miles davis
CREATE 
	(a1)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(p1),
	(a1)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(p2),
	(a1)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(p3),
	(a1)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(p4),
	(a1)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(p5),
	(a1)-[:PARTICIPATED_IN {instruments:['trumpet']}]->(p6)


// john coltrane
CREATE 
	(a3)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(p1),
	(a3)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(p2),
	(a3)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(p3),
	(a3)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(p4),
	(a3)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(p5),
	(a3)-[:PARTICIPATED_IN {instruments:['tenor saxophone']}]->(p6)

// paul chambers
CREATE 
	(a6)-[:PARTICIPATED_IN {instruments:['double bass']}]->(p1),
	(a6)-[:PARTICIPATED_IN {instruments:['double bass']}]->(p2),
	(a6)-[:PARTICIPATED_IN {instruments:['double bass']}]->(p3),
	(a6)-[:PARTICIPATED_IN {instruments:['double bass']}]->(p4),
	(a6)-[:PARTICIPATED_IN {instruments:['double bass']}]->(p5),
	(a6)-[:PARTICIPATED_IN {instruments:['double bass']}]->(p6)

// jimmy cobb
CREATE 
	(a7)-[:PARTICIPATED_IN {instruments:['drums']}]->(p1),
	(a7)-[:PARTICIPATED_IN {instruments:['drums']}]->(p2),
	(a7)-[:PARTICIPATED_IN {instruments:['drums']}]->(p3),
	(a7)-[:PARTICIPATED_IN {instruments:['drums']}]->(p4),
	(a7)-[:PARTICIPATED_IN {instruments:['drums']}]->(p5),
	(a7)-[:PARTICIPATED_IN {instruments:['drums']}]->(p6)

// cannonball adderley
CREATE 
	(a2)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(p1),
	(a2)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(p2),
	(a2)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(p4),
	(a2)-[:PARTICIPATED_IN {instruments:['alto saxophone']}]->(p5)

// bill evans
CREATE 
	(a5)-[:PARTICIPATED_IN {instruments:['piano']}]->(p2),
	(a5)-[:PARTICIPATED_IN {instruments:['piano']}]->(p3),
	(a5)-[:PARTICIPATED_IN {instruments:['piano']}]->(p4),
	(a5)-[:PARTICIPATED_IN {instruments:['piano']}]->(p5)

// Wynton Kelly
CREATE (a4)-[:PARTICIPATED_IN {instruments:['piano']}]->(p1)

// gil evans
CREATE (a12)-[:PARTICIPATED_IN {roles:['conductor','arrangor']}]->(p6)

// robert herridge
CREATE (a11)-[:PARTICIPATED_IN {roles:['television producer','television host']}]->(s3)

// performance - work
CREATE 
	(p1)-[:PERFORMANCE_OF]->(w1),
	(p2)-[:PERFORMANCE_OF]->(w2),
	(p3)-[:PERFORMANCE_OF]->(w3),
	(p4)-[:PERFORMANCE_OF]->(w4),
	(p5)-[:PERFORMANCE_OF]->(w5),
	(p6)-[:PERFORMANCE_OF]->(w2)

// session - performances
CREATE 
	(s1)-[:HAS_PERFORMANCE]->(p1),
	(s1)-[:HAS_PERFORMANCE]->(p2),
	(s1)-[:HAS_PERFORMANCE]->(p3),
	(s2)-[:HAS_PERFORMANCE]->(p4),
	(s2)-[:HAS_PERFORMANCE]->(p5),
	(s3)-[:HAS_PERFORMANCE]->(p6)

// session - location
CREATE (s1)-[:HAS_LOCATION]->(loc1)
CREATE (s2)-[:HAS_LOCATION]->(loc1)
CREATE (s3)-[:HAS_LOCATION]->(loc2)

// album - performance
CREATE 
	(alb1)-[:HAS_TRACK {sequence:2}]->(p1),
	(alb1)-[:HAS_TRACK {sequence:1}]->(p2),
	(alb1)-[:HAS_TRACK {sequence:3}]->(p3),
	(alb1)-[:HAS_TRACK {sequence:5}]->(p4),
	(alb1)-[:HAS_TRACK {sequence:4}]->(p5)

// album - label
CREATE (alb1)-[:HAS_LABEL]->(lab1)

// album - producers, engineers, liner notes, etc.
CREATE 
	(a8)-[:PARTICIPATED_IN {roles:['producer']}]->(alb1),
	(a9)-[:PARTICIPATED_IN {roles:['producer']}]->(alb1),
	(a5)-[:PARTICIPATED_IN {roles:['original liner notes']}]->(alb1),
	(a10)-[:PARTICIPATED_IN {roles:['engineer']}]->(alb1)