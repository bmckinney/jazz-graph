
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_0da292e7533f:Release{ uuid: 'd0dc6f54-b5f8-4a68-bfc0-0da292e7533f' })
SET release_0da292e7533f.name = 'Hip Ensemble'
SET release_0da292e7533f.country = 'US'
SET release_0da292e7533f.date = '1971'
SET release_0da292e7533f.format = '12" Vinyl'
SET release_0da292e7533f.discode = 'MRL 313'
SET release_0da292e7533f.discogs = 'https://www.discogs.com/release/5415345'
SET release_0da292e7533f.musicbrainz = 'http://musicbrainz.org/release/d0dc6f54-b5f8-4a68-bfc0-0da292e7533f'
SET release_0da292e7533f.source = 'musicbrainz.org'


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
SET person_6f0a331cc1ca.databases = ['http://id.loc.gov/authorities/names/n81140108', 'https://adp.library.ucsb.edu/names/320530', 'https://catalogue.bnf.fr/ark:/12148/cb13895060w', 'https://d-nb.info/gnd/134400623', 'http://snaccooperative.org/ark:/99166/w6fj33d4', 'https://www.worldcat.org/identities/lccn-n81140108']
SET person_6f0a331cc1ca.musicbrainz = 'https://musicbrainz.org/artist/2c090b57-5e9d-49c5-9b71-6f0a331cc1ca'
SET person_6f0a331cc1ca.isni_list = ['http://isni.org/isni/0000000078266176']
SET person_6f0a331cc1ca.source = 'musicbrainz.org'


MERGE (person_8d0192d5a78b:Person{ uuid: 'b1e7da08-7215-466c-95df-8d0192d5a78b' }) 
SET person_8d0192d5a78b.name = 'George Adams'
SET person_8d0192d5a78b.gender = 'Male'
SET person_8d0192d5a78b.disambiguation = 'jazz musician'
SET person_8d0192d5a78b.country = 'US'
SET person_8d0192d5a78b.allmusic = 'https://www.allmusic.com/artist/mn0000804097'
SET person_8d0192d5a78b.discogs = 'https://www.discogs.com/artist/336123'
SET person_8d0192d5a78b.viaf = 'http://viaf.org/viaf/119607934'
SET person_8d0192d5a78b.wikidata = 'https://www.wikidata.org/wiki/Q1331323'
SET person_8d0192d5a78b.wikipedia = 'https://en.wikipedia.org/wiki/George_Adams_(musician)'
SET person_8d0192d5a78b.databases = ['http://id.loc.gov/authorities/names/n86102049', 'https://catalogue.bnf.fr/ark:/12148/cb13890585d', 'https://d-nb.info/gnd/134310977', 'http://snaccooperative.org/ark:/99166/w6xk8vvn', 'https://www.worldcat.org/identities/lccn-n86102049']
SET person_8d0192d5a78b.musicbrainz = 'https://musicbrainz.org/artist/b1e7da08-7215-466c-95df-8d0192d5a78b'
SET person_8d0192d5a78b.isni_list = ['http://isni.org/isni/0000000084155640']
SET person_8d0192d5a78b.source = 'musicbrainz.org'


MERGE (person_5b6e1e63e268:Person{ uuid: '653eb8e1-19a3-467e-a800-5b6e1e63e268' }) 
SET person_5b6e1e63e268.name = 'Hannibal Marvin Peterson'
SET person_5b6e1e63e268.gender = 'Male'
SET person_5b6e1e63e268.country = 'US'
SET person_5b6e1e63e268.allmusic = 'https://www.allmusic.com/artist/mn0000374683'
SET person_5b6e1e63e268.discogs = 'https://www.discogs.com/artist/272598'
SET person_5b6e1e63e268.viaf = 'http://viaf.org/viaf/24788144'
SET person_5b6e1e63e268.wikidata = 'https://www.wikidata.org/wiki/Q1412862'
SET person_5b6e1e63e268.databases = ['http://id.loc.gov/authorities/names/n91097718', 'https://catalogue.bnf.fr/ark:/12148/cb13949238c', 'https://d-nb.info/gnd/13448343X', 'http://snaccooperative.org/ark:/99166/w63n57m5', 'https://nla.gov.au/nla.party-1107191', 'https://www.worldcat.org/identities/lccn-n91097718']
SET person_5b6e1e63e268.musicbrainz = 'https://musicbrainz.org/artist/653eb8e1-19a3-467e-a800-5b6e1e63e268'
SET person_5b6e1e63e268.isni_list = ['http://isni.org/isni/0000000107980791']
SET person_5b6e1e63e268.source = 'musicbrainz.org'


MERGE (person_6d2978392b0b:Person{ uuid: '27b7a7d2-8237-499f-82c3-6d2978392b0b' }) 
SET person_6d2978392b0b.name = 'Carl Schroeder'
SET person_6d2978392b0b.gender = 'Male'
SET person_6d2978392b0b.disambiguation = 'pianist'
SET person_6d2978392b0b.source = 'musicbrainz.org'

