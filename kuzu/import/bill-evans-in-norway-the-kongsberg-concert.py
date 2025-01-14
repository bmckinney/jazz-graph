
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_c3124b6fd166:Release{ uuid: '4a8cbd7d-78aa-4739-b7b3-c3124b6fd166' })
SET release_c3124b6fd166.name = 'Bill Evans in Norway - The Kongsberg Concert'
SET release_c3124b6fd166.date = '2024'
SET release_c3124b6fd166.format = 'CD'
SET release_c3124b6fd166.discode = '5990447'
SET release_c3124b6fd166.discogs = 'https://www.discogs.com/release/32144328'
SET release_c3124b6fd166.musicbrainz = 'http://musicbrainz.org/release/4a8cbd7d-78aa-4739-b7b3-c3124b6fd166'
SET release_c3124b6fd166.source = 'musicbrainz.org'


MERGE (person_c2c10eb1981c:Person{ uuid: '3203d20c-9e96-4e8b-a51e-c2c10eb1981c' }) 
SET person_c2c10eb1981c.name = 'Eddie Gomez'
SET person_c2c10eb1981c.gender = 'Male'
SET person_c2c10eb1981c.disambiguation = 'jazz double bassist'
SET person_c2c10eb1981c.country = 'PR'
SET person_c2c10eb1981c.allmusic = 'https://www.allmusic.com/artist/mn0000794244'
SET person_c2c10eb1981c.discogs = 'https://www.discogs.com/artist/274957'
SET person_c2c10eb1981c.viaf = 'http://viaf.org/viaf/85696187'
SET person_c2c10eb1981c.wikidata = 'https://www.wikidata.org/wiki/Q948613'
SET person_c2c10eb1981c.databases = ['http://id.loc.gov/authorities/names/n81146635', 'https://adp.library.ucsb.edu/names/318173', 'https://catalogue.bnf.fr/ark:/12148/cb13894594b', 'https://d-nb.info/gnd/134387686', 'http://snaccooperative.org/ark:/99166/w6wr3rcn', 'https://www.worldcat.org/identities/lccn-n81146635']
SET person_c2c10eb1981c.musicbrainz = 'https://musicbrainz.org/artist/3203d20c-9e96-4e8b-a51e-c2c10eb1981c'
SET person_c2c10eb1981c.isni_list = ['http://isni.org/isni/0000000114507070']
SET person_c2c10eb1981c.source = 'musicbrainz.org'


MERGE (person_332987bbd937:Person{ uuid: 'a8104b28-fc75-4563-9e1a-332987bbd937' }) 
SET person_332987bbd937.name = 'Marty Morell'
SET person_332987bbd937.gender = 'Male'
SET person_332987bbd937.disambiguation = 'drums'
SET person_332987bbd937.country = 'US'
SET person_332987bbd937.allmusic = 'https://www.allmusic.com/artist/mn0000371398'
SET person_332987bbd937.discogs = 'https://www.discogs.com/artist/307623'
SET person_332987bbd937.imdb = 'https://www.imdb.com/name/nm9443922/'
SET person_332987bbd937.viaf = 'http://viaf.org/viaf/119842457'
SET person_332987bbd937.wikidata = 'https://www.wikidata.org/wiki/Q962885'
SET person_332987bbd937.databases = ['http://id.loc.gov/authorities/names/n91083273', 'https://catalogue.bnf.fr/ark:/12148/cb138976992', 'https://d-nb.info/gnd/134805585', 'https://rateyourmusic.com/artist/marty_morell', 'https://www.worldcat.org/identities/lccn-n91083273']
SET person_332987bbd937.musicbrainz = 'https://musicbrainz.org/artist/a8104b28-fc75-4563-9e1a-332987bbd937'
SET person_332987bbd937.isni_list = ['http://isni.org/isni/000000008666019X']
SET person_332987bbd937.source = 'musicbrainz.org'


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
SET person_6c57b03a4e36.databases = ['http://id.loc.gov/authorities/names/n81147281', 'https://adp.library.ucsb.edu/names/203037', 'https://castalbums.org/people/Bill-Evans-1/11965', 'https://catalogue.bnf.fr/ark:/12148/cb13893736g', 'https://d-nb.info/gnd/137724519', 'https://id.oclc.org/worldcat/entity/E39PBJf8xcCTxHr9htXyQxwpyd', 'https://musicmoz.org/Bands_and_Artists/E/Evans,_Bill/', 'http://snaccooperative.org/ark:/99166/w6v411q5', 'https://openlibrary.org/authors/OL6591650A', 'https://openlibrary.org/authors/OL7514955A', 'https://operabase.com/a2242729', 'https://rateyourmusic.com/artist/bill_evans', 'https://www.dramonline.org/composers/evans-bill', 'https://www.librarything.com/author/evansbill-1-5203912', 'https://www.musik-sammler.de/artist/175764/', 'https://www.muziekweb.nl/Link/M00000255981/POPULAR/', 'https://www.themoviedb.org/person/137953', 'https://www.whosampled.com/Bill-Evans/', 'https://www.worldcat.org/identities/lccn-n81-147281', 'http://www.maniadb.com/artist/117793']
SET person_6c57b03a4e36.musicbrainz = 'https://musicbrainz.org/artist/8247a3f2-3a8e-4256-b322-6c57b03a4e36'
SET person_6c57b03a4e36.isni_list = ['http://isni.org/isni/0000000121261603']
SET person_6c57b03a4e36.source = 'musicbrainz.org'

// labels

MERGE (label_12fa5d542dac:Label{ uuid: '576376e0-8c12-453f-a4e7-12fa5d542dac' })
SET label_12fa5d542dac.name= 'Elemental Music'

// performances

MERGE (perf_d82abfdb265e:Performance{ uuid: 'ee057cca-536d-44e9-ac8f-d82abfdb265e' })
SET perf_d82abfdb265e.name = 'Come Rain or Come Shine'
SET perf_d82abfdb265e.duration = '5:55'
SET perf_d82abfdb265e.source = 'musicbrainz.org'


MERGE (perf_27daedd41413:Performance{ uuid: '4391b257-a4e9-47b4-ab7d-27daedd41413' })
SET perf_27daedd41413.name = 'What Are You Doing the Rest of Your Life?'
SET perf_27daedd41413.duration = '5:39'
SET perf_27daedd41413.source = 'musicbrainz.org'


