
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_2289a1525181:Release{ uuid: 'a581e1e1-40f2-4f32-932a-2289a1525181' })
SET release_2289a1525181.name = 'At The Five Spot Cafe, New York City, August 1958'
SET release_2289a1525181.country = 'IT'
SET release_2289a1525181.date = '1992'
SET release_2289a1525181.format = 'CD'
SET release_2289a1525181.discode = 'CD 53112'
SET release_2289a1525181.discogs = 'https://www.discogs.com/release/1435112'
SET release_2289a1525181.musicbrainz = 'http://musicbrainz.org/release/a581e1e1-40f2-4f32-932a-2289a1525181'
SET release_2289a1525181.source = 'musicbrainz.org'


MERGE (person_fbf258bd1250:Person{ uuid: '30842fc5-6f84-4cd4-bb5e-fbf258bd1250' }) 
SET person_fbf258bd1250.name = 'Ray Fowler'
SET person_fbf258bd1250.gender = 'Male'
SET person_fbf258bd1250.disambiguation = 'US recording engineer'
SET person_fbf258bd1250.country = 'US'
SET person_fbf258bd1250.allmusic = 'https://www.allmusic.com/artist/mn0000409242'
SET person_fbf258bd1250.discogs = 'https://www.discogs.com/artist/295649'
SET person_fbf258bd1250.databases = ['https://rateyourmusic.com/artist/ray_fowler']
SET person_fbf258bd1250.musicbrainz = 'https://musicbrainz.org/artist/30842fc5-6f84-4cd4-bb5e-fbf258bd1250'
SET person_fbf258bd1250.source = 'musicbrainz.org'


MERGE (person_6f0a331cc1ca:Person{ uuid: '2c090b57-5e9d-49c5-9b71-6f0a331cc1ca' }) 
SET person_6f0a331cc1ca.name = 'Roy Haynes'
SET person_6f0a331cc1ca.gender = 'Male'
SET person_6f0a331cc1ca.disambiguation = 'American jazz drummer and bandleader'
SET person_6f0a331cc1ca.country = 'US'
SET person_6f0a331cc1ca.allmusic = 'https://www.allmusic.com/artist/mn0000290464'
SET person_6f0a331cc1ca.bbc = 'https://www.bbc.co.uk/music/artists/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.discogs = 'https://www.discogs.com/artist/255556'
SET person_6f0a331cc1ca.imdb = 'https://www.imdb.com/name/nm0371542/'
SET person_6f0a331cc1ca.viaf = 'http://viaf.org/viaf/84975999'
SET person_6f0a331cc1ca.wikidata = 'https://www.wikidata.org/wiki/Q448235'
SET person_6f0a331cc1ca.databases = ['http://d-nb.info/gnd/134400623', 'http://id.loc.gov/authorities/names/n81140108', 'https://catalogue.bnf.fr/ark:/12148/cb13895060w', 'http://snaccooperative.org/ark:/99166/w6fj33d4', 'https://www.worldcat.org/identities/lccn-n81140108']
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'


MERGE (person_743eba86808c:Person{ uuid: 'f9625cf4-1436-4f2c-bd5e-743eba86808c' }) 
SET person_743eba86808c.name = 'Johnny Griffin'
SET person_743eba86808c.gender = 'Male'
SET person_743eba86808c.country = 'US'
SET person_743eba86808c.allmusic = 'https://www.allmusic.com/artist/mn0000213510'
SET person_743eba86808c.discogs = 'https://www.discogs.com/artist/251333'
SET person_743eba86808c.imdb = 'https://www.imdb.com/name/nm0341256/'
SET person_743eba86808c.viaf = 'http://viaf.org/viaf/49408148'
SET person_743eba86808c.wikidata = 'https://www.wikidata.org/wiki/Q708439'
SET person_743eba86808c.databases = ['http://d-nb.info/gnd/13439108X', 'http://id.loc.gov/authorities/names/n82099703', 'https://catalogue.bnf.fr/ark:/12148/cb13894727r', 'http://snaccooperative.org/ark:/99166/w64j0mfv', 'https://www.worldcat.org/identities/lccn-n82099703']
SET person_743eba86808c.musicbrainz = 'https://musicbrainz.org/artist/f9625cf4-1436-4f2c-bd5e-743eba86808c'
SET person_743eba86808c.isni_list = ['http://isni.org/isni/0000000118159720']
SET person_743eba86808c.source = 'musicbrainz.org'


