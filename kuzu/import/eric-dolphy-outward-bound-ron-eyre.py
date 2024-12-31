
import kuzu

db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

conn.execute(
"""

MERGE (release_e07e145d5b54:Release{ uuid: '2b01b641-ad01-4903-8028-e07e145d5b54' })
SET release_e07e145d5b54.name = 'Outward Bound'

MERGE (person_c3ea1fca0dd8:Person{ uuid: '95e86db2-7d52-48ed-a4cb-c3ea1fca0dd8' })
SET person_c3ea1fca0dd8.name = 'Ron Eyre'
SET person_c3ea1fca0dd8.gender = 'Male'
SET person_c3ea1fca0dd8.country = 'US'
SET person_c3ea1fca0dd8.discogs = 'https://www.discogs.com/artist/1650513-Ron-Eyre'
SET person_c3ea1fca0dd8.musicbrainz = 'https://musicbrainz.org/artist/95e86db2-7d52-48ed-a4cb-c3ea1fca0dd8'
SET person_c3ea1fca0dd8.source = 'musicbrainz.org'

MERGE (liner_notes_ef33ddf69a55:LinerNotes{ uuid: 'a0d2a07a-aaba-418b-ae08-ef33ddf69a55' })
SET liner_notes_ef33ddf69a55.name = 'Outward Bound, Liner Notes by Ron Eyre'
SET liner_notes_ef33ddf69a55.date = '1960'
SET liner_notes_ef33ddf69a55.type = 'Original'
SET liner_notes_ef33ddf69a55.thejazztome = 'https://thejazztome.info/eric-dolphy-outward-bound/'
SET liner_notes_ef33ddf69a55.internetarchive = 'https://archive.org/details/cd_outward-bound_eric-dolphy/page/n1/mode/1up'
SET liner_notes_ef33ddf69a55.discogs = 'https://i.discogs.com/Kqj9UxgaHbqXSf6udE4xXcjmGytLYW5tLY55FvvhTx8/rs:fit/g:sm/q:90/h:600/w:595/czM6Ly9kaXNjb2dz/LWRhdGFiYXNlLWlt/YWdlcy9SLTI5NzM1/NTItMTQ1ODAwMjY1/Ni04OTk5LmpwZWc.jpeg'


MERGE (person_c3ea1fca0dd8)-[:AUTHORED]->(liner_notes_ef33ddf69a55)

MERGE (release_e07e145d5b54)-[:HAS_LINER_NOTES]->(liner_notes_ef33ddf69a55)
    
"""
)