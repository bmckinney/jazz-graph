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
        links STRING[],
        PRIMARY KEY (uuid))
    """""
)

# Person Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Person(
        uuid STRING, 
        name STRING, 
        aliases STRING[],
        birth_date STRING,
        death_date STRING,
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

# Annotation Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Annotation(
        uuid STRING, 
        name STRING, 
        type STRING, 
        date STRING,
        content STRING,
        citation STRING,
        databases STRING[],
        tags STRING[],
        PRIMARY KEY (uuid))
    """
)

# Video Node
conn.execute(
    """
    CREATE NODE TABLE IF NOT EXISTS Video(
        uuid STRING, 
        name STRING, 
        creator STRING,
        date STRING,
        begin_timestamp STRING,
        end_timestamp STRING,
        duration STRING,
        citation STRING,
        links STRING[],
        tags STRING[],
        PRIMARY KEY (uuid))
    """
)


# Release HAS_LABEL
conn.execute("CREATE REL TABLE IF NOT EXISTS HAS_LABEL(FROM Release TO Label)")

# Release, Performance, Work, Event, Person HAS_ANNOTATION
conn.execute("CREATE REL TABLE GROUP IF NOT EXISTS HAS_ANNOTATION(FROM Release TO Annotation, FROM Performance TO Annotation, FROM Work TO Annotation, FROM Event TO Annotation, FROM Person TO Annotation)")

# Release, Performance, Event HAS_Video
conn.execute("CREATE REL TABLE GROUP IF NOT EXISTS HAS_VIDEO(FROM Release TO Video, FROM Performance TO Video, FROM Event TO Video, begin_timestamp STRING, end_timestamp STRING)")

# Release HAS_TRACK
conn.execute("CREATE REL TABLE IF NOT EXISTS HAS_TRACK(FROM Release TO Performance, name STRING, sequence INT64)")

# PERFORMANCE_OF Work
conn.execute("CREATE REL TABLE IF NOT EXISTS PERFORMANCE_OF(FROM Performance TO Work, medley BOOLEAN)")

# Person COMPOSED Work
conn.execute("CREATE REL TABLE IF NOT EXISTS COMPOSED(FROM Person TO Work)")

# Person CREATED Annotation
conn.execute("CREATE REL TABLE IF NOT EXISTS CREATED(FROM Person TO Annotation, role STRING)")

# Person CREATED Video
conn.execute("CREATE REL TABLE IF NOT EXISTS CREATED(FROM Person TO Video, role STRING)")

# Person WROTE_LYRICS Work
conn.execute("CREATE REL TABLE IF NOT EXISTS WROTE_LYRICS(FROM Person TO Work)")

# Performance HAS_PLACE
conn.execute("CREATE REL TABLE GROUP IF NOT EXISTS HAS_PLACE(FROM Performance TO Place, FROM Event to Place, type STRING, begin_date STRING, end_date STRING)")

# Person PARTICIPATED_IN Performance
conn.execute("CREATE REL TABLE IF NOT EXISTS PARTICIPATED_IN(FROM Person TO Performance, roles STRING[], instruments STRING[])")

# Event HAS_PERFORMANCE
conn.execute("CREATE REL TABLE IF NOT EXISTS HAS_PERFORMANCE(FROM Event TO Performance, begin_date STRING, end_date STRING)")