MERGE (perf_42721156b473:Performance{ uuid: 'ea79d97d-b435-4e55-b6d3-42721156b473' })
SET perf_42721156b473.name = '34 Skidoo'
SET perf_42721156b473.duration = '5:55'
SET perf_42721156b473.source = 'musicbrainz.org'


MERGE (perf_e784c8e6b27f:Performance{ uuid: '8df39294-abb3-445e-912b-e784c8e6b27f' })
SET perf_e784c8e6b27f.name = 'Turn Out the Stars'
SET perf_e784c8e6b27f.duration = '5:12'
SET perf_e784c8e6b27f.source = 'musicbrainz.org'


MERGE (perf_3db3fa0c9998:Performance{ uuid: '12cae967-2e88-477d-92e3-3db3fa0c9998' })
SET perf_3db3fa0c9998.name = 'Autumn Leaves'
SET perf_3db3fa0c9998.duration = '5:49'
SET perf_3db3fa0c9998.source = 'musicbrainz.org'


MERGE (perf_b253c98866d9:Performance{ uuid: '95bc765f-24ea-487f-a6a4-b253c98866d9' })
SET perf_b253c98866d9.name = 'Quiet Now'
SET perf_b253c98866d9.duration = '5:35'
SET perf_b253c98866d9.source = 'musicbrainz.org'


MERGE (perf_d8513170568b:Performance{ uuid: '855af700-1567-42d9-ae85-d8513170568b' })
SET perf_d8513170568b.name = 'So What'
SET perf_d8513170568b.duration = '6:56'
SET perf_d8513170568b.source = 'musicbrainz.org'


MERGE (perf_2ed946bf0f3e:Performance{ uuid: '453be210-1648-47bf-a554-2ed946bf0f3e' })
SET perf_2ed946bf0f3e.name = 'Gloria\\'s Step'
SET perf_2ed946bf0f3e.duration = '4:59'
SET perf_2ed946bf0f3e.source = 'musicbrainz.org'


MERGE (perf_bbdf71eded76:Performance{ uuid: 'd5d9b891-b1a2-461f-bb03-bbdf71eded76' })
SET perf_bbdf71eded76.name = 'Emilly'
SET perf_bbdf71eded76.duration = '5:18'
SET perf_bbdf71eded76.source = 'musicbrainz.org'


MERGE (perf_d566779ad5f4:Performance{ uuid: 'b0ae844b-e97a-4a03-9194-d566779ad5f4' })
SET perf_d566779ad5f4.name = 'Midnight Mood'
SET perf_d566779ad5f4.duration = '6:22'
SET perf_d566779ad5f4.source = 'musicbrainz.org'


MERGE (perf_ec91a530f07b:Performance{ uuid: 'c3c9e666-8186-4c93-8654-ec91a530f07b' })
SET perf_ec91a530f07b.name = 'Who Can\\'t I Turn to?'
SET perf_ec91a530f07b.duration = '6:39'
SET perf_ec91a530f07b.source = 'musicbrainz.org'


MERGE (perf_45021ac40c89:Performance{ uuid: '07f6f2a5-3edd-4080-9d9d-45021ac40c89' })
SET perf_45021ac40c89.name = 'Some Other Time'
SET perf_45021ac40c89.duration = '5:42'
SET perf_45021ac40c89.source = 'musicbrainz.org'


MERGE (perf_77215e77d09b:Performance{ uuid: '5f71c638-fb69-4e4e-be52-77215e77d09b' })
SET perf_77215e77d09b.name = 'Nardis'
SET perf_77215e77d09b.duration = '9:35'
SET perf_77215e77d09b.source = 'musicbrainz.org'




// labels
MERGE (release_c3124b6fd166)-[:HAS_LABEL]->(label_12fa5d542dac)


// tracks
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_d82abfdb265e)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_27daedd41413)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_42721156b473)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_e784c8e6b27f)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_3db3fa0c9998)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_b253c98866d9)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_d8513170568b)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_2ed946bf0f3e)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_bbdf71eded76)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_d566779ad5f4)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '11', sequence: 11}]->(perf_ec91a530f07b)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '12', sequence: 12}]->(perf_45021ac40c89)
MERGE (release_c3124b6fd166)-[:HAS_TRACK {name: '13', sequence: 13}]->(perf_77215e77d09b)

// works

MERGE (person_796faa298651:Person{ uuid: '32434ee8-8f04-4c95-a963-796faa298651' }) 
SET person_796faa298651.name = 'Alan Bergman'
SET person_796faa298651.gender = 'Male'
SET person_796faa298651.disambiguation = 'American lyricist'
SET person_796faa298651.country = 'US'
SET person_796faa298651.allmusic = 'https://www.allmusic.com/artist/mn0000622418'
SET person_796faa298651.discogs = 'https://www.discogs.com/artist/555781'
SET person_796faa298651.imdb = 'https://www.imdb.com/name/nm0074732/'
SET person_796faa298651.viaf = 'http://viaf.org/viaf/121923192'
SET person_796faa298651.wikidata = 'https://www.wikidata.org/wiki/Q1857066'
SET person_796faa298651.databases = ['http://id.loc.gov/authorities/names/n83156022', 'https://adp.library.ucsb.edu/names/104319', 'https://catalogue.bnf.fr/ark:/12148/cb140086489', 'https://d-nb.info/gnd/134764730', 'http://snaccooperative.org/ark:/99166/w6gh9td2', 'https://rateyourmusic.com/artist/alan_bergman', 'https://www.ibdb.com/person.php?id=12751', 'https://www.worldcat.org/identities/lccn-n83156022/']
SET person_796faa298651.musicbrainz = 'https://musicbrainz.org/artist/32434ee8-8f04-4c95-a963-796faa298651'
SET person_796faa298651.isni_list = ['http://isni.org/isni/0000000080463531']
SET person_796faa298651.source = 'musicbrainz.org'


