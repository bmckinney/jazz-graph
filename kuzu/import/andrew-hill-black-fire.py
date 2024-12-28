
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_83a9081b75b8:Release{ uuid: 'cd16b8de-943b-49ae-9113-83a9081b75b8' })
SET release_83a9081b75b8.name = 'Black Fire'
SET release_83a9081b75b8.disambiguation = 'mono'
SET release_83a9081b75b8.country = 'US'
SET release_83a9081b75b8.date = '1964'
SET release_83a9081b75b8.format = '12" Vinyl'
SET release_83a9081b75b8.discode = 'BLP 4151'
SET release_83a9081b75b8.discogs = 'https://www.discogs.com/release/1114174'
SET release_83a9081b75b8.musicbrainz = 'http://musicbrainz.org/release/cd16b8de-943b-49ae-9113-83a9081b75b8'
SET release_83a9081b75b8.source = 'musicbrainz.org'


MERGE (person_2584a0b30ec9:Person{ uuid: 'ede80a9f-f114-4041-b0d9-2584a0b30ec9' }) 
SET person_2584a0b30ec9.name = 'Andrew Hill'
SET person_2584a0b30ec9.gender = 'Male'
SET person_2584a0b30ec9.disambiguation = 'jazz pianist'
SET person_2584a0b30ec9.country = 'US'
SET person_2584a0b30ec9.allmusic = 'https://www.allmusic.com/artist/mn0000034617'
SET person_2584a0b30ec9.discogs = 'https://www.discogs.com/artist/61584'
SET person_2584a0b30ec9.viaf = 'http://viaf.org/viaf/22327521'
SET person_2584a0b30ec9.wikidata = 'https://www.wikidata.org/wiki/Q505138'
SET person_2584a0b30ec9.databases = ['http://d-nb.info/gnd/132903911', 'http://id.loc.gov/authorities/names/n81035955', 'https://catalogue.bnf.fr/ark:/12148/cb13895208b', 'http://snaccooperative.org/ark:/99166/w6zw917f', 'https://rateyourmusic.com/artist/andrew_hill', 'https://www.worldcat.org/identities/lccn-n81035955']
SET person_2584a0b30ec9.musicbrainz = 'https://musicbrainz.org/artist/ede80a9f-f114-4041-b0d9-2584a0b30ec9'
SET person_2584a0b30ec9.isni_list = ['http://isni.org/isni/000000012022259X']
SET person_2584a0b30ec9.source = 'musicbrainz.org'


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


MERGE (person_9ee947b4ce37:Person{ uuid: 'bcab8301-c7e5-4689-a4ad-9ee947b4ce37' }) 
SET person_9ee947b4ce37.name = 'Joe Henderson'
SET person_9ee947b4ce37.gender = 'Male'
SET person_9ee947b4ce37.disambiguation = 'US jazz tenor saxophonist'
SET person_9ee947b4ce37.country = 'US'
SET person_9ee947b4ce37.allmusic = 'https://www.allmusic.com/artist/mn0000139804'
SET person_9ee947b4ce37.allmusic = 'https://www.allmusic.com/artist/mn0002687715'
SET person_9ee947b4ce37.discogs = 'https://www.discogs.com/artist/10079'
SET person_9ee947b4ce37.viaf = 'http://viaf.org/viaf/115064662'
SET person_9ee947b4ce37.wikidata = 'https://www.wikidata.org/wiki/Q506006'
SET person_9ee947b4ce37.databases = ['http://d-nb.info/gnd/131961454', 'http://id.loc.gov/authorities/names/n82164702', 'https://catalogue.bnf.fr/ark:/12148/cb138951291', 'http://snaccooperative.org/ark:/99166/w6hm8fsd', 'https://nla.gov.au/nla.party-1048452', 'https://openlibrary.org/works/OL5629680A', 'https://rateyourmusic.com/artist/joe_henderson', 'https://www.worldcat.org/identities/lccn-n82164702']
SET person_9ee947b4ce37.musicbrainz = 'https://musicbrainz.org/artist/bcab8301-c7e5-4689-a4ad-9ee947b4ce37'
SET person_9ee947b4ce37.isni_list = ['http://isni.org/isni/0000000081835181']
SET person_9ee947b4ce37.source = 'musicbrainz.org'


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


