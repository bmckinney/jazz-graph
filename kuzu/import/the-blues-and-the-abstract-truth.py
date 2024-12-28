
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_8655f949fa5f:Release{ uuid: '0bc26986-223f-447b-bef9-8655f949fa5f' })
SET release_8655f949fa5f.name = 'The Blues and the Abstract Truth'
SET release_8655f949fa5f.country = 'US'
SET release_8655f949fa5f.date = '1961'
SET release_8655f949fa5f.format = '12" Vinyl'
SET release_8655f949fa5f.discode = 'STEREO A-5'
SET release_8655f949fa5f.discogs = 'https://www.discogs.com/release/3188298'
SET release_8655f949fa5f.musicbrainz = 'http://musicbrainz.org/release/0bc26986-223f-447b-bef9-8655f949fa5f'
SET release_8655f949fa5f.source = 'musicbrainz.org'


MERGE (person_8f9b52869d74:Person{ uuid: '4704f86b-33b0-458a-9460-8f9b52869d74' }) 
SET person_8f9b52869d74.name = 'Oliver Nelson'
SET person_8f9b52869d74.gender = 'Male'
SET person_8f9b52869d74.disambiguation = 'saxophone, arranger, composer'
SET person_8f9b52869d74.country = 'US'
SET person_8f9b52869d74.allmusic = 'https://www.allmusic.com/artist/mn0000398615'
SET person_8f9b52869d74.discogs = 'https://www.discogs.com/artist/10095'
SET person_8f9b52869d74.imdb = 'https://www.imdb.com/name/nm0625648/'
SET person_8f9b52869d74.viaf = 'http://viaf.org/viaf/46947276'
SET person_8f9b52869d74.wikidata = 'https://www.wikidata.org/wiki/Q720687'
SET person_8f9b52869d74.databases = ['http://d-nb.info/gnd/134471628', 'http://id.loc.gov/authorities/names/n81033440', 'https://catalogue.bnf.fr/ark:/12148/cb138978988', 'http://snaccooperative.org/ark:/99166/w6ht2mtq', 'https://nla.gov.au/nla.party-844935', 'https://www.worldcat.org/identities/lccn-n81033440']
SET person_8f9b52869d74.musicbrainz = 'https://musicbrainz.org/artist/4704f86b-33b0-458a-9460-8f9b52869d74'
SET person_8f9b52869d74.isni_list = ['http://isni.org/isni/0000000081255777']
SET person_8f9b52869d74.source = 'musicbrainz.org'


MERGE (person_05d508e09a73:Person{ uuid: 'f0707f1d-55e1-46b6-8a9c-05d508e09a73' }) 
SET person_05d508e09a73.name = 'Rudy van Gelder'
SET person_05d508e09a73.gender = 'Male'
SET person_05d508e09a73.country = 'US'
SET person_05d508e09a73.allmusic = 'https://www.allmusic.com/artist/mn0000305301'
SET person_05d508e09a73.discogs = 'https://www.discogs.com/artist/252966'
SET person_05d508e09a73.viaf = 'http://viaf.org/viaf/33997197'
SET person_05d508e09a73.wikidata = 'https://www.wikidata.org/wiki/Q945681'
SET person_05d508e09a73.databases = ['http://d-nb.info/gnd/133648508', 'http://id.loc.gov/authorities/names/no00020144', 'https://rateyourmusic.com/artist/rudy_van_gelder', 'https://www.worldcat.org/identities/lccn-no00020144']
SET person_05d508e09a73.musicbrainz = 'https://musicbrainz.org/artist/f0707f1d-55e1-46b6-8a9c-05d508e09a73'
SET person_05d508e09a73.isni_list = ['http://isni.org/isni/0000000019691076']
SET person_05d508e09a73.source = 'musicbrainz.org'


