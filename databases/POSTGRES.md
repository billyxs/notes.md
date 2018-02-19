# Postgresql

+ [http://rhaas.blogspot.com/2018/01/do-or-undo-there-is-no-vacuum.html]

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

`psql postgres` - initial database setup

`psql postgres -U username` - login to database as user

`CREATE ROLE username WITH LOGIN PASSWORD 'quoted password';` - setup user

`ALTER ROLE username CREATEDB;` - change permissions, add createdb permissions

`CREATE DATABASE databasename;` - create db

`GRANT ALL PRIVILEGES ON DATABASE super_awesome_application TO username;` - give all permissions

`\du` - view users

`\q` - quit cli

`\list` - list all databases on server

`\connect` - connect to database on server

`\dt` - list the tables currently connected on the server


## Todo

https://www.citusdata.com/blog/2018/02/15/when-postgresql-blocks/

