
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

// releases

MERGE (release_90e3710bbac2:Release{ uuid: '6aacd502-679d-4451-9ebf-90e3710bbac2' })
SET release_90e3710bbac2.name = 'Busman\\'s Holiday'
SET release_90e3710bbac2.country = 'US'
SET release_90e3710bbac2.date = '1954'
SET release_90e3710bbac2.format = '10" Vinyl'
SET release_90e3710bbac2.discode = 'MG-26048'
SET release_90e3710bbac2.discogs = 'https://www.discogs.com/release/6120084'
SET release_90e3710bbac2.musicbrainz = 'http://musicbrainz.org/release/6aacd502-679d-4451-9ebf-90e3710bbac2'
SET release_90e3710bbac2.source = 'musicbrainz.org'


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


MERGE (person_7cc6ea3f2760:Person{ uuid: 'a6722684-ef61-4e64-9ad9-7cc6ea3f2760' }) 
SET person_7cc6ea3f2760.name = 'Åke Persson'
SET person_7cc6ea3f2760.gender = 'Male'
SET person_7cc6ea3f2760.country = 'SE'
SET person_7cc6ea3f2760.allmusic = 'https://www.allmusic.com/artist/mn0000607297'
SET person_7cc6ea3f2760.discogs = 'https://www.discogs.com/artist/582273'
SET person_7cc6ea3f2760.viaf = 'http://viaf.org/viaf/2657359'
SET person_7cc6ea3f2760.wikidata = 'https://www.wikidata.org/wiki/Q188208'
SET person_7cc6ea3f2760.wikipedia = 'https://en.wikipedia.org/wiki/%C3%85ke_Persson'
SET person_7cc6ea3f2760.databases = ['http://d-nb.info/gnd/1063255554', 'http://id.loc.gov/authorities/names/n2006059091', 'https://catalogue.bnf.fr/ark:/12148/cb138983984', 'https://www.worldcat.org/identities/lccn-n2006059091']
SET person_7cc6ea3f2760.musicbrainz = 'https://musicbrainz.org/artist/a6722684-ef61-4e64-9ad9-7cc6ea3f2760'
SET person_7cc6ea3f2760.isni_list = ['http://isni.org/isni/0000000115863325']
SET person_7cc6ea3f2760.source = 'musicbrainz.org'


MERGE (person_e2424455a108:Person{ uuid: '5f741d12-4aa0-46fc-8e49-e2424455a108' }) 
SET person_e2424455a108.name = 'Sahib Shihab'
SET person_e2424455a108.gender = 'Male'
SET person_e2424455a108.disambiguation = 'American jazz musician'
SET person_e2424455a108.country = 'US'
SET person_e2424455a108.allmusic = 'https://www.allmusic.com/artist/mn0000831788'
SET person_e2424455a108.discogs = 'https://www.discogs.com/artist/1220293'
SET person_e2424455a108.discogs = 'https://www.discogs.com/artist/89693'
SET person_e2424455a108.viaf = 'http://viaf.org/viaf/76501524'
SET person_e2424455a108.wikidata = 'https://www.wikidata.org/wiki/Q968887'
SET person_e2424455a108.databases = ['http://d-nb.info/gnd/134521250', 'http://id.loc.gov/authorities/names/nr90020312', 'https://catalogue.bnf.fr/ark:/12148/cb13899744j', 'http://snaccooperative.org/ark:/99166/w6jw9nzk', 'https://rateyourmusic.com/artist/sahib_shihab', 'https://www.worldcat.org/identities/lccn-nr90020312']
SET person_e2424455a108.musicbrainz = 'https://musicbrainz.org/artist/5f741d12-4aa0-46fc-8e49-e2424455a108'
SET person_e2424455a108.isni_list = ['http://isni.org/isni/0000000081569565', 'http://isni.org/isni/0000000368502261']
SET person_e2424455a108.source = 'musicbrainz.org'


MERGE (person_e1ca2bdde097:Person{ uuid: 'c6f84b92-7d04-47aa-b43a-e1ca2bdde097' }) 
SET person_e1ca2bdde097.name = 'Adrian Acia'
SET person_e1ca2bdde097.gender = 'Male'
SET person_e1ca2bdde097.discogs = 'https://www.discogs.com/artist/2656300'
SET person_e1ca2bdde097.musicbrainz = 'https://musicbrainz.org/artist/c6f84b92-7d04-47aa-b43a-e1ca2bdde097'
SET person_e1ca2bdde097.source = 'musicbrainz.org'


