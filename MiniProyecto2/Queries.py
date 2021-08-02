import mysql.connector as db
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "dino1994",
    database = "Cine"
)

miCursor = mydb.cursor()
'''
sqlSentence= 'SELECT d.last_name, d.first_name, COUNT(movie_id) AS How_Many \
    FROM movies_directors AS md JOIN directors AS d ON d.id = \
    md.director_id\
    GROUP by d.last_name, d.first_name\
    HAVING COUNT(movie_id) > 3\
    ORDER BY COUNT(movie_id) DESC'

miCursor.execute(sqlSentence)
rows = miCursor.fetchall()
for row in rows:
    print(row)
'''
#####################################################################################
'''
sqlSentence= 'SELECT a.last_name, a.first_name, COUNT(movie_id) \
    FROM actors AS a JOIN movies_actors as ma ON ma.actor_id = a.id \
    GROUP BY a.last_name, a.first_name\
    ORDER BY a.last_name, a.first_name'

miCursor.execute(sqlSentence)
rows = miCursor.fetchall()
for row in rows:
    print(row)
'''
##################################################################################

sqlSentence= 'SELECT m.name as `Movie`, m.year AS `Year`, d.last_name AS `Director`,\
m.rank AS `Ranking`\
FROM (movies_directors AS md JOIN movies AS m ON m.id = md.movie_id)\
JOIN directors AS d ON d.id = director_id WHERE m.rank is not null and m.rank>8 ORDER BY m.rank DESC'

miCursor.execute(sqlSentence)
rows = miCursor.fetchall()
for row in rows:
    print(row)
