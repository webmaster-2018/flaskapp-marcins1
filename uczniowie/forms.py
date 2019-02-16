# -*- coding: utf-8 -*-
# quiz-orm/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, HiddenField, FieldList, IntegerField
from wtforms import SelectField, FormField, BooleanField
from wtforms.validators import Required

blad1 = 'To pole jest wymagane'


class dKlaseForm(FlaskForm):
    id = HiddenField()
    nazwa = StringField('Nazwa klasy:', validators=[Required(message=blad1)])
    roknaboru = IntegerField('Rok naboru:', validators=[Required(message=blad1)])
    rokmatury = IntegerField('Rok matury:', validators=[Required(message=blad1)])

class dUczniaForm(FlaskForm):
    id = HiddenField()
    imie = StringField('Imię:', validators=[Required(message=blad1)])
    nazwisko = StringField('Nazwisko:', validators=[Required(message=blad1)])
    plec = SelectField('Płeć:', coerce=int)
    klasa = SelectField('Klasa:', coerce=int)
