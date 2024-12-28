
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_fcb59b338c51:Release{ uuid: 'a90a0375-ed82-487d-bfef-fcb59b338c51' })
SET release_fcb59b338c51.name = 'Question and Answer'
SET release_fcb59b338c51.country = 'XE'
SET release_fcb59b338c51.date = '1990'
SET release_fcb59b338c51.format = 'CD'
SET release_fcb59b338c51.discode = '424 293-2'
SET release_fcb59b338c51.discogs = 'https://www.discogs.com/release/10742522'
SET release_fcb59b338c51.musicbrainz = 'http://musicbrainz.org/release/a90a0375-ed82-487d-bfef-fcb59b338c51'
SET release_fcb59b338c51.source = 'musicbrainz.org'


MERGE (person_dbad528aa58e:Person{ uuid: '7ea233ad-c340-4f62-8678-dbad528aa58e' }) 
SET person_dbad528aa58e.name = 'Dave Holland'
SET person_dbad528aa58e.gender = 'Male'
SET person_dbad528aa58e.disambiguation = 'British jazz bassist and composer'
SET person_dbad528aa58e.country = 'GB'
SET person_dbad528aa58e.allmusic = 'https://www.allmusic.com/artist/mn0000585092'
SET person_dbad528aa58e.bbc = 'https://www.bbc.co.uk/music/artists/7ea233ad-c340-4f62-8678-dbad528aa58e'
SET person_dbad528aa58e.discogs = 'https://www.discogs.com/artist/84214'
SET person_dbad528aa58e.imdb = 'https://www.imdb.com/name/nm1180224/'
SET person_dbad528aa58e.viaf = 'http://viaf.org/viaf/115064351'
SET person_dbad528aa58e.wikidata = 'https://www.wikidata.org/wiki/Q504671'
SET person_dbad528aa58e.databases = ['http://d-nb.info/gnd/134409361', 'http://id.loc.gov/authorities/names/n84163014', 'https://catalogue.bnf.fr/ark:/12148/cb13895278h', 'http://snaccooperative.org/ark:/99166/w6dn45cm', 'https://www.worldcat.org/identities/lccn-n84163014']
SET person_dbad528aa58e.musicbrainz = 'https://musicbrainz.org/artist/7ea233ad-c340-4f62-8678-dbad528aa58e'
SET person_dbad528aa58e.isni_list = ['http://isni.org/isni/0000000084120907']
SET person_dbad528aa58e.source = 'musicbrainz.org'


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


MERGE (person_f014a10fb3f2:Person{ uuid: '1fcaf7ef-ecf4-43c3-a5d6-f014a10fb3f2' }) 
SET person_f014a10fb3f2.name = 'Rob Eaton'
SET person_f014a10fb3f2.gender = 'Male'
SET person_f014a10fb3f2.country = 'US'
SET person_f014a10fb3f2.allmusic = 'https://www.allmusic.com/artist/mn0000229578'
SET person_f014a10fb3f2.discogs = 'https://www.discogs.com/artist/255341'
SET person_f014a10fb3f2.databases = ['https://rateyourmusic.com/artist/rob_eaton']
SET person_f014a10fb3f2.musicbrainz = 'https://musicbrainz.org/artist/1fcaf7ef-ecf4-43c3-a5d6-f014a10fb3f2'
SET person_f014a10fb3f2.source = 'musicbrainz.org'


MERGE (person_08192698e72f:Person{ uuid: '07ba1d36-6542-438b-b35a-08192698e72f' }) 
SET person_08192698e72f.name = 'Matthew "Boomer" LaMonica'
SET person_08192698e72f.gender = 'Male'
SET person_08192698e72f.country = 'US'
SET person_08192698e72f.allmusic = 'https://www.allmusic.com/artist/mn0000398557'
SET person_08192698e72f.allmusic = 'https://www.allmusic.com/artist/mn0003060803'
SET person_08192698e72f.discogs = 'https://www.discogs.com/artist/250936'
SET person_08192698e72f.discogs = 'https://www.discogs.com/artist/925092'
SET person_08192698e72f.databases = ['https://rateyourmusic.com/artist/matthew_lamonica']
SET person_08192698e72f.musicbrainz = 'https://musicbrainz.org/artist/07ba1d36-6542-438b-b35a-08192698e72f'
SET person_08192698e72f.source = 'musicbrainz.org'


