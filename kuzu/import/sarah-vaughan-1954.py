
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_53e655af426b:Release{ uuid: '6ebe3f1f-5804-495a-97ef-53e655af426b' })
SET release_53e655af426b.name = 'Sarah Vaughan'
SET release_53e655af426b.country = 'US'
SET release_53e655af426b.date = '1954-12-18'
SET release_53e655af426b.format = '12" Vinyl'
SET release_53e655af426b.discode = 'MG-36004'
SET release_53e655af426b.discogs = 'https://www.discogs.com/release/3050687'
SET release_53e655af426b.musicbrainz = 'http://musicbrainz.org/release/6ebe3f1f-5804-495a-97ef-53e655af426b'
SET release_53e655af426b.source = 'musicbrainz.org'


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


MERGE (person_8f221f658ef3:Person{ uuid: '7ec27748-5886-464d-8e65-8f221f658ef3' }) 
SET person_8f221f658ef3.name = 'Joe Benjamin'
SET person_8f221f658ef3.gender = 'Male'
SET person_8f221f658ef3.disambiguation = 'US jazz bassist'
SET person_8f221f658ef3.country = 'US'
SET person_8f221f658ef3.allmusic = 'https://www.allmusic.com/artist/mn0000140366'
SET person_8f221f658ef3.discogs = 'https://www.discogs.com/artist/254975'
SET person_8f221f658ef3.viaf = 'http://viaf.org/viaf/85790625'
SET person_8f221f658ef3.wikidata = 'https://www.wikidata.org/wiki/Q39016'
SET person_8f221f658ef3.databases = ['http://d-nb.info/gnd/134326059', 'http://id.loc.gov/authorities/names/n80144178', 'https://catalogue.bnf.fr/ark:/12148/cb138913497', 'https://www.worldcat.org/identities/lccn-n80144178']
SET person_8f221f658ef3.musicbrainz = 'https://musicbrainz.org/artist/7ec27748-5886-464d-8e65-8f221f658ef3'
SET person_8f221f658ef3.isni_list = ['http://isni.org/isni/0000000076900778']
SET person_8f221f658ef3.source = 'musicbrainz.org'


MERGE (person_022409fbce60:Person{ uuid: '04271c28-b9a7-4724-b7fd-022409fbce60' }) 
SET person_022409fbce60.name = 'Herbie Mann'
SET person_022409fbce60.gender = 'Male'
SET person_022409fbce60.country = 'US'
SET person_022409fbce60.allmusic = 'https://www.allmusic.com/artist/mn0000678408'
SET person_022409fbce60.discogs = 'https://www.discogs.com/artist/30721'
SET person_022409fbce60.imdb = 'https://www.imdb.com/name/nm0542781/'
SET person_022409fbce60.viaf = 'http://viaf.org/viaf/51875940'
SET person_022409fbce60.wikidata = 'https://www.wikidata.org/wiki/Q551912'
SET person_022409fbce60.databases = ['http://d-nb.info/gnd/128374268', 'http://id.loc.gov/authorities/names/n82019972', 'https://catalogue.bnf.fr/ark:/12148/cb138970413', 'http://snaccooperative.org/ark:/99166/w64b650v', 'https://rateyourmusic.com/artist/herbie_mann', 'https://www.worldcat.org/identities/lccn-n82019972']
SET person_022409fbce60.musicbrainz = 'https://musicbrainz.org/artist/04271c28-b9a7-4724-b7fd-022409fbce60'
SET person_022409fbce60.isni_list = ['http://isni.org/isni/0000000073599430']
SET person_022409fbce60.source = 'musicbrainz.org'


MERGE (person_c85fad20da55:Person{ uuid: '351d8bdf-33a1-45e2-8c04-c85fad20da55' }) 
SET person_c85fad20da55.name = 'Sarah Vaughan'
SET person_c85fad20da55.gender = 'Female'
SET person_c85fad20da55.country = 'US'
SET person_c85fad20da55.allmusic = 'https://www.allmusic.com/artist/mn0000204901'
SET person_c85fad20da55.bbc = 'https://www.bbc.co.uk/music/artists/351d8bdf-33a1-45e2-8c04-c85fad20da55'
SET person_c85fad20da55.discogs = 'https://www.discogs.com/artist/8284'
SET person_c85fad20da55.imdb = 'https://www.imdb.com/name/nm0891098/'
SET person_c85fad20da55.viaf = 'http://viaf.org/viaf/112758178'
SET person_c85fad20da55.wikidata = 'https://www.wikidata.org/wiki/Q229513'
SET person_c85fad20da55.databases = ['http://d-nb.info/gnd/119140047', 'http://id.loc.gov/authorities/names/n82019976', 'http://musicmoz.org/Bands_and_Artists/V/Vaughan,_Sarah/', 'https://catalogue.bnf.fr/ark:/12148/cb13900777n', 'http://snaccooperative.org/ark:/99166/w6cc1ksr', 'https://openlibrary.org/works/OL7220209A', 'https://rateyourmusic.com/artist/sarah_vaughan', 'https://www.musik-sammler.de/artist/sarah-vaughan/', 'https://www.worldcat.org/identities/lccn-n82019976']
SET person_c85fad20da55.musicbrainz = 'https://musicbrainz.org/artist/351d8bdf-33a1-45e2-8c04-c85fad20da55'
SET person_c85fad20da55.isni_list = ['http://isni.org/isni/0000000081802574']
SET person_c85fad20da55.source = 'musicbrainz.org'


MERGE (person_eab1269c7ba8:Person{ uuid: '2a291f34-73cb-40c5-b721-eab1269c7ba8' }) 
SET person_eab1269c7ba8.name = 'Clifford Brown'
SET person_eab1269c7ba8.gender = 'Male'
SET person_eab1269c7ba8.disambiguation = 'trumpet'
SET person_eab1269c7ba8.country = 'US'
SET person_eab1269c7ba8.allmusic = 'https://www.allmusic.com/artist/mn0000789775'
SET person_eab1269c7ba8.discogs = 'https://www.discogs.com/artist/259082'
SET person_eab1269c7ba8.viaf = 'http://viaf.org/viaf/19864699'
SET person_eab1269c7ba8.wikidata = 'https://www.wikidata.org/wiki/Q354490'
SET person_eab1269c7ba8.databases = ['http://d-nb.info/gnd/122167953', 'http://id.loc.gov/authorities/names/n82013477', 'https://catalogue.bnf.fr/ark:/12148/cb13891891d', 'http://snaccooperative.org/ark:/99166/w6rf6gjc', 'https://nla.gov.au/nla.party-910548', 'https://rateyourmusic.com/artist/clifford_brown', 'https://www.musik-sammler.de/artist/clifford-brown/', 'https://www.worldcat.org/identities/lccn-n82013477']
SET person_eab1269c7ba8.musicbrainz = 'https://musicbrainz.org/artist/2a291f34-73cb-40c5-b721-eab1269c7ba8'
SET person_eab1269c7ba8.isni_list = ['http://isni.org/isni/0000000121232204']
SET person_eab1269c7ba8.source = 'musicbrainz.org'