MERGE (person_6c57b03a4e36:Person{ uuid: '8247a3f2-3a8e-4256-b322-6c57b03a4e36' }) 
SET person_6c57b03a4e36.name = 'Bill Evans'
SET person_6c57b03a4e36.gender = 'Male'
SET person_6c57b03a4e36.disambiguation = 'pianist'
SET person_6c57b03a4e36.country = 'US'
SET person_6c57b03a4e36.allmusic = 'https://www.allmusic.com/artist/mn0000764702'
SET person_6c57b03a4e36.bbc = 'https://www.bbc.co.uk/music/artists/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.discogs = 'https://www.discogs.com/artist/252310'
SET person_6c57b03a4e36.imdb = 'https://www.imdb.com/name/nm0262572/'
SET person_6c57b03a4e36.viaf = 'http://viaf.org/viaf/29717820'
SET person_6c57b03a4e36.wikidata = 'https://www.wikidata.org/wiki/Q208205'
SET person_6c57b03a4e36.databases = ['http://d-nb.info/gnd/137724519', 'http://id.loc.gov/authorities/names/n81147281', 'https://catalogue.bnf.fr/ark:/12148/cb13893736g', 'http://snaccooperative.org/ark:/99166/w6v411q5', 'https://rateyourmusic.com/artist/bill_evans', 'https://www.musik-sammler.de/artist/175764/', 'https://www.whosampled.com/Bill-Evans/', 'https://www.worldcat.org/identities/lccn-n81-147281']
SET person_6c57b03a4e36.musicbrainz = 'https://musicbrainz.org/artist/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.isni_list = ['http://isni.org/isni/0000000121261603']
SET person_6c57b03a4e36.source = 'musicbrainz.org'


MERGE (person_07467bdf0f71:Person{ uuid: 'badda5cf-f2c5-4dc2-b3d3-07467bdf0f71' }) 
SET person_07467bdf0f71.name = 'Eric Dolphy'
SET person_07467bdf0f71.gender = 'Male'
SET person_07467bdf0f71.country = 'US'
SET person_07467bdf0f71.allmusic = 'https://www.allmusic.com/artist/mn0000800100'
SET person_07467bdf0f71.bbc = 'https://www.bbc.co.uk/music/artists/badda5cf-f2c5-4dc2-b3d3-07467bdf0f71'
SET person_07467bdf0f71.discogs = 'https://www.discogs.com/artist/145272'
SET person_07467bdf0f71.imdb = 'https://www.imdb.com/name/nm0231238/'
SET person_07467bdf0f71.viaf = 'http://viaf.org/viaf/66651545'
SET person_07467bdf0f71.wikidata = 'https://www.wikidata.org/wiki/Q367508'
SET person_07467bdf0f71.databases = ['http://d-nb.info/gnd/118812866', 'http://id.loc.gov/authorities/names/n81035956', 'https://catalogue.bnf.fr/ark:/12148/cb13893337q', 'http://snaccooperative.org/ark:/99166/w6s18p3z', 'https://nla.gov.au/nla.party-910562', 'https://rateyourmusic.com/artist/eric_dolphy', 'https://www.worldcat.org/identities/lccn-n81035956']
SET person_07467bdf0f71.musicbrainz = 'https://musicbrainz.org/artist/badda5cf-f2c5-4dc2-b3d3-07467bdf0f71'
SET person_07467bdf0f71.isni_list = ['http://isni.org/isni/000000008146531X']
SET person_07467bdf0f71.source = 'musicbrainz.org'


MERGE (person_7de13124b970:Person{ uuid: 'b6ff4fd0-03ae-41a6-942e-7de13124b970' }) 
SET person_7de13124b970.name = 'Paul Chambers'
SET person_7de13124b970.gender = 'Male'
SET person_7de13124b970.disambiguation = 'US jazz bassist'
SET person_7de13124b970.country = 'US'
SET person_7de13124b970.allmusic = 'https://www.allmusic.com/artist/mn0000747984'
SET person_7de13124b970.discogs = 'https://www.discogs.com/artist/259778'
SET person_7de13124b970.imdb = 'https://www.imdb.com/name/nm2424848/'
SET person_7de13124b970.viaf = 'http://viaf.org/viaf/100313280'
SET person_7de13124b970.wikidata = 'https://www.wikidata.org/wiki/Q541659'
SET person_7de13124b970.databases = ['http://d-nb.info/gnd/134345797', 'http://id.loc.gov/authorities/names/n84148412', 'https://catalogue.bnf.fr/ark:/12148/cb138923573', 'http://snaccooperative.org/ark:/99166/w6ht3khn', 'https://www.worldcat.org/identities/lccn-n84148412']
SET person_7de13124b970.musicbrainz = 'https://musicbrainz.org/artist/b6ff4fd0-03ae-41a6-942e-7de13124b970'
SET person_7de13124b970.isni_list = ['http://isni.org/isni/0000000109289128']
SET person_7de13124b970.source = 'musicbrainz.org'


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