MERGE (person_f8091d98cf25:Person{ uuid: '7daac7f9-8fcc-485f-a14f-f8091d98cf25' }) 
SET person_f8091d98cf25.name = 'Pat Metheny'
SET person_f8091d98cf25.gender = 'Male'
SET person_f8091d98cf25.country = 'US'
SET person_f8091d98cf25.allmusic = 'https://www.allmusic.com/artist/mn0000179698'
SET person_f8091d98cf25.bbc = 'https://www.bbc.co.uk/music/artists/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.discogs = 'https://www.discogs.com/artist/20185'
SET person_f8091d98cf25.imdb = 'https://www.imdb.com/name/nm0582533/'
SET person_f8091d98cf25.viaf = 'http://viaf.org/viaf/22188874'
SET person_f8091d98cf25.wikidata = 'https://www.wikidata.org/wiki/Q213887'
SET person_f8091d98cf25.databases = ['http://d-nb.info/gnd/118946803', 'http://id.loc.gov/authorities/names/n78096789', 'https://catalogue.bnf.fr/ark:/12148/cb122016747', 'http://snaccooperative.org/ark:/99166/w6gj10fw', 'https://www.musik-sammler.de/artist/pat-metheny/', 'https://www.progarchives.com/artist.asp?id=2445', 'https://www.worldcat.org/identities/lccn-n78096789']
SET person_f8091d98cf25.musicbrainz = 'https://musicbrainz.org/artist/7daac7f9-8fcc-485f-a14f-f8091d98cf25'
SET person_f8091d98cf25.isni_list = ['http://isni.org/isni/0000000121236985']
SET person_f8091d98cf25.source = 'musicbrainz.org'


// labels

MERGE (label_612b317e716b:Label{ uuid: '0fadc2ce-f7de-4e27-bbe6-612b317e716b' })
SET label_612b317e716b.name= 'Geffen Records'

// performances

MERGE (perf_15489714817e:Performance{ uuid: '3df74772-8928-492f-a21f-15489714817e' })
SET perf_15489714817e.name = 'Solar'
SET perf_15489714817e.duration = '8:27'
SET perf_15489714817e.begin_date = '1989-12-21'
SET perf_15489714817e.end_date = '1989-12-21'
SET perf_15489714817e.source = 'musicbrainz.org'


MERGE (perf_6ce8a06eff96:Performance{ uuid: 'be9c117f-adfc-40c4-aec0-6ce8a06eff96' })
SET perf_6ce8a06eff96.name = 'Question and Answer'
SET perf_6ce8a06eff96.duration = '7:10'
SET perf_6ce8a06eff96.begin_date = '1989-12-21'
SET perf_6ce8a06eff96.end_date = '1989-12-21'
SET perf_6ce8a06eff96.source = 'musicbrainz.org'


MERGE (perf_4bb11bd76764:Performance{ uuid: '8700cca8-b2e1-4c6c-9c32-4bb11bd76764' })
SET perf_4bb11bd76764.name = 'H & H'
SET perf_4bb11bd76764.duration = '6:51'
SET perf_4bb11bd76764.begin_date = '1989-12-21'
SET perf_4bb11bd76764.end_date = '1989-12-21'
SET perf_4bb11bd76764.source = 'musicbrainz.org'


MERGE (perf_1b34fa4195c0:Performance{ uuid: '8d32137a-e581-4899-bee4-1b34fa4195c0' })
SET perf_1b34fa4195c0.name = 'Never Too Far Away'
SET perf_1b34fa4195c0.duration = '5:54'
SET perf_1b34fa4195c0.begin_date = '1989-12-21'
SET perf_1b34fa4195c0.end_date = '1989-12-21'
SET perf_1b34fa4195c0.source = 'musicbrainz.org'