MERGE (person_fd8990977d00:Person{ uuid: '0a2bd34d-0cf9-4e34-9854-fd8990977d00' }) 
SET person_fd8990977d00.name = 'Marilyn Bergman'
SET person_fd8990977d00.gender = 'Female'
SET person_fd8990977d00.country = 'US'
SET person_fd8990977d00.allmusic = 'https://www.allmusic.com/artist/mn0000222469'
SET person_fd8990977d00.discogs = 'https://www.discogs.com/artist/555780'
SET person_fd8990977d00.discogs = 'https://www.discogs.com/artist/917384'
SET person_fd8990977d00.imdb = 'https://www.imdb.com/name/nm0004750/'
SET person_fd8990977d00.viaf = 'http://viaf.org/viaf/85752565'
SET person_fd8990977d00.wikidata = 'https://www.wikidata.org/wiki/Q442879'
SET person_fd8990977d00.databases = ['http://id.loc.gov/authorities/names/n83156023', 'https://catalogue.bnf.fr/ark:/12148/cb14008650v', 'https://d-nb.info/gnd/134764749', 'https://ibdb.com/person.php?id=12752', 'https://nla.gov.au/nla.party-1257902', 'https://rateyourmusic.com/artist/marilyn_bergman', 'https://www.worldcat.org/identities/lccn-n83156023/']
SET person_fd8990977d00.musicbrainz = 'https://musicbrainz.org/artist/0a2bd34d-0cf9-4e34-9854-fd8990977d00'
SET person_fd8990977d00.isni_list = ['http://isni.org/isni/0000000114767091']
SET person_fd8990977d00.source = 'musicbrainz.org'


MERGE (person_635888a66dea:Person{ uuid: '114ec00a-c6cf-42cf-af03-635888a66dea' }) 
SET person_635888a66dea.name = 'Joseph Kosma'
SET person_635888a66dea.gender = 'Male'
SET person_635888a66dea.disambiguation = 'composer'
SET person_635888a66dea.country = 'FR'
SET person_635888a66dea.allmusic = 'https://www.allmusic.com/artist/mn0002449817'
SET person_635888a66dea.discogs = 'https://www.discogs.com/artist/445911'
SET person_635888a66dea.imdb = 'https://www.imdb.com/name/nm0006158/'
SET person_635888a66dea.viaf = 'http://viaf.org/viaf/10033644'
SET person_635888a66dea.wikidata = 'https://www.wikidata.org/wiki/Q213661'
SET person_635888a66dea.databases = ['http://id.loc.gov/authorities/names/n85369395', 'https://adp.library.ucsb.edu/names/322793', 'https://catalogue.bnf.fr/ark:/12148/cb138961205', 'https://d-nb.info/gnd/118898728', 'http://snaccooperative.org/ark:/99166/w6kq12n2', 'https://nla.gov.au/nla.party-1107135', 'https://openlibrary.org/works/OL4787988A', 'https://www.worldcat.org/identities/lccn-n85369395']
SET person_635888a66dea.musicbrainz = 'https://musicbrainz.org/artist/114ec00a-c6cf-42cf-af03-635888a66dea'
SET person_635888a66dea.isni_list = ['http://isni.org/isni/000000036849154X']
SET person_635888a66dea.source = 'musicbrainz.org'


MERGE (person_e3bdc47b2f0b:Person{ uuid: '1ba5e790-ab00-4acc-9083-e3bdc47b2f0b' }) 
SET person_e3bdc47b2f0b.name = 'Leslie Bricusse'
SET person_e3bdc47b2f0b.gender = 'Male'
SET person_e3bdc47b2f0b.country = 'GB'
SET person_e3bdc47b2f0b.allmusic = 'https://www.allmusic.com/artist/mn0000250699'
SET person_e3bdc47b2f0b.discogs = 'https://www.discogs.com/artist/283101'
SET person_e3bdc47b2f0b.imdb = 'https://www.imdb.com/name/nm0108634/'
SET person_e3bdc47b2f0b.viaf = 'http://viaf.org/viaf/197322435'
SET person_e3bdc47b2f0b.wikidata = 'https://www.wikidata.org/wiki/Q1305608'
SET person_e3bdc47b2f0b.databases = ['http://id.loc.gov/authorities/names/n86031627', 'https://catalogue.bnf.fr/ark:/12148/cb13891847x', 'https://d-nb.info/gnd/132580217', 'https://ibdb.com/person.php?id=11429', 'http://snaccooperative.org/ark:/99166/w6c00kxc', 'https://nla.gov.au/nla.party-795929', 'http://soundtrackcollector.com/composer/262/', 'https://rateyourmusic.com/artist/leslie_bricusse', 'https://www.worldcat.org/identities/lccn-n86031627']
SET person_e3bdc47b2f0b.musicbrainz = 'https://musicbrainz.org/artist/1ba5e790-ab00-4acc-9083-e3bdc47b2f0b'
SET person_e3bdc47b2f0b.isni_list = ['http://isni.org/isni/0000000109218135']
SET person_e3bdc47b2f0b.source = 'musicbrainz.org'


MERGE (person_e7709a8a199c:Person{ uuid: '46c4e7e3-445b-4f45-8cc9-e7709a8a199c' }) 
SET person_e7709a8a199c.name = 'Denny Zeitlin'
SET person_e7709a8a199c.gender = 'Male'
SET person_e7709a8a199c.country = 'US'
SET person_e7709a8a199c.allmusic = 'https://www.allmusic.com/artist/mn0000821624'
SET person_e7709a8a199c.discogs = 'https://www.discogs.com/artist/335785'
SET person_e7709a8a199c.imdb = 'https://www.imdb.com/name/nm0954419/'
SET person_e7709a8a199c.viaf = 'http://viaf.org/viaf/100847858'
SET person_e7709a8a199c.wikidata = 'https://www.wikidata.org/wiki/Q1189689'
SET person_e7709a8a199c.databases = ['http://id.loc.gov/authorities/names/n91129148', 'https://catalogue.bnf.fr/ark:/12148/cb139014025', 'https://d-nb.info/gnd/134564146', 'https://www.worldcat.org/identities/lccn-n91129148']
SET person_e7709a8a199c.musicbrainz = 'https://musicbrainz.org/artist/46c4e7e3-445b-4f45-8cc9-e7709a8a199c'
SET person_e7709a8a199c.isni_list = ['http://isni.org/isni/0000000078398611']
SET person_e7709a8a199c.source = 'musicbrainz.org'


