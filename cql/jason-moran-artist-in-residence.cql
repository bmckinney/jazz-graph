// releases

MERGE (release_a0463f291822:Release{ uuid: '2c626844-1ed1-4e52-b966-a0463f291822' })
SET release_a0463f291822.name = 'Artist in Residence'
SET release_a0463f291822.country = 'US'
SET release_a0463f291822.date = '2006-09-12'
SET release_a0463f291822.format = 'CD'
SET release_a0463f291822.discode = '0946 3 62711 2 5'
SET release_a0463f291822.discogs = 'https://www.discogs.com/release/4819423'
SET release_a0463f291822.musicbrainz = 'http://musicbrainz.org/release/2c626844-1ed1-4e52-b966-a0463f291822'
SET release_a0463f291822.source = 'musicbrainz.org'
SET release_a0463f291822.timestamp = timestamp()

MERGE (person_ab71e164ae60:Person{ uuid: 'a60a8aad-3d96-441a-9c3b-ab71e164ae60' }) 
SET person_ab71e164ae60.name = 'Tarus Mateen'
SET person_ab71e164ae60.gender = 'Male'
SET person_ab71e164ae60.country = 'US'
SET person_ab71e164ae60.allmusic = 'https://www.allmusic.com/artist/mn0000011084'
SET person_ab71e164ae60.discogs = 'https://www.discogs.com/artist/187661'
SET person_ab71e164ae60.viaf = 'http://viaf.org/viaf/22332258'
SET person_ab71e164ae60.wikidata = 'https://www.wikidata.org/wiki/Q1481025'
SET person_ab71e164ae60.databases = ['http://id.loc.gov/authorities/names/nr94041571', 'https://catalogue.bnf.fr/ark:/12148/cb13939811s', 'https://d-nb.info/gnd/134742745', 'https://www.worldcat.org/identities/lccn-nr94041571']
SET person_ab71e164ae60.musicbrainz = 'https://musicbrainz.org/artist/a60a8aad-3d96-441a-9c3b-ab71e164ae60'
SET person_ab71e164ae60.isni_list = ['http://isni.org/isni/0000000055164943']
SET person_ab71e164ae60.source = 'musicbrainz.org'
SET person_ab71e164ae60.timestamp = timestamp()

MERGE (person_67b070680a78:Person{ uuid: '6b079c70-64ff-4865-a699-67b070680a78' }) 
SET person_67b070680a78.name = 'Alicia Hall Moran'
SET person_67b070680a78.musicbrainz = 'https://musicbrainz.org/artist/6b079c70-64ff-4865-a699-67b070680a78'
SET person_67b070680a78.source = 'musicbrainz.org'
SET person_67b070680a78.timestamp = timestamp()

MERGE (person_ba0ce36d5a54:Person{ uuid: '50a172ae-3de4-498a-9352-ba0ce36d5a54' }) 
SET person_ba0ce36d5a54.name = 'Adrian Piper'
SET person_ba0ce36d5a54.source = 'musicbrainz.org'
SET person_ba0ce36d5a54.timestamp = timestamp()

MERGE (person_b5acc3932dcf:Person{ uuid: '7fa3578c-76b6-45ea-9041-b5acc3932dcf' }) 
SET person_b5acc3932dcf.name = 'Abdou M’Boup'
SET person_b5acc3932dcf.discogs = 'https://www.discogs.com/artist/314263'
SET person_b5acc3932dcf.musicbrainz = 'https://musicbrainz.org/artist/7fa3578c-76b6-45ea-9041-b5acc3932dcf'
SET person_b5acc3932dcf.source = 'musicbrainz.org'
SET person_b5acc3932dcf.timestamp = timestamp()