MERGE (person_14e6a1dda090:Person{ uuid: '2956e70b-3644-4ec6-a95a-14e6a1dda090' }) 
SET person_14e6a1dda090.name = 'Orrin Keepnews'
SET person_14e6a1dda090.gender = 'Male'
SET person_14e6a1dda090.country = 'US'
SET person_14e6a1dda090.allmusic = 'https://www.allmusic.com/artist/mn0000894236'
SET person_14e6a1dda090.discogs = 'https://www.discogs.com/artist/254946'
SET person_14e6a1dda090.viaf = 'http://viaf.org/viaf/52169488'
SET person_14e6a1dda090.wikidata = 'https://www.wikidata.org/wiki/Q352028'
SET person_14e6a1dda090.databases = ['http://d-nb.info/gnd/1068085649', 'http://id.loc.gov/authorities/names/n81071421', 'https://catalogue.bnf.fr/ark:/12148/cb163738346', 'https://rateyourmusic.com/artist/orrin_keepnews', 'https://www.worldcat.org/identities/lccn-n81071421']
SET person_14e6a1dda090.musicbrainz = 'https://musicbrainz.org/artist/2956e70b-3644-4ec6-a95a-14e6a1dda090'
SET person_14e6a1dda090.isni_list = ['http://isni.org/isni/000000010901399X']
SET person_14e6a1dda090.source = 'musicbrainz.org'


MERGE (person_5260b4274ed4:Person{ uuid: '8e8c7417-c905-46b1-b42a-5260b4274ed4' }) 
SET person_5260b4274ed4.name = 'Thelonious Monk'
SET person_5260b4274ed4.gender = 'Male'
SET person_5260b4274ed4.country = 'US'
SET person_5260b4274ed4.allmusic = 'https://www.allmusic.com/artist/mn0000490416'
SET person_5260b4274ed4.bbc = 'https://www.bbc.co.uk/music/artists/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.discogs = 'https://www.discogs.com/artist/145256'
SET person_5260b4274ed4.imdb = 'https://www.imdb.com/name/nm0598243/'
SET person_5260b4274ed4.viaf = 'http://viaf.org/viaf/44485892'
SET person_5260b4274ed4.wikidata = 'https://www.wikidata.org/wiki/Q109612'
SET person_5260b4274ed4.databases = ['http://d-nb.info/gnd/118826158', 'http://id.loc.gov/authorities/names/n82218969', 'https://catalogue.bnf.fr/ark:/12148/cb13897622g', 'http://snaccooperative.org/ark:/99166/w6j38zvn', 'https://rateyourmusic.com/artist/thelonious_monk', 'https://www.worldcat.org/identities/lccn-n82218969']
SET person_5260b4274ed4.musicbrainz = 'https://musicbrainz.org/artist/8e8c7417-c905-46b1-b42a-5260b4274ed4'
SET person_5260b4274ed4.isni_list = ['http://isni.org/isni/0000000120249127']
SET person_5260b4274ed4.source = 'musicbrainz.org'