MERGE (person_8a3b4f0f3f79:Person{ uuid: '5fd5aa4f-02b0-4747-ad4c-8a3b4f0f3f79' }) 
SET person_8a3b4f0f3f79.name = 'Sammy Cahn'
SET person_8a3b4f0f3f79.gender = 'Male'
SET person_8a3b4f0f3f79.country = 'US'
SET person_8a3b4f0f3f79.allmusic = 'https://www.allmusic.com/artist/mn0000987625'
SET person_8a3b4f0f3f79.discogs = 'https://www.discogs.com/artist/255312'
SET person_8a3b4f0f3f79.imdb = 'https://www.imdb.com/name/nm0005991/'
SET person_8a3b4f0f3f79.viaf = 'http://viaf.org/viaf/209945'
SET person_8a3b4f0f3f79.wikidata = 'https://www.wikidata.org/wiki/Q470040'
SET person_8a3b4f0f3f79.databases = ['http://id.loc.gov/authorities/names/n82096094', 'https://adp.library.ucsb.edu/names/103731', 'https://catalogue.bnf.fr/ark:/12148/cb14025723x', 'https://d-nb.info/gnd/124800823', 'http://snaccooperative.org/ark:/99166/w6zs2v3w', 'https://rateyourmusic.com/artist/sammy_cahn', 'https://www.ibdb.com/person.php?id=11268', 'https://www.worldcat.org/identities/lccn-n82096094/']
SET person_8a3b4f0f3f79.musicbrainz = 'https://musicbrainz.org/artist/5fd5aa4f-02b0-4747-ad4c-8a3b4f0f3f79'
SET person_8a3b4f0f3f79.isni_list = ['http://isni.org/isni/0000000080796256']
SET person_8a3b4f0f3f79.source = 'musicbrainz.org'


MERGE (person_2b3e7beaf00a:Person{ uuid: 'b342d50e-401c-4c77-b7e4-2b3e7beaf00a' }) 
SET person_2b3e7beaf00a.name = 'Johnny Mercer'
SET person_2b3e7beaf00a.gender = 'Male'
SET person_2b3e7beaf00a.country = 'US'
SET person_2b3e7beaf00a.allmusic = 'https://www.allmusic.com/artist/mn0000244406'
SET person_2b3e7beaf00a.bbc = 'https://www.bbc.co.uk/music/artists/b342d50e-401c-4c77-b7e4-2b3e7beaf00a'
SET person_2b3e7beaf00a.discogs = 'https://www.discogs.com/artist/164574'
SET person_2b3e7beaf00a.imdb = 'https://www.imdb.com/name/nm0006197/'
SET person_2b3e7beaf00a.viaf = 'http://viaf.org/viaf/79167222'
SET person_2b3e7beaf00a.wikidata = 'https://www.wikidata.org/wiki/Q363698'
SET person_2b3e7beaf00a.databases = ['http://id.loc.gov/authorities/names/n82078485', 'https://adp.library.ucsb.edu/names/103688', 'https://catalogue.bnf.fr/ark:/12148/cb138974071', 'https://d-nb.info/gnd/118801031', 'http://snaccooperative.org/ark:/99166/w65140xb', 'https://nla.gov.au/nla.party-1213050', 'http://soundtrackcollector.com/composer/3036/', 'https://rateyourmusic.com/artist/johnny_mercer', 'https://www.ibdb.com/person.php?id=12137', 'https://www.worldcat.org/identities/lccn-n82078485/']
SET person_2b3e7beaf00a.musicbrainz = 'https://musicbrainz.org/artist/b342d50e-401c-4c77-b7e4-2b3e7beaf00a'
SET person_2b3e7beaf00a.isni_list = ['http://isni.org/isni/0000000120183877']
SET person_2b3e7beaf00a.source = 'musicbrainz.org'


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
SET person_323e6ce46c2a.databases = ['http://id.loc.gov/authorities/names/n50035608', 'http://musicmoz.org/Bands_and_Artists/D/Davis,_Miles/', 'https://catalogue.bnf.fr/ark:/12148/cb13893030g', 'https://d-nb.info/gnd/118524046', 'http://snaccooperative.org/ark:/99166/w68k7wq0', 'https://openlibrary.org/works/OL4359245A', 'https://rateyourmusic.com/artist/miles_davis', 'https://www.45cat.com/artist/miles-davis', 'https://www.45worlds.com/78rpm/artist/miles-davis', 'https://www.45worlds.com/cdalbum/artist/miles-davis', 'https://www.45worlds.com/live/artist/miles-davis', 'https://www.45worlds.com/tape/artist/miles-davis', 'https://www.45worlds.com/vinyl/artist/miles-davis', 'https://www.muziekweb.nl/Link/M00000286446/', 'https://www.worldcat.org/identities/lccn-n50035608']
SET person_323e6ce46c2a.musicbrainz = 'https://musicbrainz.org/artist/561d854a-6a28-4aa7-8c99-323e6ce46c2a'
SET person_323e6ce46c2a.isni_list = ['http://isni.org/isni/000000012144707X']
SET person_323e6ce46c2a.source = 'musicbrainz.org'


MERGE (person_45ce45592a10:Person{ uuid: '831694b4-19cd-499e-87ea-45ce45592a10' }) 
SET person_45ce45592a10.name = 'Ben Raleigh'
SET person_45ce45592a10.gender = 'Male'
SET person_45ce45592a10.country = 'US'
SET person_45ce45592a10.allmusic = 'https://www.allmusic.com/artist/mn0000165239'
SET person_45ce45592a10.discogs = 'https://www.discogs.com/artist/638537'
SET person_45ce45592a10.imdb = 'https://www.imdb.com/name/nm0707673/'
SET person_45ce45592a10.wikidata = 'https://www.wikidata.org/wiki/Q4886326'
SET person_45ce45592a10.databases = ['https://adp.library.ucsb.edu/names/109543', 'https://rateyourmusic.com/artist/ben_raleigh']
SET person_45ce45592a10.musicbrainz = 'https://musicbrainz.org/artist/831694b4-19cd-499e-87ea-45ce45592a10'
SET person_45ce45592a10.isni_list = ['http://isni.org/isni/0000000063030064']
SET person_45ce45592a10.source = 'musicbrainz.org'


