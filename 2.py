import sqlite3 as sql
import pandas as pd

con = sql.connect("store.sqlite")

df = pd.read_sql('''
                 SELECT DISTINCT client.name_client, buy_book.amount 
                 FROM buy_book
                 INNER JOIN buy ON buy_book.book_id = buy.buy_id
                 INNER JOIN client ON buy.buy_id = client.client_id
                 WHERE buy_book.amount >= 2
                 ORDER BY client.name_client ASC
                 ''', con)
print(df)
con.close()
