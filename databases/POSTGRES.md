# Postgresql
- [Postgresql Docs](https://www.postgresql.org/docs/manuals/)

##
- [PipelineDB Extension](https://www.pipelinedb.com/blog/pipelinedb-0-9-9-one-more-release-until-pipelinedb-is-a-postgresql-extension)
- [http://rhaas.blogspot.com/2018/01/do-or-undo-there-is-no-vacuum.html]
- [Scalable PostgreSQL - Streaming](https://blog.timescale.com/scalable-postgresql-high-availability-read-scalability-streaming-replication-fb95023e2af)
- [Fun with SQL recursive ctes](https://www.citusdata.com/blog/2018/05/15/fun-with-sql-recursive-ctes/)
- [When postgresql blocks](https://www.citusdata.com/blog/2018/02/15/when-postgresql-blocks/)


# Fix version issue

```bash
FATAL:  database files are incompatible with server
The data directory was initialized by PostgreSQL version 9.6, which is not compatible with this version 10.2.
```
Fix this issue with these directions
https://gist.github.com/giannisp/ebaca117ac9e44231421f04e7796d5ca


## Setup

Startup postgres server automatically
```bash
pg_ctl -D /usr/local/var/postgres start && brew services start postgresql
```

## LEARNING

### Cli commands
- [Postgres Data Types, Date, Timestamp, and Time Zones](https://tapoueh.org/blog/2018/04/postgresql-data-types-date-timestamp-and-time-zones/)
- [Favorite Postgres Queries](https://severalnines.com/blog/my-favorite-postgresql-queries-and-why-they-matter)

```bash
psql postgres - initial database setup

psql postgres -U username - login to database as user

CREATE ROLE username WITH LOGIN PASSWORD 'quoted password'; - setup user

ALTER ROLE username CREATEDB; - change permissions, add createdb permissions

CREATE DATABASE databasename; - create db

GRANT ALL PRIVILEGES ON DATABASE super_awesome_application TO username; - give all permissions

\du - view users

\q - quit cli

\list or \l  - list all databases on server

\connect DBNAME or \c DBNAME  - connect to database on server

\dt - table list of current database

\d+ TABLENAME - describe the table 
```