MERGE (person_07569e15f3fa:Person{ uuid: '15c1d7c1-32e3-4356-8f44-07569e15f3fa' }) 
SET person_07569e15f3fa.name = 'Ernie Wilkins'
SET person_07569e15f3fa.gender = 'Male'
SET person_07569e15f3fa.country = 'US'
SET person_07569e15f3fa.allmusic = 'https://www.allmusic.com/artist/mn0000205130'
SET person_07569e15f3fa.discogs = 'https://www.discogs.com/artist/282003'
SET person_07569e15f3fa.viaf = 'http://viaf.org/viaf/100232872'
SET person_07569e15f3fa.wikidata = 'https://www.wikidata.org/wiki/Q326634'
SET person_07569e15f3fa.databases = ['http://d-nb.info/gnd/134580621', 'http://id.loc.gov/authorities/names/n88629938', 'https://catalogue.bnf.fr/ark:/12148/cb13901164w', 'http://snaccooperative.org/ark:/99166/w6x37289', 'https://www.worldcat.org/identities/lccn-n88629938']
SET person_07569e15f3fa.musicbrainz = 'https://musicbrainz.org/artist/15c1d7c1-32e3-4356-8f44-07569e15f3fa'
SET person_07569e15f3fa.isni_list = ['http://isni.org/isni/0000000116917495']
SET person_07569e15f3fa.source = 'musicbrainz.org'


MERGE (person_beee70c5e271:Person{ uuid: 'd0fd2d09-eda7-45e2-b7da-beee70c5e271' }) 
SET person_beee70c5e271.name = 'Jimmy Jones'
SET person_beee70c5e271.gender = 'Male'
SET person_beee70c5e271.disambiguation = 'jazz pianist, active years 1936-1975'
SET person_beee70c5e271.country = 'US'
SET person_beee70c5e271.discogs = 'https://www.discogs.com/artist/307373'
SET person_beee70c5e271.viaf = 'http://viaf.org/viaf/100229577'
SET person_beee70c5e271.wikidata = 'https://www.wikidata.org/wiki/Q122966'
SET person_beee70c5e271.wikipedia = 'https://en.wikipedia.org/wiki/Jimmy_Jones_(pianist)'
SET person_beee70c5e271.databases = ['http://d-nb.info/gnd/135370728', 'http://id.loc.gov/authorities/names/n91084904', 'https://catalogue.bnf.fr/ark:/12148/cb13895730w', 'http://snaccooperative.org/ark:/99166/w60k29ks', 'https://www.worldcat.org/identities/lccn-n91084904']
SET person_beee70c5e271.musicbrainz = 'https://musicbrainz.org/artist/d0fd2d09-eda7-45e2-b7da-beee70c5e271'
SET person_beee70c5e271.isni_list = ['http://isni.org/isni/0000000115574603']
SET person_beee70c5e271.source = 'musicbrainz.org'


MERGE (person_209e4eaf1b70:Person{ uuid: 'daac94c4-689f-462f-bbfd-209e4eaf1b70' }) 
SET person_209e4eaf1b70.name = 'Paul Quinichette'
SET person_209e4eaf1b70.gender = 'Male'
SET person_209e4eaf1b70.country = 'US'
SET person_209e4eaf1b70.allmusic = 'https://www.allmusic.com/artist/mn0000028015'
SET person_209e4eaf1b70.discogs = 'https://www.discogs.com/artist/311992'
SET person_209e4eaf1b70.viaf = 'http://viaf.org/viaf/76501255'
SET person_209e4eaf1b70.wikidata = 'https://www.wikidata.org/wiki/Q353750'
SET person_209e4eaf1b70.wikipedia = 'https://en.wikipedia.org/wiki/Paul_Quinichette'
SET person_209e4eaf1b70.databases = ['http://d-nb.info/gnd/134490304', 'http://id.loc.gov/authorities/names/n78031054', 'https://catalogue.bnf.fr/ark:/12148/cb138987538', 'https://www.worldcat.org/identities/lccn-n78031054']
SET person_209e4eaf1b70.musicbrainz = 'https://musicbrainz.org/artist/daac94c4-689f-462f-bbfd-209e4eaf1b70'
SET person_209e4eaf1b70.isni_list = ['http://isni.org/isni/0000000055151886']
SET person_209e4eaf1b70.source = 'musicbrainz.org'


MERGE (person_ff9017878cdd:Person{ uuid: 'b59843a1-bb97-45f0-84b9-ff9017878cdd' }) 
SET person_ff9017878cdd.name = 'Richard Davis'
SET person_ff9017878cdd.gender = 'Male'
SET person_ff9017878cdd.disambiguation = 'American jazz bassist'
SET person_ff9017878cdd.country = 'US'
SET person_ff9017878cdd.allmusic = 'https://www.allmusic.com/artist/mn0000851653'
SET person_ff9017878cdd.discogs = 'https://www.discogs.com/artist/263441'
SET person_ff9017878cdd.viaf = 'http://viaf.org/viaf/120739764'
SET person_ff9017878cdd.wikidata = 'https://www.wikidata.org/wiki/Q716851'
SET person_ff9017878cdd.databases = ['http://d-nb.info/gnd/134355792', 'http://id.loc.gov/authorities/names/n81015291', 'https://catalogue.bnf.fr/ark:/12148/cb13893033h', 'http://snaccooperative.org/ark:/99166/w66d6dj7', 'https://rateyourmusic.com/artist/richard_davis', 'https://www.worldcat.org/identities/lccn-n81015291']
SET person_ff9017878cdd.musicbrainz = 'https://musicbrainz.org/artist/b59843a1-bb97-45f0-84b9-ff9017878cdd'
SET person_ff9017878cdd.isni_list = ['http://isni.org/isni/0000000079564079']
SET person_ff9017878cdd.source = 'musicbrainz.org'

// labels

MERGE (label_42366b3be8c9:Label{ uuid: 'e023c53a-7e9b-4f7d-99ff-42366b3be8c9' })
SET label_42366b3be8c9.name= 'EmArcy'

// performances

MERGE (perf_7ecdd90ce2e1:Performance{ uuid: 'f5ab671e-0dcc-4ef8-99fe-7ecdd90ce2e1' })
SET perf_7ecdd90ce2e1.name = 'Lullaby of Birdland'
SET perf_7ecdd90ce2e1.duration = '3:59'
SET perf_7ecdd90ce2e1.source = 'musicbrainz.org'


MERGE (perf_d392d8d26a10:Performance{ uuid: '98db247c-5376-4c6c-90e9-d392d8d26a10' })
SET perf_d392d8d26a10.name = 'April in Paris'
SET perf_d392d8d26a10.duration = '6:19'
SET perf_d392d8d26a10.source = 'musicbrainz.org'


MERGE (perf_0d4ab9d8818b:Performance{ uuid: 'c3436e9b-a833-4aea-8670-0d4ab9d8818b' })
SET perf_0d4ab9d8818b.name = 'He’s My Guy'
SET perf_0d4ab9d8818b.duration = '4:13'
SET perf_0d4ab9d8818b.begin_date = '1954-12-18'
SET perf_0d4ab9d8818b.end_date = '1954-12-18'
SET perf_0d4ab9d8818b.source = 'musicbrainz.org'