MERGE (person_51919784005c:Person{ uuid: 'bdacc598-6e9e-4938-982d-51919784005c' }) 
SET person_51919784005c.name = 'Bjarne Nerem'
SET person_51919784005c.gender = 'Male'
SET person_51919784005c.country = 'NO'
SET person_51919784005c.discogs = 'https://www.discogs.com/artist/478101'
SET person_51919784005c.viaf = 'http://viaf.org/viaf/51880525'
SET person_51919784005c.wikidata = 'https://www.wikidata.org/wiki/Q377092'
SET person_51919784005c.databases = ['http://d-nb.info/gnd/1029884021', 'http://id.loc.gov/authorities/names/n85323885', 'https://catalogue.bnf.fr/ark:/12148/cb13946701p', 'https://www.worldcat.org/identities/lccn-n85323885']
SET person_51919784005c.musicbrainz = 'https://musicbrainz.org/artist/bdacc598-6e9e-4938-982d-51919784005c'
SET person_51919784005c.isni_list = ['http://isni.org/isni/0000000374473524']
SET person_51919784005c.source = 'musicbrainz.org'


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

// labels

MERGE (label_42366b3be8c9:Label{ uuid: 'e023c53a-7e9b-4f7d-99ff-42366b3be8c9' })
SET label_42366b3be8c9.name= 'EmArcy'

// performances

MERGE (perf_d05d8441fc31:Performance{ uuid: '569c54d1-ea63-451a-844a-d05d8441fc31' })
SET perf_d05d8441fc31.name = 'Little Leona'
SET perf_d05d8441fc31.duration = '4:50'
SET perf_d05d8441fc31.source = 'musicbrainz.org'


MERGE (perf_83505cd06697:Performance{ uuid: 'e848b7b0-53aa-49d5-8a0e-83505cd06697' })
SET perf_83505cd06697.name = 'Miss Mopsy'
SET perf_83505cd06697.duration = '5:02'
SET perf_83505cd06697.source = 'musicbrainz.org'


MERGE (perf_85b17ed01bd1:Performance{ uuid: 'bb044123-0ebe-47d2-9f87-85b17ed01bd1' })
SET perf_85b17ed01bd1.name = 'Gone Again'
SET perf_85b17ed01bd1.duration = '5:56'
SET perf_85b17ed01bd1.source = 'musicbrainz.org'


MERGE (perf_6ee8dc57892c:Performance{ uuid: '8770c0df-33b6-4672-9dfe-6ee8dc57892c' })
SET perf_6ee8dc57892c.name = 'Hagnes'
SET perf_6ee8dc57892c.duration = '5:31'
SET perf_6ee8dc57892c.source = 'musicbrainz.org'




// labels
MERGE (release_90e3710bbac2)-[:HAS_LABEL]->(label_42366b3be8c9)


// tracks
MERGE (release_90e3710bbac2)-[:HAS_TRACK {name: 'A1', sequence: 1}]->(perf_d05d8441fc31)
MERGE (release_90e3710bbac2)-[:HAS_TRACK {name: 'A2', sequence: 2}]->(perf_83505cd06697)
MERGE (release_90e3710bbac2)-[:HAS_TRACK {name: 'B1', sequence: 3}]->(perf_85b17ed01bd1)
MERGE (release_90e3710bbac2)-[:HAS_TRACK {name: 'B2', sequence: 4}]->(perf_6ee8dc57892c)

MERGE (person_e1ca2bdde097)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d05d8441fc31)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d05d8441fc31)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_d05d8441fc31)
MERGE (person_51919784005c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_d05d8441fc31)
MERGE (person_7cc6ea3f2760)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_d05d8441fc31)
MERGE (person_e2424455a108)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_d05d8441fc31)
MERGE (person_e1ca2bdde097)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_83505cd06697)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_83505cd06697)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_83505cd06697)
MERGE (person_51919784005c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_83505cd06697)
MERGE (person_7cc6ea3f2760)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trombone'] }]->(perf_83505cd06697)
MERGE (person_e2424455a108)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_83505cd06697)
MERGE (person_e1ca2bdde097)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_85b17ed01bd1)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_85b17ed01bd1)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_85b17ed01bd1)
MERGE (person_51919784005c)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['tenor saxophone'] }]->(perf_85b17ed01bd1)
MERGE (person_e2424455a108)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['saxophone'] }]->(perf_85b17ed01bd1)
MERGE (person_e1ca2bdde097)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_6ee8dc57892c)
MERGE (person_8f221f658ef3)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_6ee8dc57892c)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['drums (drum set)'] }]->(perf_6ee8dc57892c)



"""
)