MERGE (perf_f3448cf1e869:Performance{ uuid: 'a2194d0e-93ce-4250-969a-f3448cf1e869' })
SET perf_f3448cf1e869.name = 'Law Years'
SET perf_f3448cf1e869.duration = '6:54'
SET perf_f3448cf1e869.begin_date = '1989-12-21'
SET perf_f3448cf1e869.end_date = '1989-12-21'
SET perf_f3448cf1e869.source = 'musicbrainz.org'


MERGE (perf_ba91209aea84:Performance{ uuid: 'b406d7f6-df27-4bff-b23f-ba91209aea84' })
SET perf_ba91209aea84.name = 'Change of Heart'
SET perf_ba91209aea84.duration = '6:16'
SET perf_ba91209aea84.begin_date = '1989-12-21'
SET perf_ba91209aea84.end_date = '1989-12-21'
SET perf_ba91209aea84.source = 'musicbrainz.org'


MERGE (perf_02c14d3b97c0:Performance{ uuid: 'd70b09f3-63dd-412c-8b9f-02c14d3b97c0' })
SET perf_02c14d3b97c0.name = 'All the Things You Are'
SET perf_02c14d3b97c0.duration = '8:25'
SET perf_02c14d3b97c0.begin_date = '1989-12-21'
SET perf_02c14d3b97c0.end_date = '1989-12-21'
SET perf_02c14d3b97c0.source = 'musicbrainz.org'


MERGE (perf_9719b2592600:Performance{ uuid: 'c796f3b1-0e4a-4900-96c5-9719b2592600' })
SET perf_9719b2592600.name = 'Old Folks'
SET perf_9719b2592600.duration = '6:40'
SET perf_9719b2592600.begin_date = '1989-12-21'
SET perf_9719b2592600.end_date = '1989-12-21'
SET perf_9719b2592600.source = 'musicbrainz.org'


MERGE (perf_e74f54dd296f:Performance{ uuid: '102a2be9-e9f7-40cb-af47-e74f54dd296f' })
SET perf_e74f54dd296f.name = 'Three Flights Up'
SET perf_e74f54dd296f.duration = '6:11'
SET perf_e74f54dd296f.begin_date = '1989-12-21'
SET perf_e74f54dd296f.end_date = '1989-12-21'
SET perf_e74f54dd296f.source = 'musicbrainz.org'




// labels
MERGE (release_fcb59b338c51)-[:HAS_LABEL]->(label_612b317e716b)
MERGE (release_fcb59b338c51)-[:HAS_LABEL]->(label_612b317e716b)
MERGE (release_fcb59b338c51)-[:HAS_LABEL]->(label_612b317e716b)


// tracks
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_15489714817e)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_6ce8a06eff96)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_4bb11bd76764)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_1b34fa4195c0)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_f3448cf1e869)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_ba91209aea84)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_02c14d3b97c0)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_9719b2592600)
MERGE (release_fcb59b338c51)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_e74f54dd296f)

// works