MERGE (person_1e32b602b802:Person{ uuid: 'e237b71d-0196-4a37-90a3-1e32b602b802' }) 
SET person_1e32b602b802.name = 'Ralph Alessi'
SET person_1e32b602b802.gender = 'Male'
SET person_1e32b602b802.country = 'US'
SET person_1e32b602b802.allmusic = 'https://www.allmusic.com/artist/mn0000397752'
SET person_1e32b602b802.discogs = 'https://www.discogs.com/artist/316510'
SET person_1e32b602b802.viaf = 'http://viaf.org/viaf/34651038'
SET person_1e32b602b802.wikidata = 'https://www.wikidata.org/wiki/Q957350'
SET person_1e32b602b802.databases = ['http://id.loc.gov/authorities/names/no96057741', 'https://catalogue.bnf.fr/ark:/12148/cb13972037d', 'https://d-nb.info/gnd/134825632', 'https://www.worldcat.org/identities/lccn-no96057741']
SET person_1e32b602b802.musicbrainz = 'https://musicbrainz.org/artist/e237b71d-0196-4a37-90a3-1e32b602b802'
SET person_1e32b602b802.isni_list = ['http://isni.org/isni/0000000078392383']
SET person_1e32b602b802.source = 'musicbrainz.org'
SET person_1e32b602b802.timestamp = timestamp()

MERGE (person_0d41405698ee:Person{ uuid: '55cf78f8-3825-431f-bf48-0d41405698ee' }) 
SET person_0d41405698ee.name = 'Joan Jonas'
SET person_0d41405698ee.gender = 'Female'
SET person_0d41405698ee.country = 'US'
SET person_0d41405698ee.discogs = 'https://www.discogs.com/artist/615963'
SET person_0d41405698ee.viaf = 'http://viaf.org/viaf/15012445'
SET person_0d41405698ee.wikidata = 'https://www.wikidata.org/wiki/Q453808'
SET person_0d41405698ee.musicbrainz = 'https://musicbrainz.org/artist/55cf78f8-3825-431f-bf48-0d41405698ee'
SET person_0d41405698ee.isni_list = ['http://isni.org/isni/000000008094559X']
SET person_0d41405698ee.source = 'musicbrainz.org'
SET person_0d41405698ee.timestamp = timestamp()

MERGE (person_f5abd1c891d8:Person{ uuid: 'c882838a-f551-4c88-b316-f5abd1c891d8' }) 
SET person_f5abd1c891d8.name = 'Marvin Sewell'
SET person_f5abd1c891d8.gender = 'Male'
SET person_f5abd1c891d8.country = 'US'
SET person_f5abd1c891d8.discogs = 'https://www.discogs.com/artist/300870'
SET person_f5abd1c891d8.wikidata = 'https://www.wikidata.org/wiki/Q55106149'
SET person_f5abd1c891d8.musicbrainz = 'https://musicbrainz.org/artist/c882838a-f551-4c88-b316-f5abd1c891d8'
SET person_f5abd1c891d8.isni_list = ['http://isni.org/isni/0000000406824000']
SET person_f5abd1c891d8.source = 'musicbrainz.org'
SET person_f5abd1c891d8.timestamp = timestamp()

MERGE (person_c65081d12d86:Person{ uuid: '2f97f8ef-1bd6-439e-b725-c65081d12d86' }) 
SET person_c65081d12d86.name = 'Jason Moran'
SET person_c65081d12d86.gender = 'Male'
SET person_c65081d12d86.disambiguation = 'American jazz pianist and composer'
SET person_c65081d12d86.country = 'US'
SET person_c65081d12d86.discogs = 'https://www.discogs.com/artist/96435'
SET person_c65081d12d86.imdb = 'https://www.imdb.com/name/nm1390780/'
SET person_c65081d12d86.viaf = 'http://viaf.org/viaf/49422111'
SET person_c65081d12d86.wikidata = 'https://www.wikidata.org/wiki/Q978467'
SET person_c65081d12d86.databases = ['http://id.loc.gov/authorities/names/no2001053219', 'https://catalogue.bnf.fr/ark:/12148/cb14025774t', 'https://d-nb.info/gnd/13512669X', 'http://www.worldcat.org/wcidentities/lccn-no2001-53219']
SET person_c65081d12d86.musicbrainz = 'https://musicbrainz.org/artist/2f97f8ef-1bd6-439e-b725-c65081d12d86'
SET person_c65081d12d86.isni_list = ['http://isni.org/isni/000000011443588X']
SET person_c65081d12d86.source = 'musicbrainz.org'
SET person_c65081d12d86.timestamp = timestamp()