MERGE (perf_974ef6842862:Performance{ uuid: 'd88ee65b-8cc2-4b59-8d38-974ef6842862' })
SET perf_974ef6842862.name = 'Jim'
SET perf_974ef6842862.duration = '5:52'
SET perf_974ef6842862.begin_date = '1954-12-18'
SET perf_974ef6842862.end_date = '1954-12-18'
SET perf_974ef6842862.source = 'musicbrainz.org'


MERGE (perf_8b1b8d05c196:Performance{ uuid: 'cb73e53b-9a09-425c-9345-8b1b8d05c196' })
SET perf_8b1b8d05c196.name = 'You’re Not the Kind'
SET perf_8b1b8d05c196.duration = '4:44'
SET perf_8b1b8d05c196.begin_date = '1954-12-16'
SET perf_8b1b8d05c196.end_date = '1954-12-16'
SET perf_8b1b8d05c196.source = 'musicbrainz.org'


MERGE (perf_5b9d48ddcb6b:Performance{ uuid: '9944f81a-8c84-4af5-91ab-5b9d48ddcb6b' })
SET perf_5b9d48ddcb6b.name = 'Embraceable You'
SET perf_5b9d48ddcb6b.duration = '4:50'
SET perf_5b9d48ddcb6b.begin_date = '1954-12-18'
SET perf_5b9d48ddcb6b.end_date = '1954-12-18'
SET perf_5b9d48ddcb6b.source = 'musicbrainz.org'


MERGE (perf_8849bcd91686:Performance{ uuid: 'a5ba62c5-fc52-444f-b736-8849bcd91686' })
SET perf_8849bcd91686.name = 'I’m Glad There Is You'
SET perf_8849bcd91686.duration = '5:10'
SET perf_8849bcd91686.begin_date = '1954-12-16'
SET perf_8849bcd91686.end_date = '1954-12-16'
SET perf_8849bcd91686.source = 'musicbrainz.org'


MERGE (perf_1fa9437cea92:Performance{ uuid: 'd21861ba-5e45-4f93-82e5-1fa9437cea92' })
SET perf_1fa9437cea92.name = 'September Song'
SET perf_1fa9437cea92.duration = '5:46'
SET perf_1fa9437cea92.begin_date = '1954-12-16'
SET perf_1fa9437cea92.end_date = '1954-12-16'
SET perf_1fa9437cea92.source = 'musicbrainz.org'


MERGE (perf_91d9f082645e:Performance{ uuid: '3de34098-bf01-40ff-b70a-91d9f082645e' })
SET perf_91d9f082645e.name = 'It’s Crazy'
SET perf_91d9f082645e.duration = '4:55'
SET perf_91d9f082645e.begin_date = '1954-12-18'
SET perf_91d9f082645e.end_date = '1954-12-18'
SET perf_91d9f082645e.source = 'musicbrainz.org'




// labels
MERGE (release_53e655af426b)-[:HAS_LABEL]->(label_42366b3be8c9)


// tracks
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_7ecdd90ce2e1)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_d392d8d26a10)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_0d4ab9d8818b)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_974ef6842862)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'B1', sequence: 5}]->(perf_8b1b8d05c196)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'B2', sequence: 6}]->(perf_5b9d48ddcb6b)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'B3', sequence: 7}]->(perf_8849bcd91686)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'B4', sequence: 8}]->(perf_1fa9437cea92)
MERGE (release_53e655af426b)-[:HAS_TRACK {name: 'B5', sequence: 9}]->(perf_91d9f082645e)

// works

MERGE (person_640857a22571:Person{ uuid: '87031b72-fd24-44be-a70a-640857a22571' }) 
SET person_640857a22571.name = 'Milton Samuels'
SET person_640857a22571.gender = 'Male'
SET person_640857a22571.country = 'US'
SET person_640857a22571.discogs = 'https://www.discogs.com/artist/1367881'
SET person_640857a22571.wikidata = 'https://www.wikidata.org/wiki/Q110985248'
SET person_640857a22571.musicbrainz = 'https://musicbrainz.org/artist/87031b72-fd24-44be-a70a-640857a22571'
SET person_640857a22571.source = 'musicbrainz.org'


MERGE (person_6a07564b5394:Person{ uuid: '794e6b10-e8e2-4fb1-9013-6a07564b5394' }) 
SET person_6a07564b5394.name = 'Vernon Duke'
SET person_6a07564b5394.gender = 'Male'
SET person_6a07564b5394.country = 'US'
SET person_6a07564b5394.allmusic = 'https://www.allmusic.com/artist/mn0000095859'
SET person_6a07564b5394.discogs = 'https://www.discogs.com/artist/614342'
SET person_6a07564b5394.imdb = 'https://www.imdb.com/name/nm0241216/'
SET person_6a07564b5394.viaf = 'http://viaf.org/viaf/51891012'
SET person_6a07564b5394.wikidata = 'https://www.wikidata.org/wiki/Q519693'
SET person_6a07564b5394.databases = ['http://d-nb.info/gnd/10382247X', 'http://id.loc.gov/authorities/names/n80125365', 'https://catalogue.bnf.fr/ark:/12148/cb14044916c', 'https://ibdb.com/person.php?id=8943', 'http://snaccooperative.org/ark:/99166/w6280g8k', 'https://nla.gov.au/nla.party-1525253', 'https://openlibrary.org/works/OL2274232A', 'https://rateyourmusic.com/artist/vernon_duke', 'https://www.worldcat.org/identities/lccn-n80125365/']
SET person_6a07564b5394.musicbrainz = 'https://musicbrainz.org/artist/794e6b10-e8e2-4fb1-9013-6a07564b5394'
SET person_6a07564b5394.isni_list = ['http://isni.org/isni/0000000081307426']
SET person_6a07564b5394.source = 'musicbrainz.org'


MERGE (person_322e34240ffc:Person{ uuid: '509086c2-9cc8-4e77-89e9-322e34240ffc' }) 
SET person_322e34240ffc.name = 'Ira Gershwin'
SET person_322e34240ffc.gender = 'Male'
SET person_322e34240ffc.country = 'US'
SET person_322e34240ffc.allmusic = 'https://www.allmusic.com/artist/mn0000200301'
SET person_322e34240ffc.discogs = 'https://www.discogs.com/artist/264105'
SET person_322e34240ffc.imdb = 'https://www.imdb.com/name/nm0314857/'
SET person_322e34240ffc.viaf = 'http://viaf.org/viaf/39519496'
SET person_322e34240ffc.wikidata = 'https://www.wikidata.org/wiki/Q61059'
SET person_322e34240ffc.databases = ['http://d-nb.info/gnd/119500027', 'http://id.loc.gov/authorities/names/n50076010', 'https://catalogue.bnf.fr/ark:/12148/cb13194929s', 'https://ibdb.com/person.php?id=6435', 'http://snaccooperative.org/ark:/99166/w60w94tm', 'https://nla.gov.au/nla.party-965252', 'https://openlibrary.org/works/OL233692A', 'https://rateyourmusic.com/artist/ira_gershwin', 'https://www.worldcat.org/identities/lccn-n50076010/']
SET person_322e34240ffc.musicbrainz = 'https://musicbrainz.org/artist/509086c2-9cc8-4e77-89e9-322e34240ffc'
SET person_322e34240ffc.isni_list = ['http://isni.org/isni/0000000108901469']
SET person_322e34240ffc.source = 'musicbrainz.org'


