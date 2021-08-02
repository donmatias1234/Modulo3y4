import requests  #libreria necearia para obtancion de la web
import csv       #libreria para trabajar archivo csv de forma eficiente

url= 'https://datahub.io/core/population/r/population.csv' #asiganmos a una var la 'direccion' de los datos
response= requests.get(url)  #respuesta obtenida del get en el url
headers ={'User-Agent' : 'AppleWebKit/605.1.15'}  #necesario solo si tenemos que asociar el browser

if response.status_code != 200:    #si no entra a este if fue porque no hubo problema con la pagina, existia
    print('Failed to get data', response.status_code)
else:
    wrapper = csv.reader(response.text.strip().split('\n'))   #objeto con lo que se leyó del archivo csv en filas
    #csv.reader permite la lectura de un archivo (es un texto)
    #respose.text es el contenido de la respuesta
    #strip() elimina los blancos del comienzo y del final
    #split('\n') esta funcion corta la lineas (en vez de un texto entero) seerados por un newline
        #si encuentra un \n corta la fila y comineza otra
    first = next(wrapper)   #el primer wrapper son los encabezados, por eso lo avanzo con esta instrucción
    for record in wrapper:   #este for recorre completo las filas del wrapper
        country = record[0]
        year = int(record[2])   #las API casi siemore dan string, convertir los valores segun el tipo que se requiere
        population =record[3]
        #print(country, year, population)
        if (year>2010 and country == 'Chile'):
           print(country, year, population)