MERGE (person_9c4e5870c23a:Person{ uuid: 'aadac3a5-76d0-4198-b878-9c4e5870c23a' }) 
SET person_9c4e5870c23a.name = 'Ahmed Abdul-Malik'
SET person_9c4e5870c23a.gender = 'Male'
SET person_9c4e5870c23a.country = 'US'
SET person_9c4e5870c23a.allmusic = 'https://www.allmusic.com/artist/mn0000602006'
SET person_9c4e5870c23a.discogs = 'https://www.discogs.com/artist/260912'
SET person_9c4e5870c23a.viaf = 'http://viaf.org/viaf/66650902'
SET person_9c4e5870c23a.wikidata = 'https://www.wikidata.org/wiki/Q401088'
SET person_9c4e5870c23a.wikipedia = 'https://en.wikipedia.org/wiki/Ahmed_Abdul-Malik'
SET person_9c4e5870c23a.databases = ['http://d-nb.info/gnd/134590031', 'http://id.loc.gov/authorities/names/n80151158', 'https://catalogue.bnf.fr/ark:/12148/cb13890558h', 'https://www.worldcat.org/identities/lccn-n80151158']
SET person_9c4e5870c23a.musicbrainz = 'https://musicbrainz.org/artist/aadac3a5-76d0-4198-b878-9c4e5870c23a'
SET person_9c4e5870c23a.isni_list = ['http://isni.org/isni/0000000055149073']
SET person_9c4e5870c23a.source = 'musicbrainz.org'

// labels

MERGE (label_6ecd676f62a3:Label{ uuid: 'a557a1e8-8a3b-4004-bbee-6ecd676f62a3' })
SET label_6ecd676f62a3.name= 'Giants of Jazz'

// performances

MERGE (perf_f5094fa7715a:Performance{ uuid: 'a49f1c8f-3515-4bc1-bc2b-f5094fa7715a' })
SET perf_f5094fa7715a.name = 'Blue Monk'
SET perf_f5094fa7715a.duration = '8:31'
SET perf_f5094fa7715a.begin_date = '1958-08-07'
SET perf_f5094fa7715a.end_date = '1958-08-07'
SET perf_f5094fa7715a.source = 'musicbrainz.org'


MERGE (perf_b4fe927de696:Performance{ uuid: '87ff206b-bfa3-4057-81fe-b4fe927de696' })
SET perf_b4fe927de696.name = 'Nutty'
SET perf_b4fe927de696.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_b4fe927de696.duration = '5:24'
SET perf_b4fe927de696.begin_date = '1958-08-07'
SET perf_b4fe927de696.end_date = '1958-08-07'
SET perf_b4fe927de696.source = 'musicbrainz.org'


MERGE (perf_29769930d684:Performance{ uuid: '56eafd74-1b13-44ff-8ead-29769930d684' })
SET perf_29769930d684.name = 'Let’s Cool One'
SET perf_29769930d684.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_29769930d684.duration = '9:15'
SET perf_29769930d684.begin_date = '1958-08-07'
SET perf_29769930d684.end_date = '1958-08-07'
SET perf_29769930d684.source = 'musicbrainz.org'


MERGE (perf_54503759b35f:Performance{ uuid: 'b17d37cc-eb5e-462d-b63b-54503759b35f' })
SET perf_54503759b35f.name = 'In Walked Bud'
SET perf_54503759b35f.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_54503759b35f.duration = '11:22'
SET perf_54503759b35f.begin_date = '1958-08-07'
SET perf_54503759b35f.end_date = '1958-08-07'
SET perf_54503759b35f.source = 'musicbrainz.org'


MERGE (perf_1c85088e2ca0:Performance{ uuid: '88d5b731-e049-4ccb-9b52-1c85088e2ca0' })
SET perf_1c85088e2ca0.name = 'Misterioso'
SET perf_1c85088e2ca0.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_1c85088e2ca0.duration = '10:52'
SET perf_1c85088e2ca0.begin_date = '1958-08-07'
SET perf_1c85088e2ca0.end_date = '1958-08-07'
SET perf_1c85088e2ca0.source = 'musicbrainz.org'


