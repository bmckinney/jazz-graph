// releases

MERGE (release_fd6373109f9e:Release{ uuid: 'def54c2e-3b69-4ed7-8c19-fd6373109f9e' })
SET release_fd6373109f9e.name = 'Fountain of Youth'
SET release_fd6373109f9e.country = 'DE'
SET release_fd6373109f9e.date = '2007-09-10'
SET release_fd6373109f9e.format = 'Digital Media'
SET release_fd6373109f9e.musicbrainz = 'http://musicbrainz.org/release/def54c2e-3b69-4ed7-8c19-fd6373109f9e'
SET release_fd6373109f9e.source = 'musicbrainz.org'
SET release_fd6373109f9e.timestamp = timestamp()

MERGE (person_9fbfb804134b:Person{ uuid: '6788b047-292d-43c6-a781-9fbfb804134b' }) 
SET person_9fbfb804134b.name = 'Martin Bejerano'
SET person_9fbfb804134b.gender = 'Male'
SET person_9fbfb804134b.allmusic = 'https://www.allmusic.com/artist/mn0000317681'
SET person_9fbfb804134b.discogs = 'https://www.discogs.com/artist/991779'
SET person_9fbfb804134b.wikidata = 'https://www.wikidata.org/wiki/Q19665888'
SET person_9fbfb804134b.musicbrainz = 'https://musicbrainz.org/artist/6788b047-292d-43c6-a781-9fbfb804134b'
SET person_9fbfb804134b.source = 'musicbrainz.org'
SET person_9fbfb804134b.timestamp = timestamp()

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
SET person_6f0a331cc1ca.timestamp = timestamp()

MERGE (person_338556fa6693:Person{ uuid: '610a028f-aa19-43d4-afc0-338556fa6693' }) 
SET person_338556fa6693.name = 'Marcus Strickland'
SET person_338556fa6693.gender = 'Male'
SET person_338556fa6693.country = 'US'
SET person_338556fa6693.allmusic = 'https://www.allmusic.com/artist/mn0000569607'
SET person_338556fa6693.discogs = 'https://www.discogs.com/artist/659990'
SET person_338556fa6693.viaf = 'http://viaf.org/viaf/61273738'
SET person_338556fa6693.wikidata = 'https://www.wikidata.org/wiki/Q1894385'
SET person_338556fa6693.wikipedia = 'https://en.wikipedia.org/wiki/Marcus_Strickland'
SET person_338556fa6693.databases = ['http://d-nb.info/gnd/135244889', 'http://id.loc.gov/authorities/names/no2005025702', 'https://catalogue.bnf.fr/ark:/12148/cb150923392', 'https://www.worldcat.org/identities/lccn-no2005025702']
SET person_338556fa6693.musicbrainz = 'https://musicbrainz.org/artist/610a028f-aa19-43d4-afc0-338556fa6693'
SET person_338556fa6693.isni_list = ['http://isni.org/isni/0000000078480762']
SET person_338556fa6693.source = 'musicbrainz.org'
SET person_338556fa6693.timestamp = timestamp()

MERGE (person_727e344551dc:Person{ uuid: 'b57ca18c-fe34-4a5d-b896-727e344551dc' }) 
SET person_727e344551dc.name = 'John Sullivan'
SET person_727e344551dc.gender = 'Male'
SET person_727e344551dc.disambiguation = 'bass'
SET person_727e344551dc.country = 'US'
SET person_727e344551dc.discogs = 'https://www.discogs.com/artist/324037'
SET person_727e344551dc.musicbrainz = 'https://musicbrainz.org/artist/b57ca18c-fe34-4a5d-b896-727e344551dc'
SET person_727e344551dc.source = 'musicbrainz.org'
SET person_727e344551dc.timestamp = timestamp()

MERGE (person_fdfff1522b37:Person{ uuid: '816eedff-76ea-4d09-aabe-fdfff1522b37' }) 
SET person_fdfff1522b37.name = 'Doug Yoel'
SET person_fdfff1522b37.gender = 'Male'
SET person_fdfff1522b37.source = 'musicbrainz.org'
SET person_fdfff1522b37.timestamp = timestamp()