MERGE (person_d7529f22d78a:Person{ uuid: '82c19813-15ec-4b5f-a06a-d7529f22d78a' }) 
SET person_d7529f22d78a.name = 'Creed Taylor'
SET person_d7529f22d78a.gender = 'Male'
SET person_d7529f22d78a.country = 'US'
SET person_d7529f22d78a.allmusic = 'https://www.allmusic.com/artist/mn0000135180'
SET person_d7529f22d78a.discogs = 'https://www.discogs.com/artist/97480'
SET person_d7529f22d78a.viaf = 'http://viaf.org/viaf/268476531'
SET person_d7529f22d78a.wikidata = 'https://www.wikidata.org/wiki/Q1139476'
SET person_d7529f22d78a.databases = ['http://d-nb.info/gnd/1023707462', 'http://id.loc.gov/authorities/names/no98027837', 'https://catalogue.bnf.fr/ark:/12148/cb14643938g', 'https://rateyourmusic.com/artist/creed_taylor', 'https://www.worldcat.org/identities/lccn-no98027837']
SET person_d7529f22d78a.musicbrainz = 'https://musicbrainz.org/artist/82c19813-15ec-4b5f-a06a-d7529f22d78a'
SET person_d7529f22d78a.isni_list = ['http://isni.org/isni/0000000383306568']
SET person_d7529f22d78a.source = 'musicbrainz.org'


MERGE (person_769b6b099f0e:Person{ uuid: '67a136d2-2792-4634-a47f-769b6b099f0e' }) 
SET person_769b6b099f0e.name = 'George Barrow'
SET person_769b6b099f0e.gender = 'Male'
SET person_769b6b099f0e.country = 'US'
SET person_769b6b099f0e.allmusic = 'https://www.allmusic.com/artist/mn0000867794'
SET person_769b6b099f0e.discogs = 'https://www.discogs.com/artist/329251'
SET person_769b6b099f0e.viaf = 'http://viaf.org/viaf/199592'
SET person_769b6b099f0e.wikidata = 'https://www.wikidata.org/wiki/Q15428649'
SET person_769b6b099f0e.databases = ['http://d-nb.info/gnd/134321839', 'http://id.loc.gov/authorities/names/n91051278', 'https://catalogue.bnf.fr/ark:/12148/cb13931595w', 'https://www.worldcat.org/identities/lccn-n91051278']
SET person_769b6b099f0e.musicbrainz = 'https://musicbrainz.org/artist/67a136d2-2792-4634-a47f-769b6b099f0e'
SET person_769b6b099f0e.isni_list = ['http://isni.org/isni/000000005512997X']
SET person_769b6b099f0e.source = 'musicbrainz.org'


MERGE (person_e327e692bb5a:Person{ uuid: '59ae7a1a-f454-435b-8a5a-e327e692bb5a' }) 
SET person_e327e692bb5a.name = 'Freddie Hubbard'
SET person_e327e692bb5a.gender = 'Male'
SET person_e327e692bb5a.country = 'US'
SET person_e327e692bb5a.allmusic = 'https://www.allmusic.com/artist/mn0000798326'
SET person_e327e692bb5a.bbc = 'https://www.bbc.co.uk/music/artists/59ae7a1a-f454-435b-8a5a-e327e692bb5a'
SET person_e327e692bb5a.discogs = 'https://www.discogs.com/artist/55745'
SET person_e327e692bb5a.imdb = 'https://www.imdb.com/name/nm0399174/'
SET person_e327e692bb5a.viaf = 'http://viaf.org/viaf/64192087'
SET person_e327e692bb5a.wikidata = 'https://www.wikidata.org/wiki/Q346762'
SET person_e327e692bb5a.databases = ['http://d-nb.info/gnd/134411773', 'http://id.loc.gov/authorities/names/n83163529', 'https://catalogue.bnf.fr/ark:/12148/cb13895374d', 'https://rateyourmusic.com/artist/freddie_hubbard', 'https://www.worldcat.org/identities/lccn-n83163529']
SET person_e327e692bb5a.musicbrainz = 'https://musicbrainz.org/artist/59ae7a1a-f454-435b-8a5a-e327e692bb5a'
SET person_e327e692bb5a.isni_list = ['http://isni.org/isni/0000000114462300']
SET person_e327e692bb5a.source = 'musicbrainz.org'

// labels

MERGE (label_8fb76f3e6ca9:Label{ uuid: '93c3b044-2b4e-4239-a73b-8fb76f3e6ca9' })
SET label_8fb76f3e6ca9.name= 'impulse!'

// performances

