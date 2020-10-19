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
    if not 'login' in session:
        return render_template("index.html", catalogo=cata, registrado=0)
    else:
        return render_template("index.html", catalogo=cata, registrado=session['login'])

@app.route("/description", methods=['GET', 'POST'])
def description():
    pelicula = database.description(list(request.form)[2])
    return render_template("description.html", pelicula=pelicula, registrado = session['login'])


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
        hash = hashlib.sha256()
        aux =  hash.update(str.encode(password))
        secure_password = hashlib.sha256(str.encode(password)).hexdigest()


        if database.sign(username, str(secure_password), name, surname1, surname2, age, email, phone) == False:
            return render_template("sign.html", mensajeError="Error al registrar. Revise sus datos")
        #implementation of session storage
        session['username'] = username
        session['compra'] = []
        session['login'] = 1
        session.modified = True
        return render_template("index.html", catalogo=database.main(), registrado=session['login'], user = session['username'])
    else:
        return render_template("sign.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    regexname = "^[a-zA-Z0-9_.-]+$"
    lastusercookie = request.cookies.get('lastuser')
    if 'username' in request.form:
        username = request.form['username']
        password = hashlib.sha256(str.encode(request.form['password'])).hexdigest()

        if database.login(username, str(password)) == False:
            return render_template("login.html", mensajeError="Error to sign in. Please review username and/or password")

        session['username'] = username
        session['compra'] = []
        session['login'] = 1
        return render_template("index.html", catalogo=database.main(), registrado=session['login'], user = session['username'])
    else:
        return render_template("login.html")
@app.route("/Sign_out", methods=['GET', 'POST'])
def Sign_out():
    if 'username' in session:
        session.pop("username")
        session["compra"] = []
        session.pop("login")
        return redirect(url_for('index'))


@app.route("/Profile", methods=['GET', 'POST'])
def Profile():
    if 'username' in session:
        print("Voy a pedir info de {}".format(session['username']))
        info = database.getInfo(session['username'])
        print(info)
        return render_template("profile.html", info = info, user=info[0][0])



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
@app.route("/update", methods=['GET', 'POST'])
def update():
    if database.update(request.args.get('u'), request.args.get('a')) == True:
        return "OK"

@app.route("/add_money", methods=['GET', 'POST'])
def add_money():
    info = database.add_money(request.args.get('u'), request.args.get('m'))
    res = "<h3>Salary: "+str(info)+"€</h3>"
    return res
