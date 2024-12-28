# Kuzu db implementation

## GitHub Repos

- [https://github.com/kuzudb/kuzu](kuzudb/kuzu)
- [https://github.com/kuzudb/explorer](kuzudb/explorer)
- [https://github.com/kuzudb/api-server](kuzudb/api-server)
- [https://github.com/Connected-Data/cdkg-challenge](cdkg-challenge)

## Installation

See: [https://docs.kuzudb.com/installation/](https://docs.kuzudb.com/installation/)

## Run explorer in docker

```
docker run -d -p 8000:80 -v /absolute_path/haynes_db:/database -e MODE=READ_ONLY --rm kuzudb/explorer:latest

```