MERGE (perf_b688d4e8b6b4:Performance{ uuid: '39279aed-3dc3-48a4-9e34-b688d4e8b6b4' })
SET perf_b688d4e8b6b4.name = 'Stolen Moments'
SET perf_b688d4e8b6b4.duration = '8:46'
SET perf_b688d4e8b6b4.begin_date = '1961-02-23'
SET perf_b688d4e8b6b4.end_date = '1961-02-23'
SET perf_b688d4e8b6b4.source = 'musicbrainz.org'


MERGE (perf_137aa9633ddc:Performance{ uuid: 'f70f12a9-4aeb-48da-9b3a-137aa9633ddc' })
SET perf_137aa9633ddc.name = 'Hoe-Down'
SET perf_137aa9633ddc.duration = '4:43'
SET perf_137aa9633ddc.begin_date = '1961-02-23'
SET perf_137aa9633ddc.end_date = '1961-02-23'
SET perf_137aa9633ddc.source = 'musicbrainz.org'


MERGE (perf_e2510923e518:Performance{ uuid: '2e4396ac-18c2-47cb-bd3f-e2510923e518' })
SET perf_e2510923e518.name = 'Cascades'
SET perf_e2510923e518.duration = '5:31'
SET perf_e2510923e518.begin_date = '1961-02-23'
SET perf_e2510923e518.end_date = '1961-02-23'
SET perf_e2510923e518.source = 'musicbrainz.org'


MERGE (perf_e12536c70a2a:Performance{ uuid: 'db1f958c-342c-4083-abde-e12536c70a2a' })
SET perf_e12536c70a2a.name = 'Yearnin’'
SET perf_e12536c70a2a.duration = '6:23'
SET perf_e12536c70a2a.begin_date = '1961-02-23'
SET perf_e12536c70a2a.end_date = '1961-02-23'
SET perf_e12536c70a2a.source = 'musicbrainz.org'


MERGE (perf_ff5622cdf9d5:Performance{ uuid: 'feadab52-73e6-4041-904e-ff5622cdf9d5' })
SET perf_ff5622cdf9d5.name = 'Butch and Butch'
SET perf_ff5622cdf9d5.duration = '4:36'
SET perf_ff5622cdf9d5.begin_date = '1961-02-23'
SET perf_ff5622cdf9d5.end_date = '1961-02-23'
SET perf_ff5622cdf9d5.source = 'musicbrainz.org'


MERGE (perf_dd0c00a6f8b6:Performance{ uuid: 'b18fb288-250b-4434-b6a0-dd0c00a6f8b6' })
SET perf_dd0c00a6f8b6.name = 'Teenie’s Blues'
SET perf_dd0c00a6f8b6.duration = '6:34'
SET perf_dd0c00a6f8b6.begin_date = '1961-02-23'
SET perf_dd0c00a6f8b6.end_date = '1961-02-23'
SET perf_dd0c00a6f8b6.source = 'musicbrainz.org'




// labels
MERGE (release_8655f949fa5f)-[:HAS_LABEL]->(label_8fb76f3e6ca9)


// tracks
MERGE (release_8655f949fa5f)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_b688d4e8b6b4)
MERGE (release_8655f949fa5f)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_137aa9633ddc)
MERGE (release_8655f949fa5f)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_e2510923e518)
MERGE (release_8655f949fa5f)-[:HAS_TRACK {name: 'B1', sequence: 4}]->(perf_e12536c70a2a)
MERGE (release_8655f949fa5f)-[:HAS_TRACK {name: 'B2', sequence: 5}]->(perf_ff5622cdf9d5)
MERGE (release_8655f949fa5f)-[:HAS_TRACK {name: 'B3', sequence: 6}]->(perf_dd0c00a6f8b6)

// works