MERGE (person_1226521487b7:Person{ uuid: '2344f604-7b3e-4e45-a770-1226521487b7' }) 
SET person_1226521487b7.name = 'Will Hudson'
SET person_1226521487b7.gender = 'Male'
SET person_1226521487b7.country = 'US'
SET person_1226521487b7.allmusic = 'https://www.allmusic.com/artist/mn0000689853'
SET person_1226521487b7.discogs = 'https://www.discogs.com/artist/778413'
SET person_1226521487b7.imdb = 'https://www.imdb.com/name/nm1289210/'
SET person_1226521487b7.databases = ['https://rateyourmusic.com/artist/will_hudson']
SET person_1226521487b7.musicbrainz = 'https://musicbrainz.org/artist/2344f604-7b3e-4e45-a770-1226521487b7'
SET person_1226521487b7.isni_list = ['http://isni.org/isni/0000000116521271']
SET person_1226521487b7.source = 'musicbrainz.org'


MERGE (person_560575963ee1:Person{ uuid: '7dc2579e-4619-4087-ac78-560575963ee1' }) 
SET person_560575963ee1.name = 'B. Y. Forster'
SET person_560575963ee1.gender = 'Male'
SET person_560575963ee1.disambiguation = 'pseudonym of George David Weiss'
SET person_560575963ee1.country = 'US'
SET person_560575963ee1.source = 'musicbrainz.org'


MERGE (person_a80827ca20da:Person{ uuid: 'c803b5aa-af2f-406a-9e40-a80827ca20da' }) 
SET person_a80827ca20da.name = 'Paul Madeira'
SET person_a80827ca20da.gender = 'Male'
SET person_a80827ca20da.disambiguation = 'Paul Madeira Mertz'
SET person_a80827ca20da.country = 'US'
SET person_a80827ca20da.allmusic = 'https://www.allmusic.com/artist/mn0001009269'
SET person_a80827ca20da.discogs = 'https://www.discogs.com/artist/299283'
SET person_a80827ca20da.viaf = 'http://viaf.org/viaf/11896635'
SET person_a80827ca20da.wikidata = 'https://www.wikidata.org/wiki/Q96905202'
SET person_a80827ca20da.musicbrainz = 'https://musicbrainz.org/artist/c803b5aa-af2f-406a-9e40-a80827ca20da'
SET person_a80827ca20da.source = 'musicbrainz.org'


MERGE (person_e9da3eef0186:Person{ uuid: 'f8688b5e-874d-4dee-8366-e9da3eef0186' }) 
SET person_e9da3eef0186.name = 'Maxwell Anderson'
SET person_e9da3eef0186.gender = 'Male'
SET person_e9da3eef0186.country = 'US'
SET person_e9da3eef0186.allmusic = 'https://www.allmusic.com/artist/mn0001320781'
SET person_e9da3eef0186.discogs = 'https://www.discogs.com/artist/226814'
SET person_e9da3eef0186.imdb = 'https://www.imdb.com/name/nm0027173/'
SET person_e9da3eef0186.viaf = 'http://viaf.org/viaf/24683691'
SET person_e9da3eef0186.wikidata = 'https://www.wikidata.org/wiki/Q432919'
SET person_e9da3eef0186.databases = ['http://d-nb.info/gnd/118645145', 'http://id.loc.gov/authorities/names/n50021938', 'https://catalogue.bnf.fr/ark:/12148/cb12383728n', 'http://snaccooperative.org/ark:/99166/w6sf2wng', 'https://nla.gov.au/nla.party-787146', 'https://openlibrary.org/works/OL587394A', 'https://rateyourmusic.com/artist/maxwell_anderson', 'https://www.ibdb.com/person.php?id=7672', 'https://www.worldcat.org/identities/lccn-n50021938/', 'http://www.lortel.org/Archives/CreditableEntity/1547']
SET person_e9da3eef0186.musicbrainz = 'https://musicbrainz.org/artist/f8688b5e-874d-4dee-8366-e9da3eef0186'
SET person_e9da3eef0186.isni_list = ['http://isni.org/isni/0000000108798035']
SET person_e9da3eef0186.source = 'musicbrainz.org'


MERGE (person_434e2b3faba6:Person{ uuid: '3df7b4b5-d6cd-4372-b7d5-434e2b3faba6' }) 
SET person_434e2b3faba6.name = 'Caesar Petrillo'
SET person_434e2b3faba6.gender = 'Male'
SET person_434e2b3faba6.country = 'US'
SET person_434e2b3faba6.discogs = 'https://www.discogs.com/artist/826062'
SET person_434e2b3faba6.viaf = 'http://viaf.org/viaf/75854146'
SET person_434e2b3faba6.wikidata = 'https://www.wikidata.org/wiki/Q6141202'
SET person_434e2b3faba6.databases = ['http://d-nb.info/gnd/138739536', 'http://id.loc.gov/authorities/names/no00010229', 'http://snaccooperative.org/ark:/99166/w65b03bj', 'https://www.worldcat.org/identities/lccn-no00010229/']
SET person_434e2b3faba6.musicbrainz = 'https://musicbrainz.org/artist/3df7b4b5-d6cd-4372-b7d5-434e2b3faba6'
SET person_434e2b3faba6.isni_list = ['http://isni.org/isni/0000000063327474']
SET person_434e2b3faba6.source = 'musicbrainz.org'


MERGE (person_c5d6969cef65:Person{ uuid: '96ae8237-7675-4d69-b357-c5d6969cef65' }) 
SET person_c5d6969cef65.name = 'Don Raye'
SET person_c5d6969cef65.gender = 'Male'
SET person_c5d6969cef65.country = 'US'
SET person_c5d6969cef65.allmusic = 'https://www.allmusic.com/artist/mn0000190492'
SET person_c5d6969cef65.allmusic = 'https://www.allmusic.com/artist/mn0002837005'
SET person_c5d6969cef65.discogs = 'https://www.discogs.com/artist/631367'
SET person_c5d6969cef65.imdb = 'https://www.imdb.com/name/nm0713098/'
SET person_c5d6969cef65.viaf = 'http://viaf.org/viaf/278124'
SET person_c5d6969cef65.wikidata = 'https://www.wikidata.org/wiki/Q220028'
SET person_c5d6969cef65.databases = ['http://d-nb.info/gnd/134949579', 'http://id.loc.gov/authorities/names/n89614294', 'https://catalogue.bnf.fr/ark:/12148/cb14838703m', 'http://snaccooperative.org/ark:/99166/w6z33nxn', 'https://rateyourmusic.com/artist/don_raye', 'https://www.ibdb.com/person.php?id=83530', 'https://www.worldcat.org/identities/lccn-n89614294/']
SET person_c5d6969cef65.musicbrainz = 'https://musicbrainz.org/artist/96ae8237-7675-4d69-b357-c5d6969cef65'
SET person_c5d6969cef65.isni_list = ['http://isni.org/isni/0000000120369153']
SET person_c5d6969cef65.source = 'musicbrainz.org'