MERGE (perf_ee191f18a63e:Performance{ uuid: '169d55af-f44c-4931-9a02-ee191f18a63e' })
SET perf_ee191f18a63e.name = 'Light Blue'
SET perf_ee191f18a63e.duration = '5:15'
SET perf_ee191f18a63e.begin_date = '1958-08-07'
SET perf_ee191f18a63e.end_date = '1958-08-07'
SET perf_ee191f18a63e.source = 'musicbrainz.org'


MERGE (perf_6bd80d94399e:Performance{ uuid: '429a1e70-bca6-44c9-a774-6bd80d94399e' })
SET perf_6bd80d94399e.name = 'Coming on the Hudson'
SET perf_6bd80d94399e.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_6bd80d94399e.duration = '5:24'
SET perf_6bd80d94399e.begin_date = '1958-08-07'
SET perf_6bd80d94399e.end_date = '1958-08-07'
SET perf_6bd80d94399e.source = 'musicbrainz.org'


MERGE (perf_8edece462bd4:Performance{ uuid: '03f639cb-8afb-4f75-ac67-8edece462bd4' })
SET perf_8edece462bd4.name = 'Rhythm-A-Ning'
SET perf_8edece462bd4.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_8edece462bd4.duration = '9:26'
SET perf_8edece462bd4.begin_date = '1958-08-07'
SET perf_8edece462bd4.end_date = '1958-08-07'
SET perf_8edece462bd4.source = 'musicbrainz.org'


MERGE (perf_4f16a74c8237:Performance{ uuid: 'd268fcb2-6380-4496-bf92-4f16a74c8237' })
SET perf_4f16a74c8237.name = 'Epistrophy (theme)'
SET perf_4f16a74c8237.disambiguation = 'live, 1958-08-07: Five Spot, New York, NY, USA'
SET perf_4f16a74c8237.duration = '1:05'
SET perf_4f16a74c8237.begin_date = '1958-08-07'
SET perf_4f16a74c8237.end_date = '1958-08-07'
SET perf_4f16a74c8237.source = 'musicbrainz.org'




// labels
MERGE (release_2289a1525181)-[:HAS_LABEL]->(label_6ecd676f62a3)


// tracks
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_f5094fa7715a)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_b4fe927de696)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_29769930d684)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_54503759b35f)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_1c85088e2ca0)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_ee191f18a63e)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_6bd80d94399e)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_8edece462bd4)
MERGE (release_2289a1525181)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_4f16a74c8237)

// works

MERGE (person_736867f1ba50:Person{ uuid: '48eaf8a1-6e44-488c-a91a-736867f1ba50' }) 
SET person_736867f1ba50.name = 'Kenny Clarke'
SET person_736867f1ba50.gender = 'Male'
SET person_736867f1ba50.country = 'US'
SET person_736867f1ba50.allmusic = 'https://www.allmusic.com/artist/mn0000081796'
SET person_736867f1ba50.discogs = 'https://www.discogs.com/artist/228917'
SET person_736867f1ba50.imdb = 'https://www.imdb.com/name/nm0164858/'
SET person_736867f1ba50.viaf = 'http://viaf.org/viaf/116335684'
SET person_736867f1ba50.wikidata = 'https://www.wikidata.org/wiki/Q346779'
SET person_736867f1ba50.databases = ['http://d-nb.info/gnd/118834827', 'http://id.loc.gov/authorities/names/n81055676', 'https://catalogue.bnf.fr/ark:/12148/cb13892538c', 'http://snaccooperative.org/ark:/99166/w6cj91b2', 'https://nla.gov.au/nla.party-1176449', 'https://rateyourmusic.com/artist/kenny_clarke', 'https://www.worldcat.org/identities/lccn-n81055676']
SET person_736867f1ba50.musicbrainz = 'https://musicbrainz.org/artist/48eaf8a1-6e44-488c-a91a-736867f1ba50'
SET person_736867f1ba50.isni_list = ['http://isni.org/isni/0000000084131382']
SET person_736867f1ba50.source = 'musicbrainz.org'