// labels

MERGE (label_2d074f9ea325:Label{ uuid: '32e1b749-523c-43ff-9532-2d074f9ea325' })
SET label_2d074f9ea325.name= 'Mainstream Records'

// performances

MERGE (perf_e8bda766fa41:Performance{ uuid: 'be8c3501-9052-4402-a920-e8bda766fa41' })
SET perf_e8bda766fa41.name = 'Equipoise'
SET perf_e8bda766fa41.duration = '4:18'
SET perf_e8bda766fa41.source = 'musicbrainz.org'


MERGE (perf_3c4bdf2f91cf:Performance{ uuid: 'c598c653-3cf3-4c2d-8576-3c4bdf2f91cf' })
SET perf_3c4bdf2f91cf.name = 'I\\'m So High'
SET perf_3c4bdf2f91cf.duration = '4:10'
SET perf_3c4bdf2f91cf.source = 'musicbrainz.org'


MERGE (perf_0154dc052496:Performance{ uuid: '99dd0a22-b306-4a6e-a404-0154dc052496' })
SET perf_0154dc052496.name = 'Tangiers'
SET perf_0154dc052496.duration = '5:59'
SET perf_0154dc052496.source = 'musicbrainz.org'


MERGE (perf_825cbae6f8eb:Performance{ uuid: '18555726-2fb3-4e61-bd2f-825cbae6f8eb' })
SET perf_825cbae6f8eb.name = 'Nothing Ever Changes For You My Love'
SET perf_825cbae6f8eb.duration = '4:13'
SET perf_825cbae6f8eb.source = 'musicbrainz.org'


MERGE (perf_99ea89e7bb84:Performance{ uuid: 'f2315eaa-d485-4568-bc8f-99ea89e7bb84' })
SET perf_99ea89e7bb84.name = 'Satan\\'s Mysterious Feeling'
SET perf_99ea89e7bb84.duration = '6:38'
SET perf_99ea89e7bb84.source = 'musicbrainz.org'


MERGE (perf_f3701beeb0d4:Performance{ uuid: 'ef4412f6-b119-4194-9012-f3701beeb0d4' })
SET perf_f3701beeb0d4.name = 'Medley: You Name It, List Ev\\'ry Voice And Sing'
SET perf_f3701beeb0d4.duration = '9:26'
SET perf_f3701beeb0d4.source = 'musicbrainz.org'




// labels
MERGE (release_0da292e7533f)-[:HAS_LABEL]->(label_2d074f9ea325)


// tracks
MERGE (release_0da292e7533f)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_e8bda766fa41)
MERGE (release_0da292e7533f)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_3c4bdf2f91cf)
MERGE (release_0da292e7533f)-[:HAS_TRACK {name: 'A3', sequence: 3}]->(perf_0154dc052496)
MERGE (release_0da292e7533f)-[:HAS_TRACK {name: 'A4', sequence: 4}]->(perf_825cbae6f8eb)
MERGE (release_0da292e7533f)-[:HAS_TRACK {name: 'B1', sequence: 5}]->(perf_99ea89e7bb84)
MERGE (release_0da292e7533f)-[:HAS_TRACK {name: 'B2', sequence: 6}]->(perf_f3701beeb0d4)

MERGE (person_8d0192d5a78b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_e8bda766fa41)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_e8bda766fa41)
MERGE (person_5b6e1e63e268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_e8bda766fa41)
MERGE (person_6d2978392b0b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_e8bda766fa41)
MERGE (person_8d0192d5a78b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_3c4bdf2f91cf)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_3c4bdf2f91cf)
MERGE (person_5b6e1e63e268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_3c4bdf2f91cf)
MERGE (person_6d2978392b0b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_3c4bdf2f91cf)
MERGE (person_8d0192d5a78b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_0154dc052496)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_0154dc052496)
MERGE (person_5b6e1e63e268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_0154dc052496)
MERGE (person_6d2978392b0b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_0154dc052496)
MERGE (person_8d0192d5a78b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_825cbae6f8eb)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_825cbae6f8eb)
MERGE (person_5b6e1e63e268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_825cbae6f8eb)
MERGE (person_6d2978392b0b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_825cbae6f8eb)
MERGE (person_8d0192d5a78b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_99ea89e7bb84)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_99ea89e7bb84)
MERGE (person_5b6e1e63e268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_99ea89e7bb84)
MERGE (person_6d2978392b0b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_99ea89e7bb84)
MERGE (person_8d0192d5a78b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['woodwind'] }]->(perf_f3701beeb0d4)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_f3701beeb0d4)
MERGE (person_5b6e1e63e268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_f3701beeb0d4)
MERGE (person_6d2978392b0b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f3701beeb0d4)



"""
)