MERGE (person_cf15b8735268:Person{ uuid: 'ab3363db-53ac-44c1-abfe-cf15b8735268' }) 
SET person_cf15b8735268.name = 'Nasheet Waits'
SET person_cf15b8735268.gender = 'Male'
SET person_cf15b8735268.country = 'US'
SET person_cf15b8735268.allmusic = 'https://www.allmusic.com/artist/mn0000315826'
SET person_cf15b8735268.discogs = 'https://www.discogs.com/artist/334551'
SET person_cf15b8735268.viaf = 'http://viaf.org/viaf/37128340'
SET person_cf15b8735268.wikidata = 'https://www.wikidata.org/wiki/Q1965729'
SET person_cf15b8735268.databases = ['http://id.loc.gov/authorities/names/no2001000847', 'https://catalogue.bnf.fr/ark:/12148/cb142374501', 'https://d-nb.info/gnd/135043077', 'https://www.worldcat.org/identities/lccn-no2001000847']
SET person_cf15b8735268.musicbrainz = 'https://musicbrainz.org/artist/ab3363db-53ac-44c1-abfe-cf15b8735268'
SET person_cf15b8735268.isni_list = ['http://isni.org/isni/0000000055174105']
SET person_cf15b8735268.source = 'musicbrainz.org'
SET person_cf15b8735268.timestamp = timestamp()
// labels

MERGE (label_14e1ddfd5946:Label{ uuid: '713c4a95-6616-442b-9cf6-14e1ddfd5946' })
SET label_14e1ddfd5946.name= 'Blue Note'

// performances

MERGE (perf_dc32390daee8:Performance{ uuid: '42e333e2-0fcc-49b5-9518-dc32390daee8' })
SET perf_dc32390daee8.name = 'Break Down'
SET perf_dc32390daee8.duration = '3:15'
SET perf_dc32390daee8.source = 'musicbrainz.org'
SET perf_dc32390daee8.timestamp = timestamp()

MERGE (perf_67e758b67c75:Performance{ uuid: '8af28939-51bd-47aa-983a-67e758b67c75' })
SET perf_67e758b67c75.name = 'Milestone'
SET perf_67e758b67c75.duration = '3:35'
SET perf_67e758b67c75.source = 'musicbrainz.org'
SET perf_67e758b67c75.timestamp = timestamp()

MERGE (perf_511640691c58:Performance{ uuid: '2fa4c4bb-8700-4c69-ab55-511640691c58' })
SET perf_511640691c58.name = 'Refraction 2'
SET perf_511640691c58.duration = '3:52'
SET perf_511640691c58.source = 'musicbrainz.org'
SET perf_511640691c58.timestamp = timestamp()

MERGE (perf_f23b4d6e6800:Performance{ uuid: '3463a76f-a526-4442-bb63-f23b4d6e6800' })
SET perf_f23b4d6e6800.name = 'Cradle Song'
SET perf_f23b4d6e6800.duration = '4:27'
SET perf_f23b4d6e6800.source = 'musicbrainz.org'
SET perf_f23b4d6e6800.timestamp = timestamp()

MERGE (perf_8d3c0bf33ff2:Performance{ uuid: 'a99897e7-0c5b-474d-9f90-8d3c0bf33ff2' })
SET perf_8d3c0bf33ff2.name = 'Artists Ought to Be Writing'
SET perf_8d3c0bf33ff2.duration = '3:51'
SET perf_8d3c0bf33ff2.source = 'musicbrainz.org'
SET perf_8d3c0bf33ff2.timestamp = timestamp()

MERGE (perf_573858841d75:Performance{ uuid: '24bd9eb7-4f25-4605-9801-573858841d75' })
SET perf_573858841d75.name = 'Refraction 1'
SET perf_573858841d75.duration = '6:15'
SET perf_573858841d75.source = 'musicbrainz.org'
SET perf_573858841d75.timestamp = timestamp()