MERGE (person_323e6ce46c2a:Person{ uuid: '561d854a-6a28-4aa7-8c99-323e6ce46c2a' }) 
SET person_323e6ce46c2a.name = 'Miles Davis'
SET person_323e6ce46c2a.gender = 'Male'
SET person_323e6ce46c2a.disambiguation = 'jazz trumpeter, bandleader, songwriter'
SET person_323e6ce46c2a.country = 'US'
SET person_323e6ce46c2a.allmusic = 'https://www.allmusic.com/artist/mn0000423829'
SET person_323e6ce46c2a.bbc = 'https://www.bbc.co.uk/music/artists/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.discogs = 'https://www.discogs.com/artist/23755'
SET person_323e6ce46c2a.imdb = 'https://www.imdb.com/name/nm0002537/'
SET person_323e6ce46c2a.viaf = 'http://viaf.org/viaf/97762193'
SET person_323e6ce46c2a.wikidata = 'https://www.wikidata.org/wiki/Q93341'
SET person_323e6ce46c2a.databases = ['http://d-nb.info/gnd/118524046', 'http://id.loc.gov/authorities/names/n50035608', 'http://musicmoz.org/Bands_and_Artists/D/Davis,_Miles/', 'https://catalogue.bnf.fr/ark:/12148/cb13893030g', 'http://snaccooperative.org/ark:/99166/w68k7wq0', 'https://openlibrary.org/works/OL4359245A', 'https://rateyourmusic.com/artist/miles_davis', 'https://www.muziekweb.nl/Link/M00000286446/', 'https://www.worldcat.org/identities/lccn-n50035608', 'http://www.45cat.com/artist/miles-davis', 'http://www.45worlds.com/78rpm/artist/miles-davis', 'http://www.45worlds.com/cdalbum/artist/miles-davis', 'http://www.45worlds.com/live/artist/miles-davis', 'http://www.45worlds.com/tape/artist/miles-davis', 'http://www.45worlds.com/vinyl/artist/miles-davis']
SET person_323e6ce46c2a.musicbrainz = 'https://musicbrainz.org/artist/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.isni_list = ['http://isni.org/isni/000000012144707X']
SET person_323e6ce46c2a.source = 'musicbrainz.org'


MERGE (person_f324ef1bf494:Person{ uuid: '8fb64b2e-db8b-4579-ad08-f324ef1bf494' }) 
SET person_f324ef1bf494.name = 'Jerome Kern'
SET person_f324ef1bf494.gender = 'Male'
SET person_f324ef1bf494.country = 'US'
SET person_f324ef1bf494.allmusic = 'https://www.allmusic.com/artist/mn0000031646'
SET person_f324ef1bf494.discogs = 'https://www.discogs.com/artist/166685'
SET person_f324ef1bf494.imdb = 'https://www.imdb.com/name/nm0006153/'
SET person_f324ef1bf494.viaf = 'http://viaf.org/viaf/196726'
SET person_f324ef1bf494.wikidata = 'https://www.wikidata.org/wiki/Q313270'
SET person_f324ef1bf494.databases = ['http://d-nb.info/gnd/118777084', 'http://id.loc.gov/authorities/names/n80149466', 'https://catalogue.bnf.fr/ark:/12148/cb13895945g', 'https://ibdb.com/person.php?id=6711', 'http://snaccooperative.org/ark:/99166/w6rg6m1n', 'https://nla.gov.au/anbd.aut-an36379903', 'https://openlibrary.org/works/OL786332A', 'https://rateyourmusic.com/artist/jerome-kern', 'https://www.worldcat.org/identities/lccn-n80-149466', 'http://www.lortel.org/Archives/CreditableEntity/11862']
SET person_f324ef1bf494.musicbrainz = 'https://musicbrainz.org/artist/8fb64b2e-db8b-4579-ad08-f324ef1bf494'
SET person_f324ef1bf494.isni_list = ['http://isni.org/isni/000000010861737X']
SET person_f324ef1bf494.source = 'musicbrainz.org'


MERGE (person_a53ce51ee4ad:Person{ uuid: '3c86df3f-6398-46a5-a013-a53ce51ee4ad' }) 
SET person_a53ce51ee4ad.name = 'Willard Robison'
SET person_a53ce51ee4ad.gender = 'Male'
SET person_a53ce51ee4ad.country = 'US'
SET person_a53ce51ee4ad.allmusic = 'https://www.allmusic.com/artist/mn0000693503'
SET person_a53ce51ee4ad.discogs = 'https://www.discogs.com/artist/264111'
SET person_a53ce51ee4ad.imdb = 'https://www.imdb.com/name/nm0733188/'
SET person_a53ce51ee4ad.viaf = 'http://viaf.org/viaf/13945872'
SET person_a53ce51ee4ad.wikidata = 'https://www.wikidata.org/wiki/Q2576625'
SET person_a53ce51ee4ad.databases = ['http://d-nb.info/gnd/174031122', 'http://id.loc.gov/authorities/names/n91037194', 'https://catalogue.bnf.fr/ark:/12148/cb13809798m', 'https://ibdb.com/person.php?id=12304', 'http://snaccooperative.org/ark:/99166/w6zd0q3p', 'https://rateyourmusic.com/artist/willard_robison', 'https://www.worldcat.org/identities/lccn-n91037194']
SET person_a53ce51ee4ad.musicbrainz = 'https://musicbrainz.org/artist/3c86df3f-6398-46a5-a013-a53ce51ee4ad'
SET person_a53ce51ee4ad.isni_list = ['http://isni.org/isni/000000008093169X']
SET person_a53ce51ee4ad.source = 'musicbrainz.org'