MERGE (person_de901f0101e9:Person{ uuid: '3b6956ed-37d2-4436-bf09-de901f0101e9' }) 
SET person_de901f0101e9.name = 'Jimmy Dorsey'
SET person_de901f0101e9.gender = 'Male'
SET person_de901f0101e9.country = 'US'
SET person_de901f0101e9.allmusic = 'https://www.allmusic.com/artist/mn0000296745'
SET person_de901f0101e9.discogs = 'https://www.discogs.com/artist/299282'
SET person_de901f0101e9.imdb = 'https://www.imdb.com/name/nm0234153/'
SET person_de901f0101e9.viaf = 'http://viaf.org/viaf/22327067'
SET person_de901f0101e9.wikidata = 'https://www.wikidata.org/wiki/Q560716'
SET person_de901f0101e9.databases = ['http://d-nb.info/gnd/120542617', 'http://id.loc.gov/authorities/names/n82077171', 'https://catalogue.bnf.fr/ark:/12148/cb13893383w', 'https://ibdb.com/person.php?id=412036', 'http://snaccooperative.org/ark:/99166/w63x8q17', 'https://nla.gov.au/nla.party-1095409', 'https://www.worldcat.org/identities/lccn-n82077171']
SET person_de901f0101e9.musicbrainz = 'https://musicbrainz.org/artist/3b6956ed-37d2-4436-bf09-de901f0101e9'
SET person_de901f0101e9.isni_list = ['http://isni.org/isni/0000000063035738']
SET person_de901f0101e9.source = 'musicbrainz.org'


MERGE (person_cae1b1c6362f:Person{ uuid: '9a775c6e-9346-4b16-a611-cae1b1c6362f' }) 
SET person_cae1b1c6362f.name = 'Dorothy Fields'
SET person_cae1b1c6362f.gender = 'Female'
SET person_cae1b1c6362f.disambiguation = 'US Tin Pan Alley librettist and lyricist'
SET person_cae1b1c6362f.country = 'US'
SET person_cae1b1c6362f.discogs = 'https://www.discogs.com/artist/301992'
SET person_cae1b1c6362f.imdb = 'https://www.imdb.com/name/nm0276227/'
SET person_cae1b1c6362f.viaf = 'http://viaf.org/viaf/59268144'
SET person_cae1b1c6362f.wikidata = 'https://www.wikidata.org/wiki/Q435241'
SET person_cae1b1c6362f.databases = ['http://d-nb.info/gnd/120891735', 'http://id.loc.gov/authorities/names/n81023046', 'https://catalogue.bnf.fr/ark:/12148/cb137951840', 'http://snaccooperative.org/ark:/99166/w6hf8jtc', 'https://nla.gov.au/nla.party-956142', 'https://openlibrary.org/works/OL2263030A', 'https://www.ibdb.com/person.php?id=5113', 'https://www.worldcat.org/identities/lccn-n81023046/']
SET person_cae1b1c6362f.musicbrainz = 'https://musicbrainz.org/artist/9a775c6e-9346-4b16-a611-cae1b1c6362f'
SET person_cae1b1c6362f.isni_list = ['http://isni.org/isni/0000000081386224']
SET person_cae1b1c6362f.source = 'musicbrainz.org'


MERGE (person_4f7500861060:Person{ uuid: '0e738f68-783c-4a6a-80ae-4f7500861060' }) 
SET person_4f7500861060.name = 'Kurt Weill'
SET person_4f7500861060.gender = 'Male'
SET person_4f7500861060.disambiguation = 'composer'
SET person_4f7500861060.country = 'DE'
SET person_4f7500861060.allmusic = 'https://www.allmusic.com/artist/mn0000683446'
SET person_4f7500861060.discogs = 'https://www.discogs.com/artist/407111'
SET person_4f7500861060.imdb = 'https://www.imdb.com/name/nm0918044/'
SET person_4f7500861060.viaf = 'http://viaf.org/viaf/76501825'
SET person_4f7500861060.wikidata = 'https://www.wikidata.org/wiki/Q55004'
SET person_4f7500861060.databases = ['http://d-nb.info/gnd/118630202', 'http://id.loc.gov/authorities/names/n50022735', 'https://catalogue.bnf.fr/ark:/12148/cb13901071w', 'https://ibdb.com/person.php?id=7112', 'http://snaccooperative.org/ark:/99166/w6rr1x51', 'https://nla.gov.au/nla.party-1009171', 'https://openlibrary.org/works/OL452842A', 'https://rateyourmusic.com/artist/kurt_weill', 'https://www.worldcat.org/identities/lccn-n50022735']
SET person_4f7500861060.musicbrainz = 'https://musicbrainz.org/artist/0e738f68-783c-4a6a-80ae-4f7500861060'
SET person_4f7500861060.isni_list = ['http://isni.org/isni/0000000114753562']
SET person_4f7500861060.source = 'musicbrainz.org'


MERGE (person_b693a808a158:Person{ uuid: '65744963-191a-44ef-a3c7-b693a808a158' }) 
SET person_b693a808a158.name = 'George Gershwin'
SET person_b693a808a158.gender = 'Male'
SET person_b693a808a158.disambiguation = 'composer'
SET person_b693a808a158.country = 'US'
SET person_b693a808a158.allmusic = 'https://www.allmusic.com/artist/mn0000197918'
SET person_b693a808a158.bbc = 'https://www.bbc.co.uk/music/artists/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.discogs = 'https://www.discogs.com/artist/261293'
SET person_b693a808a158.imdb = 'https://www.imdb.com/name/nm0006097/'
SET person_b693a808a158.viaf = 'http://viaf.org/viaf/61554329'
SET person_b693a808a158.wikidata = 'https://www.wikidata.org/wiki/Q123829'
SET person_b693a808a158.databases = ['http://d-nb.info/gnd/118639226', 'http://id.loc.gov/authorities/names/n79077265', 'https://catalogue.bnf.fr/ark:/12148/cb119493251', 'https://ibdb.com/person.php?id=5813', 'http://snaccooperative.org/ark:/99166/w6x065dx', 'https://nla.gov.au/nla.party-832382', 'https://openlibrary.org/works/OL67761A', 'http://soundtrackcollector.com/composer/33/', 'https://rateyourmusic.com/artist/george_gershwin', 'https://www.worldcat.org/identities/lccn-n79077265']
SET person_b693a808a158.musicbrainz = 'https://musicbrainz.org/artist/65744963-191a-44ef-a3c7-b693a808a158'
SET person_b693a808a158.isni_list = ['http://isni.org/isni/0000000121355968']
SET person_b693a808a158.source = 'musicbrainz.org'