MERGE (perf_383359fcf76d:Performance{ uuid: 'd92f04fe-5b47-4c5b-b4c2-383359fcf76d' })
SET perf_383359fcf76d.name = 'Arizona Landscape'
SET perf_383359fcf76d.duration = '3:07'
SET perf_383359fcf76d.source = 'musicbrainz.org'
SET perf_383359fcf76d.timestamp = timestamp()

MERGE (perf_81550b001a94:Performance{ uuid: 'a4e830a2-da06-498e-891d-81550b001a94' })
SET perf_81550b001a94.name = 'RAIN'
SET perf_81550b001a94.duration = '11:50'
SET perf_81550b001a94.source = 'musicbrainz.org'
SET perf_81550b001a94.timestamp = timestamp()

MERGE (perf_d54648562734:Performance{ uuid: 'a6ee909a-71f7-40bd-b03e-d54648562734' })
SET perf_d54648562734.name = 'Lift Ev\'ry Voice and Sing'
SET perf_d54648562734.duration = '4:55'
SET perf_d54648562734.source = 'musicbrainz.org'
SET perf_d54648562734.timestamp = timestamp()

MERGE (perf_bc128d906daa:Performance{ uuid: '731af0bf-cdc1-4b1d-a461-bc128d906daa' })
SET perf_bc128d906daa.name = 'He Puts on his Coat and Leaves'
SET perf_bc128d906daa.duration = '4:54'
SET perf_bc128d906daa.source = 'musicbrainz.org'
SET perf_bc128d906daa.timestamp = timestamp()



// labels
MERGE (release_a0463f291822)-[:HAS_LABEL]->(label_14e1ddfd5946)


// tracks
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '1', sequence: 1}]->(perf_dc32390daee8)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '2', sequence: 2}]->(perf_67e758b67c75)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '3', sequence: 3}]->(perf_511640691c58)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '4', sequence: 4}]->(perf_f23b4d6e6800)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '5', sequence: 5}]->(perf_8d3c0bf33ff2)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '6', sequence: 6}]->(perf_573858841d75)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '7', sequence: 7}]->(perf_383359fcf76d)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '8', sequence: 8}]->(perf_81550b001a94)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '9', sequence: 9}]->(perf_d54648562734)
MERGE (release_a0463f291822)-[:HAS_TRACK {name: '10', sequence: 10}]->(perf_bc128d906daa)

// works

MERGE (person_c77d3a920abe:Person{ uuid: 'c2d17829-1424-435b-9386-c77d3a920abe' }) 
SET person_c77d3a920abe.name = 'Carl Maria von Weber'
SET person_c77d3a920abe.gender = 'Male'
SET person_c77d3a920abe.disambiguation = 'composer'
SET person_c77d3a920abe.country = 'DE'
SET person_c77d3a920abe.allmusic = 'https://www.allmusic.com/artist/mn0002134208'
SET person_c77d3a920abe.bbc = 'https://www.bbc.co.uk/music/artists/c2d17829-1424-435b-9386-c77d3a920abe'
SET person_c77d3a920abe.discogs = 'https://www.discogs.com/artist/620726'
SET person_c77d3a920abe.imdb = 'https://www.imdb.com/name/nm0903203/'
SET person_c77d3a920abe.viaf = 'http://viaf.org/viaf/14959938'
SET person_c77d3a920abe.wikidata = 'https://www.wikidata.org/wiki/Q154812'
SET person_c77d3a920abe.databases = ['http://id.loc.gov/authorities/names/n79110317', 'https://adp.library.ucsb.edu/names/102543', 'https://catalogue.bnf.fr/ark:/12148/cb13901052m', 'https://d-nb.info/gnd/118629662', 'http://snaccooperative.org/ark:/99166/w6cc0zb3', 'https://nla.gov.au/nla.party-1224531', 'https://openlibrary.org/works/OL1098039A', 'https://www.classicalarchives.com/composer/3543.html', 'https://www.ibdb.com/person.php?id=118643', 'https://www.worldcat.org/identities/lccn-n79110317']
SET person_c77d3a920abe.musicbrainz = 'https://musicbrainz.org/artist/c2d17829-1424-435b-9386-c77d3a920abe'
SET person_c77d3a920abe.isni_list = ['http://isni.org/isni/0000000123199065']
SET person_c77d3a920abe.source = 'musicbrainz.org'
SET person_c77d3a920abe.timestamp = timestamp()