MERGE (person_9205b2f8f171:Person{ uuid: 'a383f062-e527-4a57-98b0-9205b2f8f171' }) 
SET person_9205b2f8f171.name = 'Oscar Hammerstein II'
SET person_9205b2f8f171.gender = 'Male'
SET person_9205b2f8f171.disambiguation = 'of Rodgers & Hammerstein'
SET person_9205b2f8f171.country = 'US'
SET person_9205b2f8f171.allmusic = 'https://www.allmusic.com/artist/mn0000804858'
SET person_9205b2f8f171.discogs = 'https://www.discogs.com/artist/253375'
SET person_9205b2f8f171.imdb = 'https://www.imdb.com/name/nm0358564/'
SET person_9205b2f8f171.viaf = 'http://viaf.org/viaf/196386'
SET person_9205b2f8f171.wikidata = 'https://www.wikidata.org/wiki/Q319693'
SET person_9205b2f8f171.databases = ['http://d-nb.info/gnd/11872018X', 'http://id.loc.gov/authorities/names/n50020012', 'https://catalogue.bnf.fr/ark:/12148/cb13894931j', 'https://ibdb.com/person.php?id=7965', 'http://snaccooperative.org/ark:/99166/w6vf7qf7', 'https://nla.gov.au/nla.party-869608', 'https://openlibrary.org/works/OL577328A', 'https://rateyourmusic.com/artist/oscar_hammerstein_ii', 'https://www.worldcat.org/identities/lccn-n50020012/']
SET person_9205b2f8f171.musicbrainz = 'https://musicbrainz.org/artist/a383f062-e527-4a57-98b0-9205b2f8f171'
SET person_9205b2f8f171.isni_list = ['http://isni.org/isni/0000000117358007']
SET person_9205b2f8f171.source = 'musicbrainz.org'


MERGE (person_829aa7b39205:Person{ uuid: '169c0d1b-fcb8-4a43-9097-829aa7b39205' }) 
SET person_829aa7b39205.name = 'Ornette Coleman'
SET person_829aa7b39205.gender = 'Male'
SET person_829aa7b39205.country = 'US'
SET person_829aa7b39205.allmusic = 'https://www.allmusic.com/artist/mn0000484396'
SET person_829aa7b39205.bbc = 'https://www.bbc.co.uk/music/artists/169c0d1b-fcb8-4a43-9097-829aa7b39205'
SET person_829aa7b39205.discogs = 'https://www.discogs.com/artist/224506'
SET person_829aa7b39205.imdb = 'https://www.imdb.com/name/nm0171170/'
SET person_829aa7b39205.viaf = 'http://viaf.org/viaf/79166373'
SET person_829aa7b39205.wikidata = 'https://www.wikidata.org/wiki/Q208797'
SET person_829aa7b39205.databases = ['http://d-nb.info/gnd/118890964', 'http://id.loc.gov/authorities/names/n83071536', 'https://catalogue.bnf.fr/ark:/12148/cb13892628b', 'http://snaccooperative.org/ark:/99166/w6rz0q2w', 'https://rateyourmusic.com/artist/ornette_coleman', 'https://www.musik-sammler.de/artist/ornette-coleman/', 'https://www.worldcat.org/oclc/935032488']
SET person_829aa7b39205.musicbrainz = 'https://musicbrainz.org/artist/169c0d1b-fcb8-4a43-9097-829aa7b39205'
SET person_829aa7b39205.isni_list = ['http://isni.org/isni/0000000117719685']
SET person_829aa7b39205.source = 'musicbrainz.org'


