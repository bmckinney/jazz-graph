import kuzu

# Create an empty on-disk database and connect to it
db = kuzu.Database("./haynes_db")
conn = kuzu.Connection(db)

# Create schema

# Release Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Release(
        uuid STRING, 
        name STRING, 
        country STRING, 
        date STRING, 
        disambiguation STRING,
        discogs STRING,
        format STRING,
        discode STRING, 
        allmusic STRING,
        musicbrainz STRING, 
        source STRING, 
        PRIMARY KEY (uuid))
    """
)

# Event Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Event(
        uuid STRING, 
        name STRING, 
        date STRING, 
        type STRING, 
        musicbrainz STRING, 
        source STRING, 
        PRIMARY KEY (uuid))
    """""
)

# Person Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Person(
        uuid STRING, 
        name STRING, 
        gender STRING,
        country STRING, 
        disambiguation STRING,
        wikipedia STRING, 
        viaf STRING, 
        allmusic STRING, 
        bbc STRING, 
        discogs STRING, 
        wikidata STRING, 
        discographies STRING, 
        databases STRING[],
        musicbrainz STRING, 
        isni_list STRING,
        imdb STRING,
        source STRING, 
        PRIMARY KEY (uuid))
    """
)

# Label Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Label(
        uuid STRING, 
        name STRING, 
        PRIMARY KEY (uuid))
    """
)

# Performance Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Performance(
        uuid STRING, 
        name STRING, 
        disambiguation STRING,
        duration STRING, 
        begin_date STRING, 
        end_date STRING, 
        source STRING,
        PRIMARY KEY (uuid))
    """
)

# Work Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Work(
        uuid STRING, 
        name STRING, 
        type STRING, 
        iswc STRING,
        tags STRING[],
        databases STRING[],
        wikipedia STRING, 
        wikidata STRING, 
        musicbrainz STRING, 
        allmusic STRING,
        source STRING, 
        PRIMARY KEY (uuid))
    """
)

# Place Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Place(
        uuid STRING, 
        name STRING, 
        address STRING, 
        lat STRING, 
        lng STRING,
        source STRING, 
        PRIMARY KEY (uuid))
    """
)

# Release HAS_LABEL
conn.execute("CREATE REL TABLE IF NOT EXISTS HAS_LABEL(From Release TO Label)")

# Release HAS_TRACK
conn.execute("CREATE REL TABLE IF NOT EXISTS HAS_TRACK(From Release TO Performance, name STRING, sequence INT64)")

# PERFORMANCE_OF Work
conn.execute("CREATE REL TABLE IF NOT EXISTS PERFORMANCE_OF(From Performance TO Work, medley BOOLEAN)")

# Person COMPOSED Work
conn.execute("CREATE REL TABLE IF NOT EXISTS COMPOSED(From Person TO Work)")

# Person WROTE_LYRICS Work
conn.execute("CREATE REL TABLE IF NOT EXISTS WROTE_LYRICS(From Person TO Work)")

# Performance HAS_PLACE
conn.execute("CREATE REL TABLE IF NOT EXISTS GROUP HAS_PLACE(From Performance TO Place, From Event to Place, type STRING, begin_date STRING, end_date STRING)")

# Person PARTICIPATED_IN Performance
conn.execute("CREATE REL TABLE IF NOT EXISTS PARTICIPATED_IN(From Person TO Performance, roles STRING[], instruments STRING[])")

# Event HAS_PERFORMANCE
conn.execute("CREATE REL TABLE IF NOT EXISTS HAS_PERFORMANCE(From Event TO Performance, begin_date STRING, end_date STRING)")
