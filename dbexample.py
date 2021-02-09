from datetime import datetime
from sqlite3 import Error
import sqlite3
import time


def sqlite_insert(entidades):
    try:
        con = sqlite3.connect('database/temperatura.db')
        cursor = con.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS medicion (id integer PRIMARY KEY, num_emp integer, nombre text, imagen text, temperatura real, fecha text, hora text, totem integer)")

        cursor.execute('INSERT INTO medicion (num_emp, nombre, imagen, temperatura, fecha, hora, totem) VALUES(?, ?, ?, ?, ?, ?, ?)', entidades)
        con.commit()
        con.close()

    except Error:
        print(Error)
        return False
    

def format_fecha_actual(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{}-de-{}-del-{}".format(day, month, year)

    return messsage

fecha_c = datetime.now()
fecha = (format_fecha_actual(fecha_c))
hora = time.strftime("%H:%M:%S")
totem = 1

#entidades = (100, 'Ada Lovelace', 'Ada.jpg', 36.5, fecha, hora, totem)
entidades = (3, 'Deyair L', 'deyair.jpg', 36.5, fecha, hora, totem)
sqlite_insert(entidades)