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


def main():
    try:
        # CONEXION
        db_conn = db_engine.connect()

        # QUERY
        query = "select caratula, title from peliculas limit 10"

        # EJECUTAR QUERY
        db_result = db_conn.execute(query)

        # DESCONEXION
        db_conn.close()

        peliculas = []
        for element in db_result:
            peliculas.append(element)

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


def busquedaPorGenero(genero):

            try:
                # CONEXION
                db_conn = db_engine.connect()

                # QUERY
                query = "select title, caratula from peliculas where genero = '{}'".format(genero)

                # EJECUTAR QUERY
                db_result = db_conn.execute(query)

                # DESCONEXION
                db_conn.close()

                peliculas = []
                for element in db_result:
                    peliculas.append(element)

                # DEVOLVER
                if len(peliculas) == 0:
                    return None
                else:
                    return peliculas

            # EXCEPCION BASE DE DATOS
            except:
                return db_exceptiondbconn(db_conn)

def busquedaPorTitulo(titulo):
        try:
            # CONEXION
            db_conn = db_engine.connect()
            # QUERY
            query = "select title, caratula from peliculas where title = '{}'".format(titulo)
            # EJECUTAR QUERY
            db_result = db_conn.execute(query)
            # DESCONEXION
            db_conn.close()
            peliculas = []
            for element in db_result:
                peliculas.append(element)
            # DEVOLVER
                if len(peliculas) == 0:
                    return None
                else:
                    return peliculas

        # EXCEPCION BASE DE DATOS
        except:
            return db_exceptiondbconn(db_conn)

def busquedaHibrida(genero, titulo):
        try:
            # CONEXION
            db_conn = db_engine.connect()
            # QUERY
            query = "select title, caratula from peliculas where title = '{}' and genero ='{}'".format(titulo, genero)
            # EJECUTAR QUERY
            db_result = db_conn.execute(query)
            # DESCONEXION
            db_conn.close()
            peliculas = []
            for element in db_result:
                peliculas.append(element)
            # DEVOLVER
                if len(peliculas) == 0:
                    return None
                else:
                    return peliculas

        # EXCEPCION BASE DE DATOS
        except:
            return db_exceptiondbconn(db_conn)

def login(username, password):
    try:
        db_conn = db_engine.connect()
        query = "select username from usuarios where username = '{}' and password = '{}'".format(username, password)
        db_result = db_conn.execute(query)
        db_conn.close()
        if len(list(db_result)) == 1:
            return True
        else:
            return False
    except:
        return db_exceptiondbconn(db_conn)


def existeUsuario(username):
        try:
            db_conn = db_engine.connect()
            query = "select username from usuarios where username = '{}'".format(username)
            db_result = db_conn.execute(query)
            db_conn.close()
            if len(list(db_result)) == 0:
                return True
            else:
                return False
        except:
            return db_exceptiondbconn(db_conn)

def sign (username, password, name, surname1, surname2, age, email, phone):
        try:
            db_conn = db_engine.connect()
            if existeUsuario(username)==False:
                return False
            else:
                query = "insert into usuarios (username, password, name, surname1, surname2, age, email, phone) values ('{}', '{}', '{}', '{}', '{}', {}, '{}', '{}')".format(username, password, name, surname1, surname2, age, email, phone)
                db_result = db_conn.execute(query)
                db_conn.close()
                return True
        except:
            return db_exceptiondbconn(db_conn)