MERGE (person_98122d70043e:Person{ uuid: 'd3784f18-8960-4d63-8705-98122d70043e' }) 
SET person_98122d70043e.name = 'David Ruffo'
SET person_98122d70043e.gender = 'Male'
SET person_98122d70043e.source = 'musicbrainz.org'
SET person_98122d70043e.timestamp = timestamp()
// labels

MERGE (label_45a4aac43b37:Label{ uuid: 'd3698a68-ef9f-431e-93a0-45a4aac43b37' })
SET label_45a4aac43b37.name= 'Dreyfus Jazz'

// performances

MERGE (perf_b67cbb1cbe06:Performance{ uuid: '722353ae-45df-4ca3-9a69-b67cbb1cbe06' })
SET perf_b67cbb1cbe06.name = 'Greensleeves'
SET perf_b67cbb1cbe06.duration = '8:20'
SET perf_b67cbb1cbe06.begin = '2002-12-04'
SET perf_b67cbb1cbe06.end = '2002-12-05'
SET perf_b67cbb1cbe06.source = 'musicbrainz.org'
SET perf_b67cbb1cbe06.timestamp = timestamp()

MERGE (perf_80efa474e1fc:Performance{ uuid: 'f796717e-3dff-4dae-899f-80efa474e1fc' })
SET perf_80efa474e1fc.name = 'Trinkle Tinkle'
SET perf_80efa474e1fc.duration = '5:55'
SET perf_80efa474e1fc.begin = '2002-12-04'
SET perf_80efa474e1fc.end = '2002-12-05'
SET perf_80efa474e1fc.source = 'musicbrainz.org'
SET perf_80efa474e1fc.timestamp = timestamp()

MERGE (perf_7a546e698c02:Performance{ uuid: 'bdcfe6c8-ec56-41a5-98a2-7a546e698c02' })
SET perf_7a546e698c02.name = 'Summer Night'
SET perf_7a546e698c02.duration = '7:55'
SET perf_7a546e698c02.begin = '2002-12-04'
SET perf_7a546e698c02.end = '2002-12-05'
SET perf_7a546e698c02.source = 'musicbrainz.org'
SET perf_7a546e698c02.timestamp = timestamp()

MERGE (perf_ea9dfe3d3115:Performance{ uuid: '15eb6503-8df8-4629-a327-ea9dfe3d3115' })
SET perf_ea9dfe3d3115.name = 'Ask Me Now'
SET perf_ea9dfe3d3115.duration = '8:55'
SET perf_ea9dfe3d3115.begin = '2002-12-04'
SET perf_ea9dfe3d3115.end = '2002-12-05'
SET perf_ea9dfe3d3115.source = 'musicbrainz.org'
SET perf_ea9dfe3d3115.timestamp = timestamp()

MERGE (perf_38217949a919:Performance{ uuid: '5b8f4033-00ad-447c-bd30-38217949a919' })
SET perf_38217949a919.name = 'Butch and Butch'
SET perf_38217949a919.duration = '4:50'
SET perf_38217949a919.begin = '2002-12-04'
SET perf_38217949a919.end = '2002-12-05'
SET perf_38217949a919.source = 'musicbrainz.org'
SET perf_38217949a919.timestamp = timestamp()

MERGE (perf_c6096d9b7d6b:Performance{ uuid: '9cdc254e-8470-4edb-a8bd-c6096d9b7d6b' })
SET perf_c6096d9b7d6b.name = 'Inner Trust'
SET perf_c6096d9b7d6b.duration = '10:53'
SET perf_c6096d9b7d6b.begin = '2002-12-04'
SET perf_c6096d9b7d6b.end = '2002-12-05'
SET perf_c6096d9b7d6b.source = 'musicbrainz.org'
SET perf_c6096d9b7d6b.timestamp = timestamp()

MERGE (perf_cc42cb95087d:Performance{ uuid: '75e49f66-4e19-4261-9673-cc42cb95087d' })
SET perf_cc42cb95087d.name = 'Green Chimneys'
SET perf_cc42cb95087d.duration = '8:08'
SET perf_cc42cb95087d.begin = '2002-12-04'
SET perf_cc42cb95087d.end = '2002-12-05'
SET perf_cc42cb95087d.source = 'musicbrainz.org'
SET perf_cc42cb95087d.timestamp = timestamp()

