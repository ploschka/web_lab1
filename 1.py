import sqlite3 as sql
import pandas as pd

con = sql.connect("store.sqlite")

df = pd.read_sql('''                 
                 SELECT title as 'Название', name_genre as 'Жанр', amount as 'Количество', price as 'Цена'
                 FROM book
                 INNER JOIN genre ON book.genre_id = genre.genre_id
                 WHERE book.title NOT LIKE '% %'
                 AND ('Цена' < 500 OR 'Цена' > 700)
                 ORDER BY 'Название' ASC, 'Жанр' ASC
                 ''', con)
print(df)
con.close()