MERGE (person_04c57e256ba5:Person{ uuid: '6e03bb52-930f-4a16-8466-04c57e256ba5' }) 
SET person_04c57e256ba5.name = 'Dedette Lee Hill'
SET person_04c57e256ba5.gender = 'Female'
SET person_04c57e256ba5.country = 'US'
SET person_04c57e256ba5.discogs = 'https://www.discogs.com/artist/679021'
SET person_04c57e256ba5.musicbrainz = 'https://musicbrainz.org/artist/6e03bb52-930f-4a16-8466-04c57e256ba5'
SET person_04c57e256ba5.source = 'musicbrainz.org'


MERGE (work_d637a0c37c1e:Work{ uuid: '03e3580d-37ae-4e85-8cc7-d637a0c37c1e' })
SET work_d637a0c37c1e.name = 'Change of Heart'
SET work_d637a0c37c1e.source = 'musicbrainz.org'


MERGE (work_cb8ba5437f00:Work{ uuid: '08040d21-621b-4afb-8363-cb8ba5437f00' })
SET work_cb8ba5437f00.name = 'Never Too Far Away'
SET work_cb8ba5437f00.source = 'musicbrainz.org'


MERGE (work_9142b87d0c62:Work{ uuid: 'f89ee5b0-7bb3-4e05-910f-9142b87d0c62' })
SET work_9142b87d0c62.name = 'Three Flights Up'
SET work_9142b87d0c62.source = 'musicbrainz.org'


MERGE (work_b3ebd3df6199:Work{ uuid: 'd73f8e96-325d-3211-89ba-b3ebd3df6199' })
SET work_b3ebd3df6199.name = 'Solar'
SET work_b3ebd3df6199.type = 'Song'
SET work_b3ebd3df6199.source = 'musicbrainz.org'


MERGE (work_9eae6375ecb0:Work{ uuid: '6ae0f429-cd54-3ac2-b635-9eae6375ecb0' })
SET work_9eae6375ecb0.name = 'Question and Answer'
SET work_9eae6375ecb0.iswc = 'T-070.243.048-5'
SET work_9eae6375ecb0.type = 'Song'
SET work_9eae6375ecb0.source = 'musicbrainz.org'


MERGE (work_1569ab45e972:Work{ uuid: 'fa61dc22-fec9-4c4b-8f65-1569ab45e972' })
SET work_1569ab45e972.name = 'H & H'
SET work_1569ab45e972.type = 'Song'
SET work_1569ab45e972.source = 'musicbrainz.org'


MERGE (work_375718472b05:Work{ uuid: '41f07a86-b141-4edc-8af7-375718472b05' })
SET work_375718472b05.name = 'Law Years'
SET work_375718472b05.type = 'Song'
SET work_375718472b05.source = 'musicbrainz.org'


MERGE (work_f94fc850c090:Work{ uuid: '54c6f3a6-c111-3220-841c-f94fc850c090' })
SET work_f94fc850c090.name = 'Old Folks'
SET work_f94fc850c090.iswc = 'T-070.158.542-3'
SET work_f94fc850c090.type = 'Song'
SET work_f94fc850c090.wikidata = 'https://www.wikidata.org/wiki/Q60743222'
SET work_f94fc850c090.musicbrainz = 'https://musicbrainz.org/work/54c6f3a6-c111-3220-841c-f94fc850c090'
SET work_f94fc850c090.source = 'musicbrainz.org'