MERGE (perf_a0785bfd9ce6:Performance{ uuid: '8e58b7af-fcda-4660-ad92-a0785bfd9ce6' })
SET perf_a0785bfd9ce6.name = 'Remember'
SET perf_a0785bfd9ce6.duration = '6:12'
SET perf_a0785bfd9ce6.begin = '2002-12-04'
SET perf_a0785bfd9ce6.end = '2002-12-05'
SET perf_a0785bfd9ce6.source = 'musicbrainz.org'
SET perf_a0785bfd9ce6.timestamp = timestamp()

MERGE (perf_8abe3ccdee07:Performance{ uuid: '4e129775-e34c-46be-bbad-8abe3ccdee07' })
SET perf_8abe3ccdee07.name = 'Question & Answer'
SET perf_8abe3ccdee07.duration = '10:16'
SET perf_8abe3ccdee07.begin = '2002-12-04'
SET perf_8abe3ccdee07.end = '2002-12-05'
SET perf_8abe3ccdee07.source = 'musicbrainz.org'
SET perf_8abe3ccdee07.timestamp = timestamp()



// labels
MERGE (release_fd6373109f9e)-[:HAS_LABEL]->(label_45a4aac43b37)


// tracks
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_b67cbb1cbe06)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_80efa474e1fc)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_7a546e698c02)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_ea9dfe3d3115)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_38217949a919)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_c6096d9b7d6b)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_cc42cb95087d)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_a0785bfd9ce6)
MERGE (release_fd6373109f9e)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_8abe3ccdee07)

// works

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
SET person_5260b4274ed4.timestamp = timestamp()

MERGE (person_eb9dc9f506b5:Person{ uuid: '5e645519-a175-4fe0-9a9b-eb9dc9f506b5' }) 
SET person_eb9dc9f506b5.name = 'Irving Berlin'
SET person_eb9dc9f506b5.gender = 'Male'
SET person_eb9dc9f506b5.country = 'US'
SET person_eb9dc9f506b5.allmusic = 'https://www.allmusic.com/artist/mn0000103748'
SET person_eb9dc9f506b5.bbc = 'https://www.bbc.co.uk/music/artists/5e645519-a175-4fe0-9a9b-eb9dc9f506b5'
SET person_eb9dc9f506b5.discogs = 'https://www.discogs.com/artist/508131'
SET person_eb9dc9f506b5.imdb = 'https://www.imdb.com/name/nm0000927/'
SET person_eb9dc9f506b5.viaf = 'http://viaf.org/viaf/19864566'
SET person_eb9dc9f506b5.wikidata = 'https://www.wikidata.org/wiki/Q128746'
SET person_eb9dc9f506b5.databases = ['https://ibdb.com/person.php?id=6452', 'https://rateyourmusic.com/artist/irving_berlin', 'http://www.lortel.org/LLA_archive/index.cfm?search_by=people&first=Irving&last=Berlin&middle=']
SET person_eb9dc9f506b5.musicbrainz = 'https://musicbrainz.org/artist/5e645519-a175-4fe0-9a9b-eb9dc9f506b5'
SET person_eb9dc9f506b5.isni_list = ['http://isni.org/isni/0000000108769971']
SET person_eb9dc9f506b5.source = 'musicbrainz.org'
SET person_eb9dc9f506b5.timestamp = timestamp()

MERGE (person_b2ff98c26207:Person{ uuid: '8663f6b3-497f-4009-a47d-b2ff98c26207' }) 
SET person_b2ff98c26207.name = 'Richard Jones'
SET person_b2ff98c26207.gender = 'Male'
SET person_b2ff98c26207.disambiguation = 'English printer, songwriter, and composer'
SET person_b2ff98c26207.source = 'musicbrainz.org'
SET person_b2ff98c26207.timestamp = timestamp()

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
SET person_f8091d98cf25.timestamp = timestamp()

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
SET person_8f9b52869d74.timestamp = timestamp()

