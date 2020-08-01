import os
import sys
import traceback
import time
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, text
from sqlalchemy.sql import select

TAX_CONSTANT = 15
CARRITO_STR = "Carrito"

# configurar el motor de sqlalchemy
db_engine = create_engine(
    "postgresql://alumnodb:alumnodb@localhost/webfilm", echo=False)
db_meta = MetaData(bind=db_engine)


def db_exceptiondbconn(db_conn):
    if db_conn is not None:
        db_conn.close()
        print("Exception in DB access:")
        print("-"*60)
        traceback.print_exc(file=sys.stderr)
        print("-"*60)
        print('Something is broken')
        return None


def caratulas():
    try:
        # CONEXION
        db_conn = db_engine.connect()

        # QUERY
        query = "select caratula from peliculas limit 10"

        # EJECUTAR QUERY
        db_result = db_conn.execute(query)

        # DESCONEXION
        db_conn.close()

        peliculas = []
        for element in db_result:
            peliculas.append(element[0])

        # DEVOLVER
        if len(peliculas) == 0:
            return None
        else:
            return peliculas

    # EXCEPCION BASE DE DATOS
    except:
        return db_exceptiondbconn(db_conn)

def titulos():
        try:
            # CONEXION
            db_conn = db_engine.connect()

            # QUERY
            query = "select title from peliculas limit 10"

            # EJECUTAR QUERY
            db_result = db_conn.execute(query)

            # DESCONEXION
            db_conn.close()

            peliculas = []
            for element in db_result:
                peliculas.append(element[0])

            # DEVOLVER
            if len(peliculas) == 0:
                return None
            else:
                return peliculas

        # EXCEPCION BASE DE DATOS
        except:
            return db_exceptiondbconn(db_conn)

def description(pelicula):

        try:
            # CONEXION
            db_conn = db_engine.connect()

            # QUERY
            query = "select caratula, title, sinopsis, price from peliculas where title = '{}'".format(pelicula)

            # EJECUTAR QUERY
            db_result = db_conn.execute(query)

            # DESCONEXION
            db_conn.close()


            for element in db_result:
                peliculas = element

            # DEVOLVER
            if peliculas == None:
                return None
            else:
                return peliculas

        # EXCEPCION BASE DE DATOS
        except:
            return db_exceptiondbconn(db_conn)