MERGE (person_6a465a5b32f3:Person{ uuid: '95c95dee-0dbc-4d5f-a428-6a465a5b32f3' }) 
SET person_6a465a5b32f3.name = 'Johnny Mandel'
SET person_6a465a5b32f3.gender = 'Male'
SET person_6a465a5b32f3.disambiguation = 'American composer and arranger'
SET person_6a465a5b32f3.country = 'US'
SET person_6a465a5b32f3.allmusic = 'https://www.allmusic.com/artist/mn0000202554'
SET person_6a465a5b32f3.discogs = 'https://www.discogs.com/artist/263472'
SET person_6a465a5b32f3.imdb = 'https://www.imdb.com/name/nm0006184/'
SET person_6a465a5b32f3.viaf = 'http://viaf.org/viaf/102341215'
SET person_6a465a5b32f3.wikidata = 'https://www.wikidata.org/wiki/Q975609'
SET person_6a465a5b32f3.databases = ['http://id.loc.gov/authorities/names/no90017628', 'https://catalogue.bnf.fr/ark:/12148/cb138970235', 'https://d-nb.info/gnd/134698541', 'http://snaccooperative.org/ark:/99166/w6ht2p6g', 'https://rateyourmusic.com/artist/johnny_mandel', 'https://www.ibdb.com/person.php?id=77510', 'https://www.worldcat.org/identities/lccn-no90017628/']
SET person_6a465a5b32f3.musicbrainz = 'https://musicbrainz.org/artist/95c95dee-0dbc-4d5f-a428-6a465a5b32f3'
SET person_6a465a5b32f3.isni_list = ['http://isni.org/isni/0000000079804298']
SET person_6a465a5b32f3.source = 'musicbrainz.org'


MERGE (person_5b4c60179611:Person{ uuid: 'dfe8c9e1-10c0-49ab-a07a-5b4c60179611' }) 
SET person_5b4c60179611.name = 'Joe Zawinul'
SET person_5b4c60179611.gender = 'Male'
SET person_5b4c60179611.disambiguation = 'jazz and fusion keyboard player'
SET person_5b4c60179611.country = 'AT'
SET person_5b4c60179611.allmusic = 'https://www.allmusic.com/artist/mn0000176859'
SET person_5b4c60179611.bbc = 'https://www.bbc.co.uk/music/artists/dfe8c9e1-10c0-49ab-a07a-5b4c60179611'
SET person_5b4c60179611.discogs = 'https://www.discogs.com/artist/56960'
SET person_5b4c60179611.imdb = 'https://www.imdb.com/name/nm1056442/'
SET person_5b4c60179611.viaf = 'http://viaf.org/viaf/119338362'
SET person_5b4c60179611.wikidata = 'https://www.wikidata.org/wiki/Q44767'
SET person_5b4c60179611.databases = ['http://id.loc.gov/authorities/names/no88003763', 'https://catalogue.bnf.fr/ark:/12148/cb13901391b', 'https://d-nb.info/gnd/119286386', 'http://snaccooperative.org/ark:/99166/w6p87996', 'https://nla.gov.au/nla.party-1076064', 'https://rateyourmusic.com/artist/joe-zawinul', 'https://www.progarchives.com/artist.asp?id=4407', 'https://www.worldcat.org/identities/lccn-no88003763']
SET person_5b4c60179611.musicbrainz = 'https://musicbrainz.org/artist/dfe8c9e1-10c0-49ab-a07a-5b4c60179611'
SET person_5b4c60179611.isni_list = ['http://isni.org/isni/0000000117008912']
SET person_5b4c60179611.source = 'musicbrainz.org'


MERGE (person_3fbbe73d09b4:Person{ uuid: '1b3a1e49-2494-441c-9818-3fbbe73d09b4' }) 
SET person_3fbbe73d09b4.name = 'Jule Styne'
SET person_3fbbe73d09b4.gender = 'Male'
SET person_3fbbe73d09b4.country = 'GB'
SET person_3fbbe73d09b4.allmusic = 'https://www.allmusic.com/artist/mn0000304458'
SET person_3fbbe73d09b4.discogs = 'https://www.discogs.com/artist/341663'
SET person_3fbbe73d09b4.imdb = 'https://www.imdb.com/name/nm0006312/'
SET person_3fbbe73d09b4.viaf = 'http://viaf.org/viaf/94213715'
SET person_3fbbe73d09b4.wikidata = 'https://www.wikidata.org/wiki/Q587741'
SET person_3fbbe73d09b4.databases = ['http://id.loc.gov/authorities/names/n81120322', 'https://adp.library.ucsb.edu/names/103313', 'https://catalogue.bnf.fr/ark:/12148/cb13900158q', 'https://d-nb.info/gnd/121819604', 'https://ibdb.com/person.php?id=12466', 'http://snaccooperative.org/ark:/99166/w6gb25xj', 'https://nla.gov.au/nla.party-1196551', 'https://openlibrary.org/works/OL575686A', 'https://rateyourmusic.com/artist/jule_styne', 'https://www.worldcat.org/identities/lccn-n81120322/']
SET person_3fbbe73d09b4.musicbrainz = 'https://musicbrainz.org/artist/1b3a1e49-2494-441c-9818-3fbbe73d09b4'
SET person_3fbbe73d09b4.isni_list = ['http://isni.org/isni/0000000114778217']
SET person_3fbbe73d09b4.source = 'musicbrainz.org'


MERGE (person_186f3b5a1ea5:Person{ uuid: '97cc902a-2850-4db8-8218-186f3b5a1ea5' }) 
SET person_186f3b5a1ea5.name = 'Scott LaFaro'
SET person_186f3b5a1ea5.gender = 'Male'
SET person_186f3b5a1ea5.country = 'US'
SET person_186f3b5a1ea5.discogs = 'https://www.discogs.com/artist/272982'
SET person_186f3b5a1ea5.viaf = 'http://viaf.org/viaf/59271653'
SET person_186f3b5a1ea5.wikidata = 'https://www.wikidata.org/wiki/Q707857'
SET person_186f3b5a1ea5.databases = ['http://id.loc.gov/authorities/names/n91048755', 'https://catalogue.bnf.fr/ark:/12148/cb139240413', 'https://d-nb.info/gnd/135323606', 'https://www.worldcat.org/identities/lccn-n91048755']
SET person_186f3b5a1ea5.musicbrainz = 'https://musicbrainz.org/artist/97cc902a-2850-4db8-8218-186f3b5a1ea5'
SET person_186f3b5a1ea5.isni_list = ['http://isni.org/isni/0000000109062089']
SET person_186f3b5a1ea5.source = 'musicbrainz.org'