MERGE (person_e057484327fe:Person{ uuid: '125ec42a-7229-4250-afc5-e057484327fe' }) 
SET person_e057484327fe.name = '[unknown]'
SET person_e057484327fe.gender = 'Not applicable'
SET person_e057484327fe.disambiguation = 'Special Purpose Artist – Do not add releases here, if possible.'
SET person_e057484327fe.country = 'XW'
SET person_e057484327fe.discogs = 'https://www.discogs.com/artist/355'
SET person_e057484327fe.wikidata = 'https://www.wikidata.org/wiki/Q56678558'
SET person_e057484327fe.databases = ['https://rateyourmusic.com/artist/_unknown-artist']
SET person_e057484327fe.musicbrainz = 'https://musicbrainz.org/artist/125ec42a-7229-4250-afc5-e057484327fe'
SET person_e057484327fe.source = 'musicbrainz.org'
SET person_e057484327fe.timestamp = timestamp()

MERGE (work_4173a5617262:Work{ uuid: '63a5a050-fdd9-3239-9bc6-4173a5617262' })
SET work_4173a5617262.name = 'Artists Ought to Be Writing'
SET work_4173a5617262.source = 'musicbrainz.org'
SET work_4173a5617262.timestamp = timestamp()

MERGE (work_df9f8b62ff31:Work{ uuid: 'e39ea977-2833-3411-8d62-df9f8b62ff31' })
SET work_df9f8b62ff31.name = 'Break Down'
SET work_df9f8b62ff31.source = 'musicbrainz.org'
SET work_df9f8b62ff31.timestamp = timestamp()

MERGE (work_52fb6b80b058:Work{ uuid: 'a5d7efe1-6329-3a26-8af7-52fb6b80b058' })
SET work_52fb6b80b058.name = 'Lift Ev\'ry Voice and Sing'
SET work_52fb6b80b058.source = 'musicbrainz.org'
SET work_52fb6b80b058.timestamp = timestamp()

MERGE (work_f67dc2d44baa:Work{ uuid: '5c65f968-8058-31b9-8486-f67dc2d44baa' })
SET work_f67dc2d44baa.name = 'He Puts on his Coat and Leaves'
SET work_f67dc2d44baa.source = 'musicbrainz.org'
SET work_f67dc2d44baa.timestamp = timestamp()

MERGE (work_941dea22ee68:Work{ uuid: '1d4424e6-232d-33ff-8d23-941dea22ee68' })
SET work_941dea22ee68.name = 'Refraction 2'
SET work_941dea22ee68.source = 'musicbrainz.org'
SET work_941dea22ee68.timestamp = timestamp()

MERGE (work_aa871cebb55f:Work{ uuid: '83c741df-3a7b-38c8-a00d-aa871cebb55f' })
SET work_aa871cebb55f.name = 'Arizona Landscape'
SET work_aa871cebb55f.source = 'musicbrainz.org'
SET work_aa871cebb55f.timestamp = timestamp()

MERGE (work_9b8eb6573d81:Work{ uuid: 'b3db1dee-9e11-3a05-b440-9b8eb6573d81' })
SET work_9b8eb6573d81.name = 'Refraction 1'
SET work_9b8eb6573d81.source = 'musicbrainz.org'
SET work_9b8eb6573d81.timestamp = timestamp()

MERGE (work_b9a01d1ecd2e:Work{ uuid: '654d4e07-6558-36df-99bc-b9a01d1ecd2e' })
SET work_b9a01d1ecd2e.name = 'Cradle Song'
SET work_b9a01d1ecd2e.source = 'musicbrainz.org'
SET work_b9a01d1ecd2e.timestamp = timestamp()

