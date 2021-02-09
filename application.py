#!/usr/bin/env python3
# __author__ = "Benji Martinez"
# __copyright__ = "Copyright 2020, Benji Martinez"
# __credits__ = ["Benji Martinez"]
# __maintainer__ = "Benji Martinez"
# __email__ = "iot.aplicaciones@outlook.com"

from os import scandir, getcwd
import json
import random
import time, os
from datetime import datetime
from flask import Flask, Response, render_template
from sqlite3 import Error
import sqlite3

def sqlite_revision():
    try:
        con = sqlite3.connect('database/temperatura.db')
        cursor = con.cursor()

        cursor.execute("SELECT * FROM medicion")

        mediciones = cursor.fetchall()

        con.commit()
        con.close()

        return len(mediciones)

    except Error:
        print(Error)
        return False

def sqlite_traer():
    try:
        con = sqlite3.connect('database/temperatura.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM medicion ORDER BY id DESC LIMIT 1")
        usuario = cursor.fetchone()
        
        con.commit()
        con.close()

        return usuario

    except Error:
        print(Error)
        return False

def imagenpath(ruta, file):
    for arch in scandir(ruta):
        if arch.is_file():
            if (arch.name == file):
                return True
            else:
                return False

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/print-data')
def chart_data():
    def generate_random_data():
        while True:

            filas = sqlite_revision()

            if (filas == 0):
                temperatura = 0
                bandera = False
                hora = '00:00:00'
                fecha = 'YYYY-MM-DD'
                nombre = 'Benji Martinez Fl.'
                imagen = 'sinperfil.png'
                num_emp = 0

            else:
                basedir = os.path.abspath(os.path.dirname(__file__))+'/static/img'
                user = sqlite_traer()
                id, num_emp, nombre, imagen, temperatura, fecha, hora, totem = user
                bandera = imagenpath(basedir, imagen)

            json_data = json.dumps(
                {'num_emp':num_emp, 'nombre':nombre, 'imagen':imagen, 'temperatura': temperatura, 'fecha': fecha, 'hora': hora, 'bandera': bandera, 'filas': filas})
            yield f"data:{json_data}\n\n"
            time.sleep(4)
    return Response(generate_random_data(), mimetype='text/event-stream')


if __name__ == '__main__':
    application.run(debug=True, threaded=True)