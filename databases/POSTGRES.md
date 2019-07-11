# Postgresql
- [Postgresql Docs](https://www.postgresql.org/docs/manuals/)

##
- [PipelineDB Extension](https://www.pipelinedb.com/blog/pipelinedb-0-9-9-one-more-release-until-pipelinedb-is-a-postgresql-extension)
- [http://rhaas.blogspot.com/2018/01/do-or-undo-there-is-no-vacuum.html]
- [Scalable PostgreSQL - Streaming](https://blog.timescale.com/scalable-postgresql-high-availability-read-scalability-streaming-replication-fb95023e2af)
- [Fun with SQL recursive ctes](https://www.citusdata.com/blog/2018/05/15/fun-with-sql-recursive-ctes/)
- [When postgresql blocks](https://www.citusdata.com/blog/2018/02/15/when-postgresql-blocks/)
- [The power of storing JSON in postgres](https://blog.codeship.com/unleash-the-power-of-storing-json-in-postgres/)


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

*Setup errors?*

`FATAL: database files are incompatible with server`
https://stackoverflow.com/questions/17822974/postgres-fatal-database-files-are-incompatible-with-server

Remove the other postgres files and initialize a new one

```bash
rm -rf /usr/local/var/postgres
initdb /usr/local/var/postgres -E utf8
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

CREATE TABLE TableName {
  TableColumnTitle DATA_TYPE constraints,
  table_constraint
  table_constraint
} INHERITS ExistingTableToInheritFrom

CREATE TABLE account(
 user_id serial PRIMARY KEY,
 username VARCHAR (50) UNIQUE NOT NULL,
 password VARCHAR (50) NOT NULL,
 email VARCHAR (355) UNIQUE NOT NULL,
 created_on TIMESTAMP NOT NULL,
 last_login TIMESTAMP
);

\du - view users

\q - quit cli

\list or \l  - list all databases on server

\connect DBNAME or \c DBNAME  - connect to database on server

\dt - table list of current database

\d+ TABLENAME - describe the table 
```


## Examples

Concating queries together

*For some reason we have duplicate county IDs and need to pull this list together*

**UNION ALL**
```sql
SELECT * FROM public."MyTable" 
	WHERE 
		"MyTable"."StateProvince" = 'CA' 
	AND 
		"MyTable"."CountyId" IN (2, 3, 4, 5) 
UNION ALL
SELECT * FROM public."ClientPricePoint" 
	WHERE 
		"MyTable"."StateProvince" = 'NY' 
	AND 
		"MyTable"."CountyId" IN (4, 5, 17, 20) 
```

**Another way**
```sql
SELECT * FROM public."MyTable" 
	WHERE 
    1 =1
  AND (
      "MyTable"."StateProvince" = 'CA' 
    AND 
      "MyTable"."CountyId" IN (2, 3, 4, 5) 
  )
  OR
  (
      "MyTable"."StateProvince" = 'NY' 
    AND 
      "MyTable"."CountyId" IN (4, 5, 17, 20) 
  )
```