MERGE (person_9dcfcb4c8c7a:Person{ uuid: '55a29cd8-0098-47f8-9650-9dcfcb4c8c7a' }) 
SET person_9dcfcb4c8c7a.name = 'Mark Murphy'
SET person_9dcfcb4c8c7a.gender = 'Male'
SET person_9dcfcb4c8c7a.disambiguation = 'US jazz singer'
SET person_9dcfcb4c8c7a.country = 'US'
SET person_9dcfcb4c8c7a.allmusic = 'https://www.allmusic.com/artist/mn0000244552'
SET person_9dcfcb4c8c7a.bbc = 'https://www.bbc.co.uk/music/artists/55a29cd8-0098-47f8-9650-9dcfcb4c8c7a'
SET person_9dcfcb4c8c7a.discogs = 'https://www.discogs.com/artist/15540'
SET person_9dcfcb4c8c7a.viaf = 'http://viaf.org/viaf/49422772'
SET person_9dcfcb4c8c7a.wikidata = 'https://www.wikidata.org/wiki/Q933550'
SET person_9dcfcb4c8c7a.databases = ['http://d-nb.info/gnd/134852850', 'http://id.loc.gov/authorities/names/n78052826', 'https://catalogue.bnf.fr/ark:/12148/cb14031965n', 'http://snaccooperative.org/ark:/99166/w6943s87', 'https://www.musik-sammler.de/artist/mark-murphy/', 'https://www.worldcat.org/identities/lccn-n78052826']
SET person_9dcfcb4c8c7a.musicbrainz = 'https://musicbrainz.org/artist/55a29cd8-0098-47f8-9650-9dcfcb4c8c7a'
SET person_9dcfcb4c8c7a.isni_list = ['http://isni.org/isni/0000000108000759']
SET person_9dcfcb4c8c7a.source = 'musicbrainz.org'


MERGE (work_17ac8b42863b:Work{ uuid: 'af0b6844-5a5a-3009-85de-17ac8b42863b' })
SET work_17ac8b42863b.name = 'Stolen Moments'
SET work_17ac8b42863b.iswc = 'T-071.220.599-6'
SET work_17ac8b42863b.type = 'Song'
SET work_17ac8b42863b.source = 'musicbrainz.org'


MERGE (work_67e64f0b5b36:Work{ uuid: '1d487f5e-0d23-4a17-ab67-67e64f0b5b36' })
SET work_67e64f0b5b36.name = 'Cascades'
SET work_67e64f0b5b36.allmusic = 'https://www.allmusic.com/song/mt0006610757'
SET work_67e64f0b5b36.musicbrainz = 'https://musicbrainz.org/work/1d487f5e-0d23-4a17-ab67-67e64f0b5b36'
SET work_67e64f0b5b36.source = 'musicbrainz.org'


MERGE (work_93ab006e9cc8:Work{ uuid: 'f677a4f1-31a3-475b-bb46-93ab006e9cc8' })
SET work_93ab006e9cc8.name = 'Teenie\\'s Blues'
SET work_93ab006e9cc8.allmusic = 'https://www.allmusic.com/song/mt0006662247'
SET work_93ab006e9cc8.musicbrainz = 'https://musicbrainz.org/work/f677a4f1-31a3-475b-bb46-93ab006e9cc8'
SET work_93ab006e9cc8.source = 'musicbrainz.org'


MERGE (work_2a7b39adcc91:Work{ uuid: 'e307cf10-5829-4ed0-b194-2a7b39adcc91' })
SET work_2a7b39adcc91.name = 'Hoe-Down'
SET work_2a7b39adcc91.allmusic = 'https://www.allmusic.com/song/mt0006669751'
SET work_2a7b39adcc91.musicbrainz = 'https://musicbrainz.org/work/e307cf10-5829-4ed0-b194-2a7b39adcc91'
SET work_2a7b39adcc91.source = 'musicbrainz.org'


MERGE (work_5f29a4fb7446:Work{ uuid: '0b7b019a-0005-49df-97e3-5f29a4fb7446' })
SET work_5f29a4fb7446.name = 'Butch and Butch'
SET work_5f29a4fb7446.type = 'Song'
SET work_5f29a4fb7446.source = 'musicbrainz.org'


MERGE (work_c267d83d036f:Work{ uuid: '85524663-3ea3-413c-9960-c267d83d036f' })
SET work_c267d83d036f.name = 'Yearnin\\''
SET work_c267d83d036f.allmusic = 'https://www.allmusic.com/song/mt0006737178'
SET work_c267d83d036f.musicbrainz = 'https://musicbrainz.org/work/85524663-3ea3-413c-9960-c267d83d036f'
SET work_c267d83d036f.source = 'musicbrainz.org'



// performances of
MERGE (perf_b688d4e8b6b4)-[:PERFORMANCE_OF]->(work_17ac8b42863b)
MERGE (perf_e2510923e518)-[:PERFORMANCE_OF]->(work_67e64f0b5b36)
MERGE (perf_dd0c00a6f8b6)-[:PERFORMANCE_OF]->(work_93ab006e9cc8)
MERGE (perf_137aa9633ddc)-[:PERFORMANCE_OF]->(work_2a7b39adcc91)
MERGE (perf_ff5622cdf9d5)-[:PERFORMANCE_OF]->(work_5f29a4fb7446)
MERGE (perf_e12536c70a2a)-[:PERFORMANCE_OF]->(work_c267d83d036f)


