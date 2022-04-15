# Pyj Db

- Explore how databases are built


## Steps

- Day 1
    - `select 1 + 1`: Parser.
    - `create table tab (x int, y char)`: Creating tables.
    - `select x from tab`: Querying from tables.
- Day 2
    - `insert into tab (x, y) values (1, 'x')`: Inserting into tables.
    - `select y from tab where x = 10`: Speed measurement.
    - `select y from tab where x = 10`: Indexing.
- Day 3
    - `select x from tab where x + 1 < 10`: Query optimization
    - `select/delete x from tab where x = 10`: Locking / WAL
