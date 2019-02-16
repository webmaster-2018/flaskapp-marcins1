# -*- coding: utf-8 -*-
# quiz-orm/views.py

from flask import Flask
from flask import render_template, request, redirect, url_for, abort, flash
from modele import *
from forms import *

app = Flask(__name__)

@app.route('/')
def index():
    """Strona główna"""
    return render_template('index.html')

@app.route("/dodajklase", methods=['GET', 'POST'])
def dodaj():
    """Dodawanie klasy"""
    form = dKlaseForm()

    if form.validate_on_submit():
        Klasa(nazwa=form.nazwa.data, roknaboru=form.roknaboru.data, rokmatury=form.rokmatury.data).save()
        return redirect(url_for('index'))

    return render_template('dodajklase.html', form=form)

@app.route("/listaklas")
def lista():
    klasy = Klasa.select()
    return render_template('listaklas.html', klasy=klasy)