MERGE (person_c1c0dfb12f18:Person{ uuid: '179333bd-7c05-4050-8d06-c1c0dfb12f18' }) 
SET person_c1c0dfb12f18.name = 'Jacques Prévert'
SET person_c1c0dfb12f18.gender = 'Male'
SET person_c1c0dfb12f18.country = 'FR'
SET person_c1c0dfb12f18.allmusic = 'https://www.allmusic.com/artist/mn0000121861'
SET person_c1c0dfb12f18.discogs = 'https://www.discogs.com/artist/583803'
SET person_c1c0dfb12f18.imdb = 'https://www.imdb.com/name/nm0699535/'
SET person_c1c0dfb12f18.viaf = 'http://viaf.org/viaf/76321578'
SET person_c1c0dfb12f18.wikidata = 'https://www.wikidata.org/wiki/Q165274'
SET person_c1c0dfb12f18.databases = ['http://id.loc.gov/authorities/names/n79054068', 'https://adp.library.ucsb.edu/names/102352', 'https://catalogue.bnf.fr/ark:/12148/cb119206049', 'https://d-nb.info/gnd/118596446', 'http://snaccooperative.org/ark:/99166/w6639mq0', 'https://nla.gov.au/nla.party-1228478', 'https://openlibrary.org/works/OL129281A', 'https://www.worldcat.org/identities/lccn-n79054068/']
SET person_c1c0dfb12f18.musicbrainz = 'https://musicbrainz.org/artist/179333bd-7c05-4050-8d06-c1c0dfb12f18'
SET person_c1c0dfb12f18.isni_list = ['http://isni.org/isni/000000012140044X']
SET person_c1c0dfb12f18.source = 'musicbrainz.org'


MERGE (person_aefd1ad8de01:Person{ uuid: '9a93190b-3e24-4586-bc10-aefd1ad8de01' }) 
SET person_aefd1ad8de01.name = 'Anthony Newley'
SET person_aefd1ad8de01.gender = 'Male'
SET person_aefd1ad8de01.disambiguation = 'English actor, singer, songwriter, and filmmaker'
SET person_aefd1ad8de01.allmusic = 'https://www.allmusic.com/artist/mn0000754219'
SET person_aefd1ad8de01.bbc = 'https://www.bbc.co.uk/music/artists/9a93190b-3e24-4586-bc10-aefd1ad8de01'
SET person_aefd1ad8de01.discogs = 'https://www.discogs.com/artist/170757'
SET person_aefd1ad8de01.imdb = 'https://www.imdb.com/name/nm0627969/'
SET person_aefd1ad8de01.viaf = 'http://viaf.org/viaf/34647429'
SET person_aefd1ad8de01.wikidata = 'https://www.wikidata.org/wiki/Q573709'
SET person_aefd1ad8de01.databases = ['http://id.loc.gov/authorities/names/n88051157', 'https://catalogue.bnf.fr/ark:/12148/cb13938558c', 'https://d-nb.info/gnd/124865399', 'https://ibdb.com/person.php?id=4204', 'https://nla.gov.au/nla.party-1105669', 'https://rateyourmusic.com/artist/anthony_newley', 'https://www.worldcat.org/identities/lccn-n88051157']
SET person_aefd1ad8de01.musicbrainz = 'https://musicbrainz.org/artist/9a93190b-3e24-4586-bc10-aefd1ad8de01'
SET person_aefd1ad8de01.isni_list = ['http://isni.org/isni/0000000063096522']
SET person_aefd1ad8de01.source = 'musicbrainz.org'


MERGE (person_dc8a236d06b3:Person{ uuid: '2c330f54-9245-488b-b678-dc8a236d06b3' }) 
SET person_dc8a236d06b3.name = 'Michel Legrand'
SET person_dc8a236d06b3.gender = 'Male'
SET person_dc8a236d06b3.country = 'FR'
SET person_dc8a236d06b3.allmusic = 'https://www.allmusic.com/artist/mn0000401066'
SET person_dc8a236d06b3.discogs = 'https://www.discogs.com/artist/84236'
SET person_dc8a236d06b3.imdb = 'https://www.imdb.com/name/nm0006166/'
SET person_dc8a236d06b3.viaf = 'http://viaf.org/viaf/152160636'
SET person_dc8a236d06b3.wikidata = 'https://www.wikidata.org/wiki/Q313281'
SET person_dc8a236d06b3.databases = ['http://id.loc.gov/authorities/names/n82004250', 'https://adp.library.ucsb.edu/names/205750', 'https://catalogue.bnf.fr/ark:/12148/cb138964967', 'https://d-nb.info/gnd/130482552', 'https://ibdb.com/person.php?id=12036', 'http://snaccooperative.org/ark:/99166/w6dr2v6x', 'https://nla.gov.au/nla.party-1077026', 'https://rateyourmusic.com/artist/michel_legrand', 'https://www.muziekweb.nl/Link/M00000240785/', 'https://www.worldcat.org/identities/lccn-n82004250']
SET person_dc8a236d06b3.musicbrainz = 'https://musicbrainz.org/artist/2c330f54-9245-488b-b678-dc8a236d06b3'
SET person_dc8a236d06b3.isni_list = ['http://isni.org/isni/0000000121867242']
SET person_dc8a236d06b3.source = 'musicbrainz.org'


MERGE (person_376736bb6cde:Person{ uuid: '3508f3fd-3b18-493c-a362-376736bb6cde' }) 
SET person_376736bb6cde.name = 'Harold Arlen'
SET person_376736bb6cde.gender = 'Male'
SET person_376736bb6cde.country = 'US'
SET person_376736bb6cde.allmusic = 'https://www.allmusic.com/artist/mn0000060306'
SET person_376736bb6cde.discogs = 'https://www.discogs.com/artist/301975'
SET person_376736bb6cde.imdb = 'https://www.imdb.com/name/nm0002182/'
SET person_376736bb6cde.viaf = 'http://viaf.org/viaf/59268723'
SET person_376736bb6cde.wikidata = 'https://www.wikidata.org/wiki/Q448644'
SET person_376736bb6cde.databases = ['http://id.loc.gov/authorities/names/n82155108', 'https://adp.library.ucsb.edu/names/103935', 'https://catalogue.bnf.fr/ark:/12148/cb13890872w', 'https://d-nb.info/gnd/119401193', 'https://ibdb.com/person.php?id=11319', 'https://id.ndl.go.jp/auth/ndlna/001155326', 'http://snaccooperative.org/ark:/99166/w6z899sq', 'https://nla.gov.au/anbd.aut-an35107300', 'https://openlibrary.org/works/OL342313A', 'https://rateyourmusic.com/artist/harold_arlen', 'https://www.worldcat.org/identities/containsVIAFID/59268723']
SET person_376736bb6cde.musicbrainz = 'https://musicbrainz.org/artist/3508f3fd-3b18-493c-a362-376736bb6cde'
SET person_376736bb6cde.isni_list = ['http://isni.org/isni/0000000083863098', 'http://isni.org/isni/0000000368517543']
SET person_376736bb6cde.source = 'musicbrainz.org'