MERGE (person_317b31f6c035:Person{ uuid: 'c332fcf2-cc5c-424e-a5ea-317b31f6c035' }) 
SET person_317b31f6c035.name = 'Alfred Lion'
SET person_317b31f6c035.gender = 'Male'
SET person_317b31f6c035.country = 'US'
SET person_317b31f6c035.allmusic = 'https://www.allmusic.com/artist/mn0000742011'
SET person_317b31f6c035.discogs = 'https://www.discogs.com/artist/252962'
SET person_317b31f6c035.viaf = 'http://viaf.org/viaf/11504589'
SET person_317b31f6c035.wikidata = 'https://www.wikidata.org/wiki/Q68260'
SET person_317b31f6c035.wikipedia = 'https://en.wikipedia.org/wiki/Alfred_Lion'
SET person_317b31f6c035.databases = ['http://id.loc.gov/authorities/names/n92085849', 'https://d-nb.info/gnd/1068409134', 'http://snaccooperative.org/ark:/99166/w6qv685s', 'https://rateyourmusic.com/artist/alfred_lion', 'https://www.worldcat.org/identities/lccn-n92085849']
SET person_317b31f6c035.musicbrainz = 'https://musicbrainz.org/artist/c332fcf2-cc5c-424e-a5ea-317b31f6c035'
SET person_317b31f6c035.isni_list = ['http://isni.org/isni/000000003027090X']
SET person_317b31f6c035.source = 'musicbrainz.org'

// labels

MERGE (label_14e1ddfd5946:Label{ uuid: '713c4a95-6616-442b-9cf6-14e1ddfd5946' })
SET label_14e1ddfd5946.name= 'Blue Note'

// performances

MERGE (perf_1033de3344b4:Performance{ uuid: '9bd96eeb-aba6-4bb8-bf1f-1033de3344b4' })
SET perf_1033de3344b4.name = 'Pumpkin'
SET perf_1033de3344b4.disambiguation = 'mono'
SET perf_1033de3344b4.begin_date = '1963-11-08'
SET perf_1033de3344b4.end_date = '1963-11-08'
SET perf_1033de3344b4.source = 'musicbrainz.org'


MERGE (perf_73cb023ee36f:Performance{ uuid: '57118443-7426-4bb7-a76d-73cb023ee36f' })
SET perf_73cb023ee36f.name = 'Subterfuge'
SET perf_73cb023ee36f.disambiguation = 'mono'
SET perf_73cb023ee36f.begin_date = '1963-11-08'
SET perf_73cb023ee36f.end_date = '1963-11-08'
SET perf_73cb023ee36f.source = 'musicbrainz.org'


MERGE (perf_5511bfb80db5:Performance{ uuid: '5a006148-89e7-4616-aebd-5511bfb80db5' })
SET perf_5511bfb80db5.name = 'Black Fire'
SET perf_5511bfb80db5.disambiguation = 'mono'
SET perf_5511bfb80db5.begin_date = '1963-11-08'
SET perf_5511bfb80db5.end_date = '1963-11-08'
SET perf_5511bfb80db5.source = 'musicbrainz.org'


MERGE (perf_2713cd9b018a:Performance{ uuid: 'fcc58ca0-5672-4c19-91e8-2713cd9b018a' })
SET perf_2713cd9b018a.name = 'Cantarnos'
SET perf_2713cd9b018a.disambiguation = 'mono'
SET perf_2713cd9b018a.begin_date = '1963-11-08'
SET perf_2713cd9b018a.end_date = '1963-11-08'
SET perf_2713cd9b018a.source = 'musicbrainz.org'