MERGE (person_df9db18b28e9:Person{ uuid: 'ef83af4c-4da9-47d1-b9bd-df9db18b28e9' }) 
SET person_df9db18b28e9.name = 'George Shearing'
SET person_df9db18b28e9.gender = 'Male'
SET person_df9db18b28e9.country = 'GB'
SET person_df9db18b28e9.allmusic = 'https://www.allmusic.com/artist/mn0000642664'
SET person_df9db18b28e9.discogs = 'https://www.discogs.com/artist/59407'
SET person_df9db18b28e9.imdb = 'https://www.imdb.com/name/nm0790471/'
SET person_df9db18b28e9.viaf = 'http://viaf.org/viaf/37103429'
SET person_df9db18b28e9.wikidata = 'https://www.wikidata.org/wiki/Q349346'
SET person_df9db18b28e9.databases = ['http://d-nb.info/gnd/129402613', 'http://id.loc.gov/authorities/names/n81015302', 'https://catalogue.bnf.fr/ark:/12148/cb13899721w', 'http://snaccooperative.org/ark:/99166/w6j39n8p', 'https://www.worldcat.org/identities/lccn-n81015302']
SET person_df9db18b28e9.musicbrainz = 'https://musicbrainz.org/artist/ef83af4c-4da9-47d1-b9bd-df9db18b28e9'
SET person_df9db18b28e9.isni_list = ['http://isni.org/isni/0000000120239981']
SET person_df9db18b28e9.source = 'musicbrainz.org'


MERGE (person_1ef2fece51ce:Person{ uuid: '2a2bf494-ac80-4ac9-901f-1ef2fece51ce' }) 
SET person_1ef2fece51ce.name = 'Irving Mills'
SET person_1ef2fece51ce.gender = 'Male'
SET person_1ef2fece51ce.country = 'US'
SET person_1ef2fece51ce.allmusic = 'https://www.allmusic.com/artist/mn0000084993'
SET person_1ef2fece51ce.discogs = 'https://www.discogs.com/artist/307446'
SET person_1ef2fece51ce.imdb = 'https://www.imdb.com/name/nm0590030/'
SET person_1ef2fece51ce.viaf = 'http://viaf.org/viaf/76500944'
SET person_1ef2fece51ce.wikidata = 'https://www.wikidata.org/wiki/Q1292110'
SET person_1ef2fece51ce.databases = ['http://d-nb.info/gnd/135465664', 'http://id.loc.gov/authorities/names/n88621778', 'https://catalogue.bnf.fr/ark:/12148/cb13897535j', 'https://ibdb.com/person.php?id=83868', 'http://snaccooperative.org/ark:/99166/w6f50280', 'https://nla.gov.au/nla.party-1528202', 'https://rateyourmusic.com/artist/irving_mills', 'https://www.worldcat.org/identities/lccn-n88621778/']
SET person_1ef2fece51ce.musicbrainz = 'https://musicbrainz.org/artist/2a2bf494-ac80-4ac9-901f-1ef2fece51ce'
SET person_1ef2fece51ce.isni_list = ['http://isni.org/isni/0000000081569522']
SET person_1ef2fece51ce.source = 'musicbrainz.org'


MERGE (person_7593a336e68d:Person{ uuid: '4d8d6af8-827e-4947-b04b-7593a336e68d' }) 
SET person_7593a336e68d.name = 'Gene de Paul'
SET person_7593a336e68d.gender = 'Male'
SET person_7593a336e68d.country = 'US'
SET person_7593a336e68d.allmusic = 'https://www.allmusic.com/artist/mn0000067671'
SET person_7593a336e68d.discogs = 'https://www.discogs.com/artist/631368'
SET person_7593a336e68d.imdb = 'https://www.imdb.com/name/nm0210877/'
SET person_7593a336e68d.viaf = 'http://viaf.org/viaf/121299490'
SET person_7593a336e68d.wikidata = 'https://www.wikidata.org/wiki/Q731258'
SET person_7593a336e68d.databases = ['http://d-nb.info/gnd/103932445', 'http://id.loc.gov/authorities/names/nr93016871', 'https://catalogue.bnf.fr/ark:/12148/cb139430282', 'http://snaccooperative.org/ark:/99166/w6v16g3b', 'https://www.ibdb.com/person.php?id=11580', 'https://www.worldcat.org/identities/lccn-nr93016871/']
SET person_7593a336e68d.musicbrainz = 'https://musicbrainz.org/artist/4d8d6af8-827e-4947-b04b-7593a336e68d'
SET person_7593a336e68d.isni_list = ['http://isni.org/isni/0000000118392952']
SET person_7593a336e68d.source = 'musicbrainz.org'


MERGE (person_0f0c2c00acca:Person{ uuid: '2870c503-db9d-4362-9af3-0f0c2c00acca' }) 
SET person_0f0c2c00acca.name = 'Nelson Shawn'
SET person_0f0c2c00acca.gender = 'Male'
SET person_0f0c2c00acca.country = 'US'
SET person_0f0c2c00acca.discogs = 'https://www.discogs.com/artist/826019'
SET person_0f0c2c00acca.wikidata = 'https://www.wikidata.org/wiki/Q110985202'
SET person_0f0c2c00acca.musicbrainz = 'https://musicbrainz.org/artist/2870c503-db9d-4362-9af3-0f0c2c00acca'
SET person_0f0c2c00acca.source = 'musicbrainz.org'


MERGE (person_acc0205f7513:Person{ uuid: '346448f5-25a0-4f78-bbd6-acc0205f7513' }) 
SET person_acc0205f7513.name = 'Richard Rodgers'
SET person_acc0205f7513.gender = 'Male'
SET person_acc0205f7513.disambiguation = 'composer'
SET person_acc0205f7513.country = 'US'
SET person_acc0205f7513.allmusic = 'https://www.allmusic.com/artist/mn0000820913'
SET person_acc0205f7513.bbc = 'https://www.bbc.co.uk/music/artists/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.discogs = 'https://www.discogs.com/artist/255801'
SET person_acc0205f7513.imdb = 'https://www.imdb.com/name/nm0006256/'
SET person_acc0205f7513.viaf = 'http://viaf.org/viaf/113475079'
SET person_acc0205f7513.wikidata = 'https://www.wikidata.org/wiki/Q269094'
SET person_acc0205f7513.databases = ['http://d-nb.info/gnd/118790862', 'http://id.loc.gov/authorities/names/n50048058', 'https://catalogue.bnf.fr/ark:/12148/cb13899099w', 'https://ibdb.com/person.php?id=8323', 'http://snaccooperative.org/ark:/99166/w69h6cvt', 'https://nla.gov.au/nla.party-1015762', 'https://openlibrary.org/works/OL35365A', 'https://rateyourmusic.com/artist/richard_rodgers', 'https://www.worldcat.org/identities/lccn-n50048058/']
SET person_acc0205f7513.musicbrainz = 'https://musicbrainz.org/artist/346448f5-25a0-4f78-bbd6-acc0205f7513'
SET person_acc0205f7513.isni_list = ['http://isni.org/isni/0000000121482043']
SET person_acc0205f7513.source = 'musicbrainz.org'


