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

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_DIR = os.path.join(BASE_DIR + "/app/", "usuarios")
catalogue_data = open(os.path.join(app.root_path, 'catalogue/catalogue.json'), encoding="utf-8").read()
catalogue = json.loads(catalogue_data)
peliculas = catalogue['peliculas']

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    cata = []
    for c, t in zip(database.caratulas(), database.titulos()):
        cata.append((c, t))
    print (cata)

    return render_template("index.html", catalogo=cata, registrado=0)

@app.route("/description", methods=['GET', 'POST'])
def description():
    pelicula = database.description(list(request.form)[2])
    return render_template("description.html", pelicula=pelicula, registrado = 0)


@app.route('/Sign_up', methods=['GET', 'POST'])
def Sign_up():
    return render_template("sign.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html")

@app.route("/search", methods=['GET', 'POST'])
def search():
    return render_template("search.html")
