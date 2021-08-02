import mysql.connector as db
import pandas as pd
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "dino1994",
    database = "Cine"
)

miCursor = mydb.cursor()

sqlSentence= 'SELECT m.name as Pelicula, m.year AS Agno, d.last_name AS `Director`,\
m.rank AS `Puntaje`\
FROM (movies_directors AS md JOIN movies AS m ON m.id = md.movie_id)\
JOIN directors AS d ON d.id = director_id WHERE m.rank is not null and m.rank>8 ORDER BY m.rank DESC'

miCursor.execute(sqlSentence)
rows = miCursor.fetchall()
lista =[]
for row in rows:
#con la instrucción de abajo vamos a ir llenando la lista, fila por fila
  lista.append(row)
df1 = pd.DataFrame(lista, columns=['Pelicula', 'Agno', 'Director', 'Puntaje'])
print(df1.loc[0:10, ['Pelicula', 'Puntaje']])
print(df1.iloc[20:50, 0:4])
