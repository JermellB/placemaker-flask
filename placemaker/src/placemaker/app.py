__author__ = 'jermellbeane'
from flask import Flask
from flask.ext.api import FlaskAPI
app = FlaskAPI(__name__)
from flask import abort, render_template,request, jsonify
from flask.ext.api import status
from  models import CoC, Organization, Person
import json
import pickle
import pytz
import datetime
import mongoengine
from settings import MONGO_HOST, MONGO_DB
mongoengine.connect(MONGO_DB, host=MONGO_HOST)

'''
class CoC(mongoengine.DynamicDocument):
    pass

class Organization(mongoengine.DynamicDocument):
    pass

class Form(mongoengine.DynamicDocument):
    pass

class Question(mongoengine.DynamicDocument):
    pass

class Person(mongoengine.DynamicDocument):
    pass

class Users(mongoengine.DynamicDocument):
    pass
'''
#COCS
@app.route('/api/coc/create', methods=['POST'])
def create_coc():
    '''
    Create a Continuum of Care
    '''
    try:
        coc = CoC(date_created=pytz.utc.localize(datetime.datetime.now()),**request.form)
        coc.save(upsert=True)
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/coc/read/<_id>', methods=['GET'])
def read_coc(_id):
    '''
    Get a CoC
    '''
    try:
        coc = CoC(_id=_id)
        return coc.to_json()
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/coc/update/<_id>', methods=['POST'])
def update_coc(_id):
    '''
    Update a CoC
    '''
    try:
        coc = CoC(_id=_id, **request.form)
        coc.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/coc/delete/<_id>', methods=['POST'])
def delete_coc(_id):
    '''
    Delete a CoC
    '''
    try:
        coc = CoC(_id=_id)
        coc.delete()
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST


#ORGANIZATIONS
@app.route('/api/organization/create', methods=['POST'])
def create_organization():
    '''
    Create an Organization
    '''
    try:
        organization = Organization(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
        organization.save(upsert=True)
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/organization/read/<_id>', methods=['GET'])
def read_organization(_id):
    '''
    Get a organization
    '''
    try:
        organization = Organization(_id=_id)
        return organization.to_json()
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/organization/update/<_id>', methods=['POST'])
def update_organization(_id):
    '''
    Update a organization
    '''
    try:
        organization = Organization(_id=_id, **request.form)
        organization.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/organization/delete/<_id>', methods=['GET','POST'])
def delete_organization(_id):
    '''
    Delete a organization
    '''
    try:
        organization = Organization(_id=_id)
        organization.delete()
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

# PERSON
@app.route('/api/person/create', methods=['POST'])
def create_person():
    '''
    Create a Person
    '''
    try:
        person = Person(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
        person.save(upsert=True)
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/person/read/<_id>', methods=['GET'])
def read_person(_id):
    '''
    Get a person
    '''
    try:
        person = Person(_id=_id)
        return person.to_json()
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/person/update/<_id>', methods=['POST'])
def update_person(_id):
    '''
    Update a person
    '''
    try:
        person = Person(_id=_id, **request.form)
        person.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/person/delete/<_id>', methods=['GET', 'POST'])
def delete_person(_id):
    '''
    Delete a person
    '''
    try:
        person = Person(_id=_id)
        person.delete()
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

