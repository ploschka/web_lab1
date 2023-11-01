import sqlite3 as sql
import pandas as pd

con = sql.connect("store.sqlite")

df = pd.read_sql('''
                 SELECT a.name_author 'Автор', SUM(b.amount) 'Количество',
                 IFNULL(
                     'Меньше чем у ' ||
                     cast((lag(a.name_author) over diff) as text) ||
                     ' на ' ||
                     cast((lag(SUM(b.amount)) over diff - SUM(b.amount)) as text), '-'
                 ) AS 'Разница'
                 FROM author a
                 NATURAL JOIN book b
                 GROUP BY a.author_id
                 WINDOW diff as (order by SUM(b.amount) DESC)
                 ORDER BY 'Количество' DESC
                 ''', con)
print(df)
con.close()