MERGE (work_f04324e0f525:Work{ uuid: '6c0ae4fc-2893-363a-a3e9-f04324e0f525' })
SET work_f04324e0f525.name = 'All the Things You Are'
SET work_f04324e0f525.iswc = 'T-070.000.803-2'
SET work_f04324e0f525.type = 'Song'
SET work_f04324e0f525.wikidata = 'https://www.wikidata.org/wiki/Q1410072'
SET work_f04324e0f525.musicbrainz = 'https://musicbrainz.org/work/6c0ae4fc-2893-363a-a3e9-f04324e0f525'
SET work_f04324e0f525.source = 'musicbrainz.org'



// performances of
MERGE (perf_ba91209aea84)-[:PERFORMANCE_OF]->(work_d637a0c37c1e)
MERGE (perf_1b34fa4195c0)-[:PERFORMANCE_OF]->(work_cb8ba5437f00)
MERGE (perf_e74f54dd296f)-[:PERFORMANCE_OF]->(work_9142b87d0c62)
MERGE (perf_15489714817e)-[:PERFORMANCE_OF]->(work_b3ebd3df6199)
MERGE (perf_6ce8a06eff96)-[:PERFORMANCE_OF]->(work_9eae6375ecb0)
MERGE (perf_4bb11bd76764)-[:PERFORMANCE_OF]->(work_1569ab45e972)
MERGE (perf_f3448cf1e869)-[:PERFORMANCE_OF]->(work_375718472b05)
MERGE (perf_9719b2592600)-[:PERFORMANCE_OF]->(work_f94fc850c090)
MERGE (perf_02c14d3b97c0)-[:PERFORMANCE_OF]->(work_f04324e0f525)


// composers
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_d637a0c37c1e)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_cb8ba5437f00)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_9142b87d0c62)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_b3ebd3df6199)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_9eae6375ecb0)
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_1569ab45e972)
MERGE (person_829aa7b39205)-[:COMPOSED]->(work_375718472b05)
MERGE (person_a53ce51ee4ad)-[:COMPOSED]->(work_f94fc850c090)
MERGE (person_04c57e256ba5)-[:WROTE_LYRICS]->(work_f94fc850c090)
MERGE (person_f324ef1bf494)-[:COMPOSED]->(work_f04324e0f525)
MERGE (person_9205b2f8f171)-[:WROTE_LYRICS]->(work_f04324e0f525)


// place nodes

MERGE (place_7e95f332e097:Place{ uuid: 'c8e0e536-3776-44a3-82d3-7e95f332e097' })
SET place_7e95f332e097.name = 'Power Station Studios'
SET place_7e95f332e097.source = 'musicbrainz.org'


// place relationships
MERGE (perf_15489714817e)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_6ce8a06eff96)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_4bb11bd76764)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_1b34fa4195c0)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_f3448cf1e869)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_ba91209aea84)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_02c14d3b97c0)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_9719b2592600)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)
MERGE (perf_e74f54dd296f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1989-12-21', end_date: '1989-12-21' }]->(place_7e95f332e097)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_15489714817e)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_15489714817e)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_15489714817e)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_15489714817e)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6ce8a06eff96)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_6ce8a06eff96)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_6ce8a06eff96)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_6ce8a06eff96)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_4bb11bd76764)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_4bb11bd76764)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_4bb11bd76764)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_4bb11bd76764)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1b34fa4195c0)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1b34fa4195c0)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_1b34fa4195c0)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_1b34fa4195c0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f3448cf1e869)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f3448cf1e869)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_f3448cf1e869)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_f3448cf1e869)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ba91209aea84)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ba91209aea84)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_ba91209aea84)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_ba91209aea84)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_02c14d3b97c0)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_02c14d3b97c0)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_02c14d3b97c0)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_02c14d3b97c0)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_9719b2592600)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_9719b2592600)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_9719b2592600)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_9719b2592600)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e74f54dd296f)
MERGE (person_dbad528aa58e)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_e74f54dd296f)
MERGE (person_f8091d98cf25)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['guitar'] }]->(perf_e74f54dd296f)
MERGE (person_f014a10fb3f2)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_e74f54dd296f)



"""
)