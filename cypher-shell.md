# cypher-shell

See: https://neo4j.com/docs/operations-manual/current/tools/cypher-shell/

## Example

```shell
$ cypher-shell -a neo4j+s://551e5878.databases.neo4j.io:7687 -u neo4j -p **********
Connected to Neo4j using Bolt protocol version 5.0 at neo4j+s://551e5878.databases.neo4j.io:7687 as user neo4j.
Type :help for a list of available commands or :exit to exit the shell.
Note that Cypher queries must end with a semicolon.
neo4j@neo4j> 

```

## Running Cypher statements from a file as a cypher-shell argument

```shell
cat cql/busmans-holiday.cql | cypher-shell -a neo4j+s://551e5878.databases.neo4j.io:7687 -u neo4j -p ****** --format plain
```