MERGE (person_5c6090f7ea1b:Person{ uuid: 'ab4ee924-e126-4835-8433-5c6090f7ea1b' }) 
SET person_5c6090f7ea1b.name = 'Al Dubin'
SET person_5c6090f7ea1b.gender = 'Male'
SET person_5c6090f7ea1b.country = 'CH'
SET person_5c6090f7ea1b.allmusic = 'https://www.allmusic.com/artist/mn0000770368'
SET person_5c6090f7ea1b.discogs = 'https://www.discogs.com/artist/628267'
SET person_5c6090f7ea1b.imdb = 'https://www.imdb.com/name/nm0006048/'
SET person_5c6090f7ea1b.viaf = 'http://viaf.org/viaf/71582796'
SET person_5c6090f7ea1b.wikidata = 'https://www.wikidata.org/wiki/Q180899'
SET person_5c6090f7ea1b.databases = ['http://d-nb.info/gnd/103976604', 'http://id.loc.gov/authorities/names/n80151128', 'https://adp.library.ucsb.edu/names/102968', 'https://catalogue.bnf.fr/ark:/12148/cb139430418', 'http://snaccooperative.org/ark:/99166/w6b39wqj', 'https://nla.gov.au/nla.party-919241', 'https://rateyourmusic.com/artist/al_dubin', 'https://www.ibdb.com/person.php?id=12855', 'https://www.worldcat.org/identities/lccn-n80151128/']
SET person_5c6090f7ea1b.musicbrainz = 'https://musicbrainz.org/artist/ab4ee924-e126-4835-8433-5c6090f7ea1b'
SET person_5c6090f7ea1b.isni_list = ['http://isni.org/isni/0000000081517132']
SET person_5c6090f7ea1b.source = 'musicbrainz.org'
SET person_5c6090f7ea1b.timestamp = timestamp()

MERGE (person_7fd09c8ae291:Person{ uuid: '7a9390eb-76ea-4d3a-a786-7fd09c8ae291' }) 
SET person_7fd09c8ae291.name = 'Harry Warren'
SET person_7fd09c8ae291.gender = 'Male'
SET person_7fd09c8ae291.disambiguation = 'US composer and lyricist'
SET person_7fd09c8ae291.country = 'US'
SET person_7fd09c8ae291.allmusic = 'https://www.allmusic.com/artist/mn0000961299'
SET person_7fd09c8ae291.discogs = 'https://www.discogs.com/artist/601710'
SET person_7fd09c8ae291.imdb = 'https://www.imdb.com/name/nm0912851/'
SET person_7fd09c8ae291.viaf = 'http://viaf.org/viaf/79169269'
SET person_7fd09c8ae291.wikidata = 'https://www.wikidata.org/wiki/Q938810'
SET person_7fd09c8ae291.databases = ['https://rateyourmusic.com/artist/harry_warren']
SET person_7fd09c8ae291.musicbrainz = 'https://musicbrainz.org/artist/7a9390eb-76ea-4d3a-a786-7fd09c8ae291'
SET person_7fd09c8ae291.isni_list = ['http://isni.org/isni/0000000083969407']
SET person_7fd09c8ae291.source = 'musicbrainz.org'
SET person_7fd09c8ae291.timestamp = timestamp()

MERGE (work_9eae6375ecb0:Work{ uuid: '6ae0f429-cd54-3ac2-b635-9eae6375ecb0' })
SET work_9eae6375ecb0.name = 'Question and Answer'
SET work_9eae6375ecb0.iswc = 'T-070.243.048-5'
SET work_9eae6375ecb0.type = 'Song'
SET work_9eae6375ecb0.source = 'musicbrainz.org'
SET work_9eae6375ecb0.timestamp = timestamp()

MERGE (work_f7cac02af20b:Work{ uuid: '9dabc9a2-f223-4de8-a7f3-f7cac02af20b' })
SET work_f7cac02af20b.name = 'Summer Night'
SET work_f7cac02af20b.type = 'Song'
SET work_f7cac02af20b.source = 'musicbrainz.org'
SET work_f7cac02af20b.timestamp = timestamp()