MERGE (person_cabff6fab531:Person{ uuid: '42e52c03-27bb-4545-8924-cabff6fab531' }) 
SET person_cabff6fab531.name = 'Yip Harburg'
SET person_cabff6fab531.gender = 'Male'
SET person_cabff6fab531.country = 'US'
SET person_cabff6fab531.allmusic = 'https://www.allmusic.com/artist/mn0000806535'
SET person_cabff6fab531.discogs = 'https://www.discogs.com/artist/573556'
SET person_cabff6fab531.imdb = 'https://www.imdb.com/name/nm0361971/'
SET person_cabff6fab531.viaf = 'http://viaf.org/viaf/120709724'
SET person_cabff6fab531.wikidata = 'https://www.wikidata.org/wiki/Q1273621'
SET person_cabff6fab531.databases = ['http://d-nb.info/gnd/11919158X', 'http://id.loc.gov/authorities/names/n85342788', 'https://catalogue.bnf.fr/ark:/12148/cb13798046w', 'https://ibdb.com/person.php?id=5177', 'http://snaccooperative.org/ark:/99166/w6q9253m', 'https://nla.gov.au/nla.party-877568', 'https://openlibrary.org/works/OL6933834A', 'https://rateyourmusic.com/artist/e_y__yip_harburg', 'https://www.worldcat.org/identities/lccn-n85342788/']
SET person_cabff6fab531.musicbrainz = 'https://musicbrainz.org/artist/42e52c03-27bb-4545-8924-cabff6fab531'
SET person_cabff6fab531.isni_list = ['http://isni.org/isni/0000000117013279', 'http://isni.org/isni/0000000372914779']
SET person_cabff6fab531.source = 'musicbrainz.org'


MERGE (work_4d4f5066e485:Work{ uuid: '2adc274e-85ba-3620-91b8-4d4f5066e485' })
SET work_4d4f5066e485.name = 'April in Paris'
SET work_4d4f5066e485.iswc = 'T-070.882.094-3'
SET work_4d4f5066e485.type = 'Song'
SET work_4d4f5066e485.wikidata = 'https://www.wikidata.org/wiki/Q4355132'
SET work_4d4f5066e485.musicbrainz = 'https://musicbrainz.org/work/2adc274e-85ba-3620-91b8-4d4f5066e485'
SET work_4d4f5066e485.source = 'musicbrainz.org'


MERGE (work_bfef5c5a47ad:Work{ uuid: 'b4e22827-c5b9-3296-a005-bfef5c5a47ad' })
SET work_bfef5c5a47ad.name = 'Knickerbocker Holiday: September Song'
SET work_bfef5c5a47ad.iswc = 'T-070.134.721-8'
SET work_bfef5c5a47ad.type = 'Song'
SET work_bfef5c5a47ad.wikidata = 'https://www.wikidata.org/wiki/Q7452233'
SET work_bfef5c5a47ad.musicbrainz = 'https://musicbrainz.org/work/b4e22827-c5b9-3296-a005-bfef5c5a47ad'
SET work_bfef5c5a47ad.source = 'musicbrainz.org'


MERGE (work_c69b5950c66f:Work{ uuid: 'bcadc8b4-c55c-3425-bcb3-c69b5950c66f' })
SET work_c69b5950c66f.name = 'Jim'
SET work_c69b5950c66f.iswc = 'T-070.267.692-3'
SET work_c69b5950c66f.type = 'Song'
SET work_c69b5950c66f.wikidata = 'https://www.wikidata.org/wiki/Q6193279'
SET work_c69b5950c66f.musicbrainz = 'https://musicbrainz.org/work/bcadc8b4-c55c-3425-bcb3-c69b5950c66f'
SET work_c69b5950c66f.source = 'musicbrainz.org'


MERGE (work_f0cbebe983b3:Work{ uuid: 'deba4b05-e0b4-39a1-908f-f0cbebe983b3' })
SET work_f0cbebe983b3.name = 'He’s My Guy'
SET work_f0cbebe983b3.iswc = 'T-070.265.055-2'
SET work_f0cbebe983b3.type = 'Song'
SET work_f0cbebe983b3.wikidata = 'https://www.wikidata.org/wiki/Q110985568'
SET work_f0cbebe983b3.musicbrainz = 'https://musicbrainz.org/work/deba4b05-e0b4-39a1-908f-f0cbebe983b3'
SET work_f0cbebe983b3.source = 'musicbrainz.org'


MERGE (work_4411df467d9b:Work{ uuid: 'bc51cec1-1c4d-3b1b-83a7-4411df467d9b' })
SET work_4411df467d9b.name = 'Lullaby of Birdland'
SET work_4411df467d9b.iswc = 'T-070.268.678-9'
SET work_4411df467d9b.type = 'Song'
SET work_4411df467d9b.wikidata = 'https://www.wikidata.org/wiki/Q1434051'
SET work_4411df467d9b.musicbrainz = 'https://musicbrainz.org/work/bc51cec1-1c4d-3b1b-83a7-4411df467d9b'
SET work_4411df467d9b.source = 'musicbrainz.org'


MERGE (work_f50508027c99:Work{ uuid: '5bce8526-0c0e-4732-afc3-f50508027c99' })
SET work_f50508027c99.name = 'It\\'s Crazy'
SET work_f50508027c99.type = 'Song'
SET work_f50508027c99.source = 'musicbrainz.org'


MERGE (work_7c0d2793d8d9:Work{ uuid: '13869248-f36a-3fe0-a8bd-7c0d2793d8d9' })
SET work_7c0d2793d8d9.name = 'Embraceable You'
SET work_7c0d2793d8d9.iswc = 'T-010.433.969-6'
SET work_7c0d2793d8d9.type = 'Song'
SET work_7c0d2793d8d9.wikidata = 'https://www.wikidata.org/wiki/Q753607'
SET work_7c0d2793d8d9.musicbrainz = 'https://musicbrainz.org/work/13869248-f36a-3fe0-a8bd-7c0d2793d8d9'
SET work_7c0d2793d8d9.source = 'musicbrainz.org'


MERGE (work_c96df644521c:Work{ uuid: '151ac679-bdc7-4d5a-9325-c96df644521c' })
SET work_c96df644521c.name = 'You’re Not the Kind'
SET work_c96df644521c.iswc = 'T-071.194.081-6'
SET work_c96df644521c.type = 'Song'
SET work_c96df644521c.source = 'musicbrainz.org'


MERGE (work_d95a06e6bd57:Work{ uuid: '2cfe5f75-75db-36bc-95ec-d95a06e6bd57' })
SET work_d95a06e6bd57.name = 'I’m Glad There Is You'
SET work_d95a06e6bd57.iswc = 'T-070.905.741-9'
SET work_d95a06e6bd57.type = 'Song'
SET work_d95a06e6bd57.wikidata = 'https://www.wikidata.org/wiki/Q5966267'
SET work_d95a06e6bd57.musicbrainz = 'https://musicbrainz.org/work/2cfe5f75-75db-36bc-95ec-d95a06e6bd57'
SET work_d95a06e6bd57.source = 'musicbrainz.org'