MERGE (perf_f563c986bab7:Performance{ uuid: 'd82862ee-a7f1-4706-8b6f-f563c986bab7' })
SET perf_f563c986bab7.name = 'Tired Trade'
SET perf_f563c986bab7.disambiguation = 'mono'
SET perf_f563c986bab7.begin_date = '1963-11-08'
SET perf_f563c986bab7.end_date = '1963-11-08'
SET perf_f563c986bab7.source = 'musicbrainz.org'


MERGE (perf_733b8754a19a:Performance{ uuid: '29654f85-8c28-46a4-af8a-733b8754a19a' })
SET perf_733b8754a19a.name = 'McNeil Island'
SET perf_733b8754a19a.disambiguation = 'mono'
SET perf_733b8754a19a.begin_date = '1963-11-08'
SET perf_733b8754a19a.end_date = '1963-11-08'
SET perf_733b8754a19a.source = 'musicbrainz.org'


MERGE (perf_b0e05d4bd99d:Performance{ uuid: '46aa7bb4-8aa3-4cd8-a990-b0e05d4bd99d' })
SET perf_b0e05d4bd99d.name = 'Land of Nod'
SET perf_b0e05d4bd99d.disambiguation = 'mono'
SET perf_b0e05d4bd99d.begin_date = '1963-11-08'
SET perf_b0e05d4bd99d.end_date = '1963-11-08'
SET perf_b0e05d4bd99d.source = 'musicbrainz.org'




// labels
MERGE (release_83a9081b75b8)-[:HAS_LABEL]->(label_14e1ddfd5946)


// tracks
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_1033de3344b4)
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_73cb023ee36f)
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_5511bfb80db5)
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'B1', sequence: 4}]->(perf_2713cd9b018a)
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'B2', sequence: 5}]->(perf_f563c986bab7)
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'B3', sequence: 6}]->(perf_733b8754a19a)
MERGE (release_83a9081b75b8)-[:HAS_TRACK {name: 'B4', sequence: 7}]->(perf_b0e05d4bd99d)


// place nodes

MERGE (place_569fa8b97644:Place{ uuid: '1165ef7d-371c-4e03-98db-569fa8b97644' })
SET place_569fa8b97644.name = 'Van Gelder Studio'
SET place_569fa8b97644.source = 'musicbrainz.org'


// place relationships
MERGE (perf_1033de3344b4)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)
MERGE (perf_73cb023ee36f)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)
MERGE (perf_5511bfb80db5)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)
MERGE (perf_2713cd9b018a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)
MERGE (perf_f563c986bab7)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)
MERGE (perf_733b8754a19a)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)
MERGE (perf_b0e05d4bd99d)-[:HAS_PLACE { type: 'recorded at', begin_date: '1963-11-08', end_date: '1963-11-08' }]->(place_569fa8b97644)

MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_1033de3344b4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_1033de3344b4)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_1033de3344b4)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_1033de3344b4)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_1033de3344b4)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_1033de3344b4)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_73cb023ee36f)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_73cb023ee36f)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_73cb023ee36f)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_73cb023ee36f)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_73cb023ee36f)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_73cb023ee36f)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_5511bfb80db5)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_5511bfb80db5)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_5511bfb80db5)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_5511bfb80db5)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_5511bfb80db5)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_5511bfb80db5)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_2713cd9b018a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_2713cd9b018a)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_2713cd9b018a)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2713cd9b018a)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_2713cd9b018a)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_2713cd9b018a)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_f563c986bab7)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_f563c986bab7)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_f563c986bab7)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f563c986bab7)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_f563c986bab7)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_f563c986bab7)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_733b8754a19a)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_733b8754a19a)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_733b8754a19a)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_733b8754a19a)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_733b8754a19a)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_733b8754a19a)
MERGE (person_ff9017878cdd)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b0e05d4bd99d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b0e05d4bd99d)
MERGE (person_9ee947b4ce37)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_b0e05d4bd99d)
MERGE (person_2584a0b30ec9)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b0e05d4bd99d)
MERGE (person_317b31f6c035)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_b0e05d4bd99d)
MERGE (person_05d508e09a73)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b0e05d4bd99d)



"""
)