MERGE (work_5eed6e3b0117:Work{ uuid: '0bb7d2ad-0a44-3b73-bbbc-5eed6e3b0117' })
SET work_5eed6e3b0117.name = 'Greensleeves'
SET work_5eed6e3b0117.type = 'Song'
SET work_5eed6e3b0117.tags = ['english folk', 'folk']
SET work_5eed6e3b0117.allmusic = 'https://www.allmusic.com/composition/mc0002354929'
SET work_5eed6e3b0117.wikidata = 'https://www.wikidata.org/wiki/Q674738'
SET work_5eed6e3b0117.musicbrainz = 'https://musicbrainz.org/work/0bb7d2ad-0a44-3b73-bbbc-5eed6e3b0117'
SET work_5eed6e3b0117.source = 'musicbrainz.org'
SET work_5eed6e3b0117.timestamp = timestamp()

MERGE (work_f60732ce3c13:Work{ uuid: '46944964-7458-3a35-acdd-f60732ce3c13' })
SET work_f60732ce3c13.name = 'Ask Me Now'
SET work_f60732ce3c13.iswc = 'T-700.000.924-7'
SET work_f60732ce3c13.type = 'Song'
SET work_f60732ce3c13.wikidata = 'https://www.wikidata.org/wiki/Q4807077'
SET work_f60732ce3c13.musicbrainz = 'https://musicbrainz.org/work/46944964-7458-3a35-acdd-f60732ce3c13'
SET work_f60732ce3c13.source = 'musicbrainz.org'
SET work_f60732ce3c13.timestamp = timestamp()

MERGE (work_88af68626085:Work{ uuid: 'ef6b8ef1-0d16-4c4b-87b0-88af68626085' })
SET work_88af68626085.name = 'Green Chimneys'
SET work_88af68626085.iswc = 'T-070.234.354-1'
SET work_88af68626085.type = 'Song'
SET work_88af68626085.musicbrainz = 'https://musicbrainz.org/work/ef6b8ef1-0d16-4c4b-87b0-88af68626085'
SET work_88af68626085.source = 'musicbrainz.org'
SET work_88af68626085.timestamp = timestamp()

MERGE (work_a66874c995b3:Work{ uuid: 'd28b7488-7b7d-4867-b80f-a66874c995b3' })
SET work_a66874c995b3.name = 'Remember'
SET work_a66874c995b3.iswc = 'T-070.126.365-1'
SET work_a66874c995b3.type = 'Song'
SET work_a66874c995b3.wikidata = 'https://www.wikidata.org/wiki/Q7311630'
SET work_a66874c995b3.wikipedia = 'https://en.wikipedia.org/wiki/Remember_(Irving_Berlin_song)'
SET work_a66874c995b3.musicbrainz = 'https://musicbrainz.org/work/d28b7488-7b7d-4867-b80f-a66874c995b3'
SET work_a66874c995b3.source = 'musicbrainz.org'
SET work_a66874c995b3.timestamp = timestamp()

MERGE (work_1003e9b588f3:Work{ uuid: '067eccc9-5533-34b9-a676-1003e9b588f3' })
SET work_1003e9b588f3.name = 'Trinkle Tinkle'
SET work_1003e9b588f3.iswc = 'T-070.247.478-9'
SET work_1003e9b588f3.type = 'Song'
SET work_1003e9b588f3.source = 'musicbrainz.org'
SET work_1003e9b588f3.timestamp = timestamp()

MERGE (work_5f29a4fb7446:Work{ uuid: '0b7b019a-0005-49df-97e3-5f29a4fb7446' })
SET work_5f29a4fb7446.name = 'Butch and Butch'
SET work_5f29a4fb7446.type = 'Song'
SET work_5f29a4fb7446.source = 'musicbrainz.org'
SET work_5f29a4fb7446.timestamp = timestamp()


// performances of
MERGE (perf_8abe3ccdee07)-[:PERFORMANCE_OF]->(work_9eae6375ecb0)
MERGE (perf_7a546e698c02)-[:PERFORMANCE_OF]->(work_f7cac02af20b)
MERGE (perf_b67cbb1cbe06)-[:PERFORMANCE_OF]->(work_5eed6e3b0117)
MERGE (perf_ea9dfe3d3115)-[:PERFORMANCE_OF]->(work_f60732ce3c13)
MERGE (perf_cc42cb95087d)-[:PERFORMANCE_OF]->(work_88af68626085)
MERGE (perf_a0785bfd9ce6)-[:PERFORMANCE_OF]->(work_a66874c995b3)
MERGE (perf_80efa474e1fc)-[:PERFORMANCE_OF]->(work_1003e9b588f3)
MERGE (perf_38217949a919)-[:PERFORMANCE_OF]->(work_5f29a4fb7446)