// performances of
MERGE (perf_d392d8d26a10)-[:PERFORMANCE_OF]->(work_4d4f5066e485)
MERGE (perf_1fa9437cea92)-[:PERFORMANCE_OF]->(work_bfef5c5a47ad)
MERGE (perf_974ef6842862)-[:PERFORMANCE_OF]->(work_c69b5950c66f)
MERGE (perf_0d4ab9d8818b)-[:PERFORMANCE_OF]->(work_f0cbebe983b3)
MERGE (perf_7ecdd90ce2e1)-[:PERFORMANCE_OF]->(work_4411df467d9b)
MERGE (perf_91d9f082645e)-[:PERFORMANCE_OF]->(work_f50508027c99)
MERGE (perf_91d9f082645e)-[:PERFORMANCE_OF]->(work_f50508027c99)
MERGE (perf_5b9d48ddcb6b)-[:PERFORMANCE_OF]->(work_7c0d2793d8d9)
MERGE (perf_5b9d48ddcb6b)-[:PERFORMANCE_OF]->(work_7c0d2793d8d9)
MERGE (perf_8b1b8d05c196)-[:PERFORMANCE_OF]->(work_c96df644521c)
MERGE (perf_8849bcd91686)-[:PERFORMANCE_OF]->(work_d95a06e6bd57)


// composers
MERGE (person_6a07564b5394)-[:COMPOSED]->(work_4d4f5066e485)
MERGE (person_cabff6fab531)-[:WROTE_LYRICS]->(work_4d4f5066e485)
MERGE (person_4f7500861060)-[:COMPOSED]->(work_bfef5c5a47ad)
MERGE (person_e9da3eef0186)-[:WROTE_LYRICS]->(work_bfef5c5a47ad)
MERGE (person_434e2b3faba6)-[:COMPOSED]->(work_c69b5950c66f)
MERGE (person_640857a22571)-[:COMPOSED]->(work_c69b5950c66f)
MERGE (person_0f0c2c00acca)-[:WROTE_LYRICS]->(work_c69b5950c66f)
MERGE (person_7593a336e68d)-[:COMPOSED]->(work_f0cbebe983b3)
MERGE (person_c5d6969cef65)-[:WROTE_LYRICS]->(work_f0cbebe983b3)
MERGE (person_df9db18b28e9)-[:COMPOSED]->(work_4411df467d9b)
MERGE (person_560575963ee1)-[:WROTE_LYRICS]->(work_4411df467d9b)
MERGE (person_acc0205f7513)-[:COMPOSED]->(work_f50508027c99)
MERGE (person_cae1b1c6362f)-[:WROTE_LYRICS]->(work_f50508027c99)
MERGE (person_b693a808a158)-[:COMPOSED]->(work_7c0d2793d8d9)
MERGE (person_322e34240ffc)-[:WROTE_LYRICS]->(work_7c0d2793d8d9)
MERGE (person_1226521487b7)-[:COMPOSED]->(work_c96df644521c)
MERGE (person_1ef2fece51ce)-[:COMPOSED]->(work_c96df644521c)
MERGE (person_de901f0101e9)-[:COMPOSED]->(work_d95a06e6bd57)
MERGE (person_a80827ca20da)-[:COMPOSED]->(work_d95a06e6bd57)


// place nodes

MERGE (place_decbb365c07f:Place{ uuid: '74e50e58-5deb-4b99-93a2-decbb365c07f' })
SET place_decbb365c07f.name = 'New York'
SET place_decbb365c07f.source = 'musicbrainz.org'

MERGE (place_51b696367905:Place{ uuid: '2932299c-1d1d-4834-add5-51b696367905' })
SET place_51b696367905.name = 'Mister Kelly’s'
SET place_51b696367905.source = 'musicbrainz.org'


// place relationships
MERGE (perf_0d4ab9d8818b)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-18', end_date: '1954-12-18' }]->(place_decbb365c07f)
MERGE (perf_974ef6842862)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-18', end_date: '1954-12-18' }]->(place_decbb365c07f)
MERGE (perf_8b1b8d05c196)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-16', end_date: '1954-12-16' }]->(place_decbb365c07f)
MERGE (perf_5b9d48ddcb6b)-[:HAS_PLACE { type: 'recorded at', begin_date: '1957-08-08', end_date: '1957-08-08' }]->(place_51b696367905)
MERGE (perf_5b9d48ddcb6b)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-18', end_date: '1954-12-18' }]->(place_decbb365c07f)
MERGE (perf_8849bcd91686)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-16', end_date: '1954-12-16' }]->(place_decbb365c07f)
MERGE (perf_1fa9437cea92)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-16', end_date: '1954-12-16' }]->(place_decbb365c07f)
MERGE (perf_91d9f082645e)-[:HAS_PLACE { type: 'recorded in', begin_date: '1954-12-18', end_date: '1954-12-18' }]->(place_decbb365c07f)

MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_0d4ab9d8818b)
MERGE (person_eab1269c7ba8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_0d4ab9d8818b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_0d4ab9d8818b)
MERGE (person_022409fbce60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_0d4ab9d8818b)
MERGE (person_209e4eaf1b70)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_0d4ab9d8818b)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_0d4ab9d8818b)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_974ef6842862)
MERGE (person_eab1269c7ba8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_974ef6842862)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_974ef6842862)
MERGE (person_022409fbce60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_974ef6842862)
MERGE (person_209e4eaf1b70)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_974ef6842862)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_974ef6842862)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8b1b8d05c196)
MERGE (person_eab1269c7ba8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8b1b8d05c196)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8b1b8d05c196)
MERGE (person_022409fbce60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_8b1b8d05c196)
MERGE (person_209e4eaf1b70)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8b1b8d05c196)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_8b1b8d05c196)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5b9d48ddcb6b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)', 'drums (drum set)'] }]->(perf_5b9d48ddcb6b)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5b9d48ddcb6b)
MERGE (person_beee70c5e271)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5b9d48ddcb6b)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer', 'singer'] }]->(perf_5b9d48ddcb6b)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8849bcd91686)
MERGE (person_eab1269c7ba8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_8849bcd91686)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_8849bcd91686)
MERGE (person_022409fbce60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_8849bcd91686)
MERGE (person_209e4eaf1b70)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_8849bcd91686)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_8849bcd91686)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1fa9437cea92)
MERGE (person_eab1269c7ba8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_1fa9437cea92)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1fa9437cea92)
MERGE (person_022409fbce60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_1fa9437cea92)
MERGE (person_209e4eaf1b70)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_1fa9437cea92)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_1fa9437cea92)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_91d9f082645e)
MERGE (person_eab1269c7ba8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_91d9f082645e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_91d9f082645e)
MERGE (person_022409fbce60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['flute'] }]->(perf_91d9f082645e)
MERGE (person_209e4eaf1b70)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_91d9f082645e)
MERGE (person_c85fad20da55)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_91d9f082645e)



"""
)