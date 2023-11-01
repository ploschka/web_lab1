import sqlite3 as sql
import pandas as pd

con = sql.connect("store.sqlite")

df = pd.read_sql('''
                 WITH average_amount(amount) AS
                 (
                  SELECT AVG(b.amount)
                  FROM book b
                 )
                 
                 SELECT *, IIF(b.amount<a.amount, floor(b.price) + 0.99, ceil(b.price) + 0.99) newprice
                 FROM book b, average_amount a
                 ''', con)

correct = '''
WITH average_amount(amount) AS
(
   SELECT AVG(b.amount)
   FROM book b
)

UPDATE book as b SET price = IIF(b.amount<a.amount, floor(b.price) + 0.99, ceil(b.price) + 0.99)
FROM average_amount a
'''

print(df)
con.close()

