import sqlite3 as sql
import pandas as pd

con = sql.connect("store.sqlite")

df = pd.read_sql('''
                 WITH
                 city_count_client (city_id, name_city, count) AS
                 (
                 SELECT ci.city_id, ci.name_city, COUNT(DISTINCT ci.city_id)
                 FROM client cl
                 NATURAL JOIN city ci
                 NATURAL JOIN buy
                 GROUP BY ci.city_id
                 ),

                 max_clients (count) AS
                 (
                 SELECT MAX(count)
                 FROM city_count_client
                 ),

                 city_with_max(city_id, name_city) AS
                 (
                 SELECT city_id, name_city
                 FROM city_count_client
                 NATURAL JOIN max_clients
                 )

                 SELECT DISTINCT title, name_author
                 FROM city_with_max
                 NATURAL JOIN client
                 NATURAL JOIN buy
                 NATURAL JOIN buy_book bb
                 INNER JOIN book b ON bb.book_id = b.book_id
                 NATURAL JOIN author

                 ''', con)

print(df)
con.close()