MERGE (work_e229183b0762:Work{ uuid: '6b1949e5-0f1c-3768-923f-e229183b0762' })
SET work_e229183b0762.name = 'Epistrophy'
SET work_e229183b0762.iswc = 'T-070.049.520-0'
SET work_e229183b0762.type = 'Song'
SET work_e229183b0762.wikidata = 'https://www.wikidata.org/wiki/Q5383642'
SET work_e229183b0762.musicbrainz = 'https://musicbrainz.org/work/6b1949e5-0f1c-3768-923f-e229183b0762'
SET work_e229183b0762.source = 'musicbrainz.org'


MERGE (work_a64223e0e713:Work{ uuid: '960f8068-8bf6-39b6-bf22-a64223e0e713' })
SET work_a64223e0e713.name = 'Light Blue'
SET work_a64223e0e713.iswc = 'T-700.037.461-0'
SET work_a64223e0e713.type = 'Song'
SET work_a64223e0e713.source = 'musicbrainz.org'


MERGE (work_744a53e360ba:Work{ uuid: '3e519d37-02f5-3fe4-b1ff-744a53e360ba' })
SET work_744a53e360ba.name = 'Blue Monk'
SET work_744a53e360ba.iswc = 'T-700.002.943-8'
SET work_744a53e360ba.type = 'Song'
SET work_744a53e360ba.wikidata = 'https://www.wikidata.org/wiki/Q2905615'
SET work_744a53e360ba.musicbrainz = 'https://musicbrainz.org/work/3e519d37-02f5-3fe4-b1ff-744a53e360ba'
SET work_744a53e360ba.source = 'musicbrainz.org'


MERGE (work_d5e438d24bc1:Work{ uuid: 'f8e0d620-1b66-31da-ade7-d5e438d24bc1' })
SET work_d5e438d24bc1.name = 'Misterioso'
SET work_d5e438d24bc1.iswc = 'T-700.044.720-3'
SET work_d5e438d24bc1.type = 'Song'
SET work_d5e438d24bc1.source = 'musicbrainz.org'


MERGE (work_ecaeddf44a98:Work{ uuid: 'ee619352-ce88-3fe2-a065-ecaeddf44a98' })
SET work_ecaeddf44a98.name = 'Rhythm-a-Ning'
SET work_ecaeddf44a98.iswc = 'T-700.057.764-2'
SET work_ecaeddf44a98.type = 'Song'
SET work_ecaeddf44a98.source = 'musicbrainz.org'


MERGE (work_56d82de9b78b:Work{ uuid: '87840895-875d-435f-a473-56d82de9b78b' })
SET work_56d82de9b78b.name = 'Nutty'
SET work_56d82de9b78b.iswc = 'T-700.049.419-1'
SET work_56d82de9b78b.type = 'Song'
SET work_56d82de9b78b.musicbrainz = 'https://musicbrainz.org/work/87840895-875d-435f-a473-56d82de9b78b'
SET work_56d82de9b78b.source = 'musicbrainz.org'


MERGE (work_7d4e19f32431:Work{ uuid: 'd6d6dcb5-36ee-3f6b-abcd-7d4e19f32431' })
SET work_7d4e19f32431.name = 'Coming on the Hudson'
SET work_7d4e19f32431.iswc = 'T-700.006.756-3'
SET work_7d4e19f32431.type = 'Song'
SET work_7d4e19f32431.source = 'musicbrainz.org'


MERGE (work_182364c981bb:Work{ uuid: '7e3478dc-b809-3b94-8e06-182364c981bb' })
SET work_182364c981bb.name = 'In Walked Bud'
SET work_182364c981bb.iswc = 'T-070.241.179-7'
SET work_182364c981bb.type = 'Song'
SET work_182364c981bb.wikidata = 'https://www.wikidata.org/wiki/Q3149674'
SET work_182364c981bb.musicbrainz = 'https://musicbrainz.org/work/7e3478dc-b809-3b94-8e06-182364c981bb'
SET work_182364c981bb.source = 'musicbrainz.org'