// composers
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_17ac8b42863b)
MERGE (person_9dcfcb4c8c7a)-[:WROTE_LYRICS]->(work_17ac8b42863b)
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_67e64f0b5b36)
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_93ab006e9cc8)
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_2a7b39adcc91)
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_5f29a4fb7446)
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_c267d83d036f)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.address = '445, Sylvan Avenue, Englewood Cliffs, Bergen County, New Jersey, 07632, United States'
SET place_569fa8b97644.lat = '40.87643740744882'
SET place_569fa8b97644.lng = '-73.95195468468218'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_b688d4e8b6b4)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-02-23', end_date: '1961-02-23' }]->(place_569fa8b97644)
MERGE (perf_137aa9633ddc)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-02-23', end_date: '1961-02-23' }]->(place_569fa8b97644)
MERGE (perf_e2510923e518)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-02-23', end_date: '1961-02-23' }]->(place_569fa8b97644)
MERGE (perf_e12536c70a2a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-02-23', end_date: '1961-02-23' }]->(place_569fa8b97644)
MERGE (perf_ff5622cdf9d5)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-02-23', end_date: '1961-02-23' }]->(place_569fa8b97644)
MERGE (perf_dd0c00a6f8b6)-[:HAS_PLACE { type: 'recorded at', begin_date: '1961-02-23', end_date: '1961-02-23' }]->(place_569fa8b97644)

MERGE (person_8f9b52869d74)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'tenor saxophone'] }]->(perf_b688d4e8b6b4)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b688d4e8b6b4)
MERGE (person_769b6b099f0e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_b688d4e8b6b4)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b688d4e8b6b4)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'flute'] }]->(perf_b688d4e8b6b4)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b688d4e8b6b4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b688d4e8b6b4)
MERGE (person_e327e692bb5a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_b688d4e8b6b4)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_b688d4e8b6b4)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_137aa9633ddc)
MERGE (person_769b6b099f0e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_137aa9633ddc)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_137aa9633ddc)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'flute'] }]->(perf_137aa9633ddc)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_137aa9633ddc)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_137aa9633ddc)
MERGE (person_e327e692bb5a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_137aa9633ddc)
MERGE (person_8f9b52869d74)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'tenor saxophone'] }]->(perf_137aa9633ddc)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_137aa9633ddc)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e2510923e518)
MERGE (person_769b6b099f0e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_e2510923e518)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e2510923e518)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'flute'] }]->(perf_e2510923e518)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e2510923e518)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e2510923e518)
MERGE (person_e327e692bb5a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e2510923e518)
MERGE (person_8f9b52869d74)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'tenor saxophone'] }]->(perf_e2510923e518)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e2510923e518)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e12536c70a2a)
MERGE (person_769b6b099f0e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_e12536c70a2a)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e12536c70a2a)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'flute'] }]->(perf_e12536c70a2a)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e12536c70a2a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e12536c70a2a)
MERGE (person_e327e692bb5a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e12536c70a2a)
MERGE (person_8f9b52869d74)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'tenor saxophone'] }]->(perf_e12536c70a2a)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_e12536c70a2a)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_ff5622cdf9d5)
MERGE (person_769b6b099f0e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_ff5622cdf9d5)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ff5622cdf9d5)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'flute'] }]->(perf_ff5622cdf9d5)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ff5622cdf9d5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ff5622cdf9d5)
MERGE (person_e327e692bb5a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_ff5622cdf9d5)
MERGE (person_8f9b52869d74)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'tenor saxophone'] }]->(perf_ff5622cdf9d5)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_ff5622cdf9d5)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_dd0c00a6f8b6)
MERGE (person_769b6b099f0e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['baritone saxophone'] }]->(perf_dd0c00a6f8b6)
MERGE (person_7de13124b970)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_dd0c00a6f8b6)
MERGE (person_07467bdf0f71)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'flute'] }]->(perf_dd0c00a6f8b6)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_dd0c00a6f8b6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_dd0c00a6f8b6)
MERGE (person_e327e692bb5a)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_dd0c00a6f8b6)
MERGE (person_8f9b52869d74)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['alto saxophone', 'tenor saxophone'] }]->(perf_dd0c00a6f8b6)
MERGE (person_d7529f22d78a)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_dd0c00a6f8b6)



"""
)