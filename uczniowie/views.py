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
def dodajklase():
    """Dodawanie klasy"""
    form = dKlaseForm()

    if form.validate_on_submit():
        Klasa(nazwa=form.nazwa.data, roknaboru=form.roknaboru.data, rokmatury=form.rokmatury.data).save()
        return redirect(url_for('listaklas'))

    return render_template('dodajklase.html', form=form)

@app.route("/listaklas")
def listaklas():
    klasy = Klasa.select()
    return render_template('listaklas.html', klasy=klasy)

@app.route("/listauczniow")
def listauczniow():
    uczniowie = Uczen.select()
    return render_template('listauczniow.html', uczniowie=uczniowie)

@app.route("/dodajucznia", methods=['GET', 'POST'])
def dodajucznia():
    """Dodawanie uczniów"""
    form = dUczniaForm()
    form.klasa.choices = [(k.id, k.nazwa) for k in Klasa.select()]
    form.plec.choices = [(0, "Mężczyzna"), (1, "Kobieta")]

    if form.validate_on_submit():
        Uczen(imie=form.imie.data, nazwisko=form.nazwisko.data, plec=form.plec.data, klasa=form.klasa.data).save()
        return redirect(url_for('listauczniow'))

    return render_template('dodajucznia.html', form=form)

def get_or_404(kid):
    try:
        k = Klasa.get_by_id(kid)
        return k
    except Klasa.DoesNotExist:
        abort(404)

@app.route("/edycjaklasy")
def listaklasdoedycji():
    klasy = Klasa.select()
    return render_template('listaklasdoedycji.html', klasy=klasy)

@app.route("/edycjaklasy/<int:kid>", methods=['GET', 'POST'])
def edytujklase(kid):
  k = get_or_404(kid)
  form = dKlaseForm()

  if form.validate_on_submit():
    k.nazwa = form.nazwa.data
    k.roknaboru = form.roknaboru.data
    k.rokmatury = form.rokmatury.data
    k.save()
    return redirect(url_for('listaklas'))

  return render_template('edytujklase.html', form=form, iducznia=k)

@app.route("/edycjaucznia")
def listauczniowdoedycji():
    uczen = Uczen.select()
    return render_template('listauczniowdoedycji.html', uczniowie=uczen)

def get_ucznia_or_404(uid):
    try:
        u = Uczen.get_by_id(uid)
        return u
    except Uczen.DoesNotExist:
        abort(404)

@app.route("/edycjaucznia/<int:uid>", methods=['GET', 'POST'])
def edytujucznia(uid):
  u = get_ucznia_or_404(uid)
  form = dUczniaForm()
  form.klasa.choices = [(u.id, u.nazwa) for u in Klasa.select()]
  form.plec.choices = [(0, "Mężczyzna"), (1, "Kobieta")]

  if form.validate_on_submit():
    u.imie = form.imie.data
    u.nazwisko = form.nazwisko.data
    u.plec = form.plec.data
    u.klasa = form.klasa.data
    u.save()
    return redirect(url_for('listauczniow'))

  return render_template('edytujucznia.html', form=form, iducznia=u)