// composers
MERGE (person_f8091d98cf25)-[:COMPOSED]->(work_9eae6375ecb0)
MERGE (person_5c6090f7ea1b)-[:COMPOSED]->(work_f7cac02af20b)
MERGE (person_7fd09c8ae291)-[:COMPOSED]->(work_f7cac02af20b)
MERGE (person_b2ff98c26207)-[:COMPOSED]->(work_5eed6e3b0117)
MERGE (person_b2ff98c26207)-[:WROTE_LYRICS]->(work_5eed6e3b0117)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_f60732ce3c13)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_88af68626085)
MERGE (person_eb9dc9f506b5)-[:COMPOSED]->(work_a66874c995b3)
MERGE (person_eb9dc9f506b5)-[:WROTE_LYRICS]->(work_a66874c995b3)
MERGE (person_5260b4274ed4)-[:COMPOSED]->(work_1003e9b588f3)
MERGE (person_8f9b52869d74)-[:COMPOSED]->(work_5f29a4fb7446)


// place nodes

MERGE (place_9808a9b287fa:Place{ uuid: '578aeeca-1616-49b2-9ff9-9808a9b287fa' })
SET place_9808a9b287fa.name = 'Birdland'
SET place_9808a9b287fa.source = 'musicbrainz.org'


// place relationships
MERGE (perf_b67cbb1cbe06)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_80efa474e1fc)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_7a546e698c02)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_ea9dfe3d3115)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_38217949a919)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_c6096d9b7d6b)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_cc42cb95087d)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_a0785bfd9ce6)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)
MERGE (perf_8abe3ccdee07)-[:HAS_PLACE { type: 'recorded at', begin: '2002-12-04', end: '2002-12-05' }]->(place_9808a9b287fa)

MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_b67cbb1cbe06)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_b67cbb1cbe06)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_b67cbb1cbe06)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_b67cbb1cbe06)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_b67cbb1cbe06)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_b67cbb1cbe06)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_80efa474e1fc)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_80efa474e1fc)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_80efa474e1fc)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_80efa474e1fc)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_80efa474e1fc)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_80efa474e1fc)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_7a546e698c02)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_7a546e698c02)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_7a546e698c02)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_7a546e698c02)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_7a546e698c02)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_7a546e698c02)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_ea9dfe3d3115)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_ea9dfe3d3115)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_ea9dfe3d3115)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_ea9dfe3d3115)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_ea9dfe3d3115)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_ea9dfe3d3115)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_38217949a919)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_38217949a919)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_38217949a919)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_38217949a919)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_38217949a919)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_38217949a919)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_c6096d9b7d6b)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_c6096d9b7d6b)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_c6096d9b7d6b)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_c6096d9b7d6b)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_c6096d9b7d6b)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_c6096d9b7d6b)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_cc42cb95087d)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_cc42cb95087d)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_cc42cb95087d)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_cc42cb95087d)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_cc42cb95087d)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_cc42cb95087d)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_a0785bfd9ce6)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_a0785bfd9ce6)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_a0785bfd9ce6)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_a0785bfd9ce6)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_a0785bfd9ce6)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_a0785bfd9ce6)
MERGE (person_6f0a331cc1ca)-[:PARTICIPATED_IN { roles: ['musician', 'producer'], instruments: ['drums (drum set)'] }]->(perf_8abe3ccdee07)
MERGE (person_9fbfb804134b)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8abe3ccdee07)
MERGE (person_338556fa6693)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['reeds'] }]->(perf_8abe3ccdee07)
MERGE (person_727e344551dc)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['double bass'] }]->(perf_8abe3ccdee07)
MERGE (person_98122d70043e)-[:PARTICIPATED_IN { roles: ['recording engineer'] }]->(perf_8abe3ccdee07)
MERGE (person_fdfff1522b37)-[:PARTICIPATED_IN { roles: ['producer'] }]->(perf_8abe3ccdee07)