MERGE (work_e4f7f5cd763a:Work{ uuid: '3f8e1ba4-9486-3bd9-9992-e4f7f5cd763a' })
SET work_e4f7f5cd763a.name = 'Milestone'
SET work_e4f7f5cd763a.source = 'musicbrainz.org'
SET work_e4f7f5cd763a.timestamp = timestamp()

MERGE (work_41ac3ff44a84:Work{ uuid: '974605da-5ebd-302e-b881-41ac3ff44a84' })
SET work_41ac3ff44a84.name = 'RAIN'
SET work_41ac3ff44a84.source = 'musicbrainz.org'
SET work_41ac3ff44a84.timestamp = timestamp()


// performances of
MERGE (perf_8d3c0bf33ff2)-[:PERFORMANCE_OF]->(work_4173a5617262)
MERGE (perf_dc32390daee8)-[:PERFORMANCE_OF]->(work_df9f8b62ff31)
MERGE (perf_d54648562734)-[:PERFORMANCE_OF]->(work_52fb6b80b058)
MERGE (perf_bc128d906daa)-[:PERFORMANCE_OF]->(work_f67dc2d44baa)
MERGE (perf_511640691c58)-[:PERFORMANCE_OF]->(work_941dea22ee68)
MERGE (perf_383359fcf76d)-[:PERFORMANCE_OF]->(work_aa871cebb55f)
MERGE (perf_573858841d75)-[:PERFORMANCE_OF]->(work_9b8eb6573d81)
MERGE (perf_f23b4d6e6800)-[:PERFORMANCE_OF]->(work_b9a01d1ecd2e)
MERGE (perf_67e758b67c75)-[:PERFORMANCE_OF]->(work_e4f7f5cd763a)
MERGE (perf_81550b001a94)-[:PERFORMANCE_OF]->(work_41ac3ff44a84)


// composers
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_4173a5617262)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_df9f8b62ff31)
MERGE (person_e057484327fe)-[:COMPOSED]->(work_52fb6b80b058)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_f67dc2d44baa)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_941dea22ee68)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_aa871cebb55f)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_9b8eb6573d81)
MERGE (person_c77d3a920abe)-[:COMPOSED]->(work_b9a01d1ecd2e)
MERGE (person_67b070680a78)-[:COMPOSED]->(work_e4f7f5cd763a)
MERGE (person_c65081d12d86)-[:COMPOSED]->(work_41ac3ff44a84)

MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_dc32390daee8)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_dc32390daee8)
MERGE (person_f5abd1c891d8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_dc32390daee8)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_dc32390daee8)
MERGE (person_ba0ce36d5a54)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_dc32390daee8)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_67e758b67c75)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_67e758b67c75)
MERGE (person_f5abd1c891d8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_67e758b67c75)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_67e758b67c75)
MERGE (person_67b070680a78)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_67e758b67c75)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_511640691c58)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_511640691c58)
MERGE (person_f5abd1c891d8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_511640691c58)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_511640691c58)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_f23b4d6e6800)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_f23b4d6e6800)
MERGE (person_f5abd1c891d8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_f23b4d6e6800)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_f23b4d6e6800)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_8d3c0bf33ff2)
MERGE (person_ba0ce36d5a54)-[:PARTICIPATED_IN { roles: ['singer'] }]->(perf_8d3c0bf33ff2)
MERGE (person_0d41405698ee)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_573858841d75)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_573858841d75)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_383359fcf76d)
MERGE (person_1e32b602b802)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['trumpet'] }]->(perf_81550b001a94)
MERGE (person_b5acc3932dcf)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['percussion'] }]->(perf_81550b001a94)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_81550b001a94)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_81550b001a94)
MERGE (person_f5abd1c891d8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_81550b001a94)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_81550b001a94)
MERGE (person_ab71e164ae60)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['bass'] }]->(perf_d54648562734)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_d54648562734)
MERGE (person_f5abd1c891d8)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['guitar'] }]->(perf_d54648562734)
MERGE (person_cf15b8735268)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['membranophone'] }]->(perf_d54648562734)
MERGE (person_c65081d12d86)-[:PARTICIPATED_IN { roles: ['musician'], instruments: ['piano'] }]->(perf_bc128d906daa)

