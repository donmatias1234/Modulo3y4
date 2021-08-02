import mysql.connector as db

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "dino1994",
    database = "Cine"
)

miCursor = mydb.cursor()
sqlCrearBD= 'CREATE DATABASE Cine'
#miCursor.execute(sqlCrearBD)

##Despues de crear la tabla vacia tengo que cambiar el database del conector para poder crear las tablas en la BD que acabo de crear

sqlCrearMovies= 'CREATE TABLE movies(id INT PRIMARY KEY, name VARCHAR(50), year INT, `rank` FLOAT)' #rank es una palabra reservada
sqlCrearActors= 'CREATE TABLE actors(id INT PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30))'
sqlCrearDirectors= 'CREATE TABLE directors(id INT PRIMARY KEY, first_name VARCHAR(30), last_name VARCHAR(30))'
sqlCrearMoviesActors= 'CREATE TABLE movies_actors(actor_id INT REFERENCES actors(id), movie_id INT REFERENCES movies(id), role VARCHAR(100), PRIMARY KEY (actor_id, movie_id))' # - Al poner esta declaracion de primarey key (al final con una coma antes) me tira error
sqlCrearMoviesDirectors= 'CREATE TABLE movies_directors(director_id INT REFERENCES directors(id), movie_id INT REFERENCES movies(id), PRIMARY KEY (director_id, movie_id))' #  - Al poner esta declaracion de primarey key (al final con una coma antes) me tira error


#miCursor.execute(sqlCrearMovies)
#miCursor.execute(sqlCrearActors)
#miCursor.execute(sqlCrearDirectors)
#miCursor.execute(sqlCrearMoviesActors)
#miCursor.execute(sqlCrearMoviesDirectors)

#mydb.commit()