MERGE (work_daf774164548:Work{ uuid: 'f138b376-72a8-3338-842c-daf774164548' })
SET work_daf774164548.name = 'Let’s Cool One'
SET work_daf774164548.iswc = 'T-700.036.671-4'
SET work_daf774164548.type = 'Song'
SET work_daf774164548.source = 'musicbrainz.org'



// performances of
MERGE (perf_4f16a74c8237)-[:PERFORMANCE_OF]->(work_e229183b0762)
MERGE (perf_ee191f18a63e)-[:PERFORMANCE_OF]->(work_a64223e0e713)
MERGE (perf_f5094fa7715a)-[:PERFORMANCE_OF]->(work_744a53e360ba)
MERGE (perf_1c85088e2ca0)-[:PERFORMANCE_OF]->(work_d5e438d24bc1)
MERGE (perf_8edece462bd4)-[:PERFORMANCE_OF]->(work_ecaeddf44a98)
MERGE (perf_b4fe927de696)-[:PERFORMANCE_OF]->(work_56d82de9b78b)
MERGE (perf_6bd80d94399e)-[:PERFORMANCE_OF]->(work_7d4e19f32431)
MERGE (perf_54503759b35f)-[:PERFORMANCE_OF]->(work_182364c981bb)
MERGE (perf_29769930d684)-[:PERFORMANCE_OF]->(work_daf774164548)


// composers
MERGE (person_736867f1ba50)-[:COMPOSED]->(work_e229183b0762)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_e229183b0762)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_a64223e0e713)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_744a53e360ba)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_d5e438d24bc1)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_ecaeddf44a98)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_56d82de9b78b)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_7d4e19f32431)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_182364c981bb)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_daf774164548)


// place nodes

MERGE (place_b90c91be7781:Place{ uuid: '47f8291d-c765-465d-a363-b90c91be7781' })
SET place_b90c91be7781.name = 'Five Spot'
SET place_b90c91be7781.source = 'musicbrainz.org'


// place relationships
MERGE (perf_f5094fa7715a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_b4fe927de696)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_29769930d684)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_54503759b35f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_1c85088e2ca0)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_ee191f18a63e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_6bd80d94399e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_8edece462bd4)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)
MERGE (perf_4f16a74c8237)-[:HAS_PLACE { type: 'recorded at', begin_date: '1958-08-07', end_date: '1958-08-07' }]->(place_b90c91be7781)

MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_f5094fa7715a)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f5094fa7715a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f5094fa7715a)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f5094fa7715a)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b4fe927de696)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_b4fe927de696)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b4fe927de696)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b4fe927de696)
MERGE (person_14e6a1dda090)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_b4fe927de696)
MERGE (person_fbf258bd1250)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b4fe927de696)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_29769930d684)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_29769930d684)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_29769930d684)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_29769930d684)
MERGE (person_14e6a1dda090)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_29769930d684)
MERGE (person_fbf258bd1250)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_29769930d684)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_54503759b35f)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_54503759b35f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_54503759b35f)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_54503759b35f)
MERGE (person_14e6a1dda090)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_54503759b35f)
MERGE (person_fbf258bd1250)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_54503759b35f)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1c85088e2ca0)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_1c85088e2ca0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1c85088e2ca0)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1c85088e2ca0)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_ee191f18a63e)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_ee191f18a63e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ee191f18a63e)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ee191f18a63e)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass', 'double bass'] }]->(perf_6bd80d94399e)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_6bd80d94399e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6bd80d94399e)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6bd80d94399e)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_8edece462bd4)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8edece462bd4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8edece462bd4)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8edece462bd4)
MERGE (person_9c4e5870c23a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_4f16a74c8237)
MERGE (person_743eba86808c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_4f16a74c8237)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_4f16a74c8237)
MERGE (person_5260b4274ed4)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_4f16a74c8237)



"""
)