MERGE (work_f5fee178e4a5:Work{ uuid: 'aae21579-5fab-3d22-90a4-f5fee178e4a5' })
SET work_f5fee178e4a5.name = 'Nardis'
SET work_f5fee178e4a5.type = 'Song'
SET work_f5fee178e4a5.source = 'musicbrainz.org'


MERGE (work_5e457b3aafed:Work{ uuid: '94129263-c392-3a5c-98bd-5e457b3aafed' })
SET work_5e457b3aafed.name = 'Turn Out the Stars'
SET work_5e457b3aafed.type = 'Song'
SET work_5e457b3aafed.musicbrainz = 'https://musicbrainz.org/work/94129263-c392-3a5c-98bd-5e457b3aafed'
SET work_5e457b3aafed.source = 'musicbrainz.org'


MERGE (work_b8c356eb1fe5:Work{ uuid: '0acc08e7-f020-33b0-b264-b8c356eb1fe5' })
SET work_b8c356eb1fe5.name = 'What Are You Doing the Rest of Your Life?'
SET work_b8c356eb1fe5.iswc = 'T-070.202.117-7'
SET work_b8c356eb1fe5.type = 'Song'
SET work_b8c356eb1fe5.wikidata = 'https://www.wikidata.org/wiki/Q3567625'
SET work_b8c356eb1fe5.musicbrainz = 'https://musicbrainz.org/work/0acc08e7-f020-33b0-b264-b8c356eb1fe5'
SET work_b8c356eb1fe5.source = 'musicbrainz.org'


MERGE (work_9626b6f1e2ea:Work{ uuid: '7fa1bfa2-ce99-3236-9859-9626b6f1e2ea' })
SET work_9626b6f1e2ea.name = 'Who Can I Turn To (When Nobody Needs Me)'
SET work_9626b6f1e2ea.iswc = 'T-071.017.448-3'
SET work_9626b6f1e2ea.type = 'Song'
SET work_9626b6f1e2ea.wikidata = 'https://www.wikidata.org/wiki/Q3567838'
SET work_9626b6f1e2ea.musicbrainz = 'https://musicbrainz.org/work/7fa1bfa2-ce99-3236-9859-9626b6f1e2ea'
SET work_9626b6f1e2ea.source = 'musicbrainz.org'


MERGE (work_48f3c62c1d24:Work{ uuid: 'dfb51dff-8e04-313c-adab-48f3c62c1d24' })
SET work_48f3c62c1d24.name = 'Come Rain or Come Shine'
SET work_48f3c62c1d24.iswc = 'T-070.025.551-1'
SET work_48f3c62c1d24.type = 'Song'
SET work_48f3c62c1d24.wikidata = 'https://www.wikidata.org/wiki/Q1113873'
SET work_48f3c62c1d24.musicbrainz = 'https://musicbrainz.org/work/dfb51dff-8e04-313c-adab-48f3c62c1d24'
SET work_48f3c62c1d24.source = 'musicbrainz.org'


MERGE (work_b32daefc9149:Work{ uuid: '52c3bd6b-1937-3cc2-b57c-b32daefc9149' })
SET work_b32daefc9149.name = 'Quiet Now'
SET work_b32daefc9149.iswc = 'T-070.939.948-3'
SET work_b32daefc9149.type = 'Song'
SET work_b32daefc9149.source = 'musicbrainz.org'


MERGE (work_28bd4a322ee4:Work{ uuid: '0eecc4ea-02d0-4444-98f2-28bd4a322ee4' })
SET work_28bd4a322ee4.name = 'Midnight Mood'
SET work_28bd4a322ee4.type = 'Song'
SET work_28bd4a322ee4.tags = ['hard bop', 'jazz']
SET work_28bd4a322ee4.musicbrainz = 'https://musicbrainz.org/work/0eecc4ea-02d0-4444-98f2-28bd4a322ee4'
SET work_28bd4a322ee4.source = 'musicbrainz.org'


MERGE (work_ab793c57c867:Work{ uuid: 'f5974775-edde-40ae-8332-ab793c57c867' })
SET work_ab793c57c867.name = 'Some Other Time'
SET work_ab793c57c867.iswc = 'T-070.136.535-6'
SET work_ab793c57c867.type = 'Song'
SET work_ab793c57c867.musicbrainz = 'https://musicbrainz.org/work/f5974775-edde-40ae-8332-ab793c57c867'
SET work_ab793c57c867.source = 'musicbrainz.org'


MERGE (work_268199324401:Work{ uuid: '048b4b7a-07c4-3e33-959f-268199324401' })
SET work_268199324401.name = 'Autumn Leaves'
SET work_268199324401.iswc = 'T-070.002.297-4'
SET work_268199324401.type = 'Song'
SET work_268199324401.wikidata = 'https://www.wikidata.org/wiki/Q789392'
SET work_268199324401.databases = ['https://d-nb.info/gnd/7590476-7']
SET work_268199324401.musicbrainz = 'https://musicbrainz.org/work/048b4b7a-07c4-3e33-959f-268199324401'
SET work_268199324401.source = 'musicbrainz.org'


MERGE (work_3a7d6599a72e:Work{ uuid: '2fafd730-423f-342e-b6c7-3a7d6599a72e' })
SET work_3a7d6599a72e.name = 'So What'
SET work_3a7d6599a72e.iswc = 'T-073.092.797-5'
SET work_3a7d6599a72e.type = 'Song'
SET work_3a7d6599a72e.wikidata = 'https://www.wikidata.org/wiki/Q919291'
SET work_3a7d6599a72e.musicbrainz = 'https://musicbrainz.org/work/2fafd730-423f-342e-b6c7-3a7d6599a72e'
SET work_3a7d6599a72e.source = 'musicbrainz.org'


