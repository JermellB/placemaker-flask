__author__ = 'jermellbeane'
from flask import Flask
from flask_api import FlaskAPI, status
app = FlaskAPI(__name__)
from flask import request
from  models import CoC, Organization, Person, User, Form, Question
import pytz
import json
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

@app.route('/')
def api_root():
    return 'HELLO'

#COCS
@app.route('/api/coc/create', methods=['POST'])
def create_coc():
    '''
    Create a Continuum of Care
    '''
    try:
        coc = CoC(date_created=pytz.utc.localize(datetime.datetime.now()),**json.loads(request.form))
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
        coc = CoC(_id=_id, **json.loads(request.form))
        coc.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/coc/delete/<_id>', methods=['GET'])
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
        organization = Organization(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.form))
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
        organization = Organization(_id=_id, **json.loads(request.form))
        organization.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/organization/delete/<_id>', methods=['GET'])
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
        person = Person(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.form))
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
        person = Person(_id=_id, **json.loads(request.form))
        person.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/person/delete/<_id>', methods=['GET'])
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

# USER
@app.route('/api/user/create', methods=['POST'])
def create_user():
    '''
    Create a User
    '''
    try:
        user = User(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.form))
        user.save(upsert=True)
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/user/read/<_id>', methods=['GET'])
def read_user(_id):
    '''
    Get a user
    '''
    try:
        user = User(_id=_id)
        return user.to_json()
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/user/update/<_id>', methods=['POST'])
def update_user(_id):
    '''
    Update a user
    '''
    try:
        user = User(_id=_id, **json.loads(request.form))
        user.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST


@app.route('/api/user/delete/<_id>', methods=['GET'])
def delete_user(_id):
    '''
    Delete a user
    '''
    try:
        user = User(_id=_id)
        user.delete()
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

#FORM
@app.route('/api/form/create', methods=['POST'])
def create_form():
    '''
    Create a Form
    '''
    try:
        form = Form(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.form))
        form.save(upsert=True)
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/form/read/<_id>', methods=['GET'])
def read_form(_id):
    '''
    Get a form
    '''
    try:
        form = Form(_id=_id)
        return form.to_json()
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/form/update/<_id>', methods=['POST'])
def update_form(_id):
    '''
    Update a form
    '''
    try:
        form = Form(_id=_id, **json.loads(request.form))
        form.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST


@app.route('/api/form/delete/<_id>', methods=['GET'])
def delete_form(_id):
    '''
    Delete a form
    '''
    try:
        form = Form(_id=_id)
        form.delete()
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

#Question
@app.route('/api/question/create', methods=['POST'])
def create_question():
    '''
    Create a Question
    '''
    try:
        question = Question(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.form))
        question.save(upsert=True)
        return status.HTTP_201_CREATED
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/question/read/<_id>', methods=['GET'])
def read_question(_id):
    '''
    Get a question
    '''
    try:
        question = Question(_id=_id)
        return question.to_json()
    except:
        return status.HTTP_400_BAD_REQUEST

@app.route('/api/question/update/<_id>', methods=['POST'])
def update_question(_id):
    '''
    Update a question
    '''
    try:
        question = Question(_id=_id, **json.loads(request.form))
        question.save(upsert=True)
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST


@app.route('/api/question/delete/<_id>', methods=['GET'])
def delete_question(_id):
    '''
    Delete a question
    '''
    try:
        question = Question(_id=_id)
        question.delete()
        return status.HTTP_202_ACCEPTED
    except:
        return status.HTTP_400_BAD_REQUEST

if __name__ == '__main__':
    app.run(host='0.0.0.0')