# this page will contain forms using the form-wtf plugin for Flask
# Classes represent individual quizes and then fields are the vars
# inside each class.

import flask_wtf as wtf
import models as ml
from wtforms import StringField, IntegerField, SelectField, DateField
from wtforms.validators import DataRequired, EqualTo, Required

class Settings_Search(wtf.FlaskForm):
    search_name = StringField('name', validators=[DataRequired()])

class Create_Dataset(wtf.FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    # get the search types available
    res = ml.Search_Names.query.all()
    search_type = SelectField(u'Search Type', coerce=str, validators=[Required("Please enter your name.")], choices=[(str(r.id), r.name) for r in res])
    year_start = DateField('year_start', validators=[Required("Please enter the correct date.")], format='%Y')
    year_end = DateField('year_end', validators=[Required("Please enter the correct date.")], format='%Y')
    access = IntegerField('access_id')

class Edit_Dataset(wtf.FlaskForm):
    name = StringField('name')
    # get the search types available
    res = ml.Search_Names.query.all()
    search_type = SelectField(u'Search Type', coerce=str, choices=[(str(r.id), r.name) for r in res])
    year_start = DateField('year_start')
    year_end = DateField('year_end')
    access = IntegerField('access_id')