MERGE (work_41ca3eb738ab:Work{ uuid: 'ad93f2d2-2bc9-4d3d-9872-41ca3eb738ab' })
SET work_41ca3eb738ab.name = '34 Skidoo'
SET work_41ca3eb738ab.type = 'Song'
SET work_41ca3eb738ab.source = 'musicbrainz.org'


MERGE (work_17431367605f:Work{ uuid: '8ab097b6-0129-46bc-ac04-17431367605f' })
SET work_17431367605f.name = 'Gloria’s Step'
SET work_17431367605f.iswc = 'T-073.110.490-7'
SET work_17431367605f.source = 'musicbrainz.org'


MERGE (work_e302f434babf:Work{ uuid: 'e5951a28-d51c-3a0f-977e-e302f434babf' })
SET work_e302f434babf.name = 'Emily'
SET work_e302f434babf.iswc = 'T-070.050.116-1'
SET work_e302f434babf.type = 'Song'
SET work_e302f434babf.wikidata = 'https://www.wikidata.org/wiki/Q5372027'
SET work_e302f434babf.musicbrainz = 'https://musicbrainz.org/work/e5951a28-d51c-3a0f-977e-e302f434babf'
SET work_e302f434babf.source = 'musicbrainz.org'



// performances of
MERGE (perf_77215e77d09b)-[:PERFORMANCE_OF]->(work_f5fee178e4a5)
MERGE (perf_e784c8e6b27f)-[:PERFORMANCE_OF]->(work_5e457b3aafed)
MERGE (perf_27daedd41413)-[:PERFORMANCE_OF]->(work_b8c356eb1fe5)
MERGE (perf_ec91a530f07b)-[:PERFORMANCE_OF]->(work_9626b6f1e2ea)
MERGE (perf_d82abfdb265e)-[:PERFORMANCE_OF]->(work_48f3c62c1d24)
MERGE (perf_b253c98866d9)-[:PERFORMANCE_OF]->(work_b32daefc9149)
MERGE (perf_d566779ad5f4)-[:PERFORMANCE_OF]->(work_28bd4a322ee4)
MERGE (perf_45021ac40c89)-[:PERFORMANCE_OF]->(work_ab793c57c867)
MERGE (perf_3db3fa0c9998)-[:PERFORMANCE_OF]->(work_268199324401)
MERGE (perf_d8513170568b)-[:PERFORMANCE_OF]->(work_3a7d6599a72e)
MERGE (perf_42721156b473)-[:PERFORMANCE_OF]->(work_41ca3eb738ab)
MERGE (perf_2ed946bf0f3e)-[:PERFORMANCE_OF]->(work_17431367605f)
MERGE (perf_bbdf71eded76)-[:PERFORMANCE_OF]->(work_e302f434babf)


// composers
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_f5fee178e4a5)
MERGE (person_6c57b03a4e36)-[:COMPOSED]->(work_5e457b3aafed)
MERGE (person_dc8a236d06b3)-[:COMPOSED]->(work_b8c356eb1fe5)
MERGE (person_796faa298651)-[:WROTE_LYRICS]->(work_b8c356eb1fe5)
MERGE (person_fd8990977d00)-[:WROTE_LYRICS]->(work_b8c356eb1fe5)
MERGE (person_e3bdc47b2f0b)-[:COMPOSED]->(work_9626b6f1e2ea)
MERGE (person_aefd1ad8de01)-[:COMPOSED]->(work_9626b6f1e2ea)
MERGE (person_376736bb6cde)-[:COMPOSED]->(work_48f3c62c1d24)
MERGE (person_2b3e7beaf00a)-[:WROTE_LYRICS]->(work_48f3c62c1d24)
MERGE (person_e7709a8a199c)-[:COMPOSED]->(work_b32daefc9149)
MERGE (person_45ce45592a10)-[:COMPOSED]->(work_28bd4a322ee4)
MERGE (person_5b4c60179611)-[:COMPOSED]->(work_28bd4a322ee4)
MERGE (person_3fbbe73d09b4)-[:COMPOSED]->(work_ab793c57c867)
MERGE (person_8a3b4f0f3f79)-[:WROTE_LYRICS]->(work_ab793c57c867)
MERGE (person_635888a66dea)-[:COMPOSED]->(work_268199324401)
MERGE (person_c1c0dfb12f18)-[:WROTE_LYRICS]->(work_268199324401)
MERGE (person_323e6ce46c2a)-[:COMPOSED]->(work_3a7d6599a72e)
MERGE (person_6c57b03a4e36)-[:COMPOSED]->(work_41ca3eb738ab)
MERGE (person_186f3b5a1ea5)-[:COMPOSED]->(work_17431367605f)
MERGE (person_6a465a5b32f3)-[:COMPOSED]->(work_e302f434babf)
MERGE (person_2b3e7beaf00a)-[:WROTE_LYRICS]->(work_e302f434babf)

MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d82abfdb265e)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d82abfdb265e)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d82abfdb265e)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_27daedd41413)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_27daedd41413)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_27daedd41413)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_42721156b473)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_42721156b473)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_42721156b473)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e784c8e6b27f)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_e784c8e6b27f)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_e784c8e6b27f)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3db3fa0c9998)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_3db3fa0c9998)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_3db3fa0c9998)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b253c98866d9)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_b253c98866d9)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_b253c98866d9)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d8513170568b)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d8513170568b)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d8513170568b)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_2ed946bf0f3e)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_2ed946bf0f3e)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_2ed946bf0f3e)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bbdf71eded76)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_bbdf71eded76)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_bbdf71eded76)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d566779ad5f4)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d566779ad5f4)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d566779ad5f4)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ec91a530f07b)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_ec91a530f07b)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_ec91a530f07b)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_45021ac40c89)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_45021ac40c89)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_45021ac40c89)
MERGE (person_6c57b03a4e36)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_77215e77d09b)
MERGE (person_c2c10eb1981c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_77215e77d09b)
MERGE (person_332987bbd937)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_77215e77d09b)



"""
)