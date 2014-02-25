-- Graph (with fixed N) object for database

CREATE TABLE graph(
       graph_id   INTEGER PRIMARY KEY AUTOINCREMENT,
       adj        UNSIGNED BIG INT NOT NULL
);
