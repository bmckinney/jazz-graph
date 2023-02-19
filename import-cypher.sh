#!/bin/sh

# export .env vars
[ ! -f .env ] || export $(grep -v '^#' .env | xargs)

# Note: server terminates if we don't chunk these:
#    importing cql/kind-of-blue-data.cql...
#    Server at 551e5878.databases.neo4j.io:7687 is no longer available
#    importing cql/mjq-white-house-event-data.cql...
#    Connection to the database terminated. Please ensure that your database is listening on the correct host...

cypher_batch1=(
 amazing-bud-powell-data
 bravo-brubeck
 brubeck-all-the-things-we-are
 busmans-holiday
 cracklin-data
)
cypher_batch2=(
 cymbalism-data
 getz-jazz-goes-to-college
 hawes-live-at-the-jazz-showcase-vol-1
 just-us-data
 kind-of-blue-data
)
cypher_batch3=(
 mjq-white-house-event-data
 out-of-the-afternoon-data
 roy-haynes-colbert-data
 roy-haynes-trio-data
 roy-haynes-white-house-data
)
cypher_batch4=(
 screamin-the-blues-data
 the-great-kai-data
 we-three-data
 the-blues-and-the-abstract-truth
)
cypher_batch5=(
 whereas
 roy-alty
 cymbalism
 fountain-of-youth
 praise
)

echo starting imports

# batch
for cypher in "${cypher_batch5[@]}"; do
echo importing cql/$cypher.cql...
cat cql/$cypher.cql | cypher-shell -a $NEO4J_SERVER -u $NEO4J_USER -p $NEO4J_PASSWORD --format plain
done

echo done