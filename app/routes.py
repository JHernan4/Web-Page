#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from app import app
import requests
from flask import render_template, request, url_for, redirect, session
import json
import os
import os.path
import sys
import hashlib
import random
import math
from datetime import datetime
from flask import Flask, session, make_response
from app import database

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    cata = database.main()

    return render_template("index.html", catalogo=cata, registrado=0)

@app.route("/description", methods=['GET', 'POST'])
def description():
    pelicula = database.description(list(request.form)[2])
    return render_template("description.html", pelicula=pelicula, registrado = 0)


@app.route('/Sign_up', methods=['GET', 'POST'])
def Sign_up():
    if 'name' in request.form:
        name = request.form['name']
        password = request.form['password']
        username = request.form["username"]
        surname1 = request.form["surname1"]
        surname2 = request.form["surname2"]
        age = request.form["age"]
        email = request.form["mail"]
        phone = request.form['phone']
        if database.sign(username, password, name, surname1, surname2, age, email, phone) == False:
            return render_template("sign.html", mensajeError="Error al registrar. Revise sus datos")

        return render_template("index.html", catalogo=database.main(), registrado=1)
    else:
        return render_template("sign.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if 'username' in request.form:
        username = request.form['username']
        password = request.form['password']

        if database.login(username, password) == False:
            return render_template("login.html", mensajeError="Error to sign in. Please review username and/or password")

        return render_template("index.html", catalogo=database.main(), registrado=1)
    else:
        return render_template("login.html")

@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template("search.html")


@app.route("/result", methods=['GET', 'POST'])
def result():
    genero = request.form['genero']
    titulo = request.form['titulo']
    print(genero)
    if genero != "" and titulo == "":
        peliculas = database.busquedaPorGenero(genero)
    elif genero == "" and titulo != "":
        peliculas = database.busquedaPorTitulo(titulo)
    else:
        peliculas = database.busquedaHibrida(genero, titulo)

    return render_template("result.html", resultado=peliculas, genero=genero, titulo=titulo)
