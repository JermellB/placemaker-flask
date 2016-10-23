__author__ = 'jermellbeane'
from flask_api import FlaskAPI, status
from flask import Flask
app = Flask(__name__)
from flask import request, make_response
from  models import Coc, Organization, Person, User, Form, Question, Log
import pytz
import json
import datetime
import mongoengine
from settings import MONGO_HOST, MONGO_DB
mongoengine.connect(MONGO_DB, host=MONGO_HOST)
from messaging import TwilioNotificationsMiddleware
'''
class Coc(mongoengine.DynamicDocument):
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

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
  return response

@app.route('/')
def api_root():
    return 'HELLO'

#CocS
@app.route('/api/coc/create', methods=['POST'])
def create_coc():
    '''
    Create a Continuum of Care
    '''
    try:
        coc = Coc(date_created=pytz.utc.localize(datetime.datetime.now()),**request.form)
        coc.save(upsert=True)
        return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
    except Exception as e:
        return str(e), status.HTTP_400_BAD_REQUEST

@app.route('/api/coc/read/<_id>', methods=['GET'])
def read_coc(_id):
    '''
    Get a Coc
    '''
    try:
        coc = Coc.objects.get(pk=_id)
        print coc
        return coc.to_json()
    except Exception as e:
        return str(e) #str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/coc/all', methods=['GET'])
def read_coc_all():
    '''
    Get a Coc
    '''
    try:
        cocs = Coc.objects
        # print cocs
        return cocs.to_json()
    except Exception as e:
        print str(e)
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/coc/update/', methods=['POST'])
def update_coc():
    '''
    Update a Coc
    '''
    try:
        coc = Coc.objects.get(pk=request.form['_id'])
        coc2 = Coc(_id=coc._id,**request.form)
        coc2.save(upsert=True)
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/coc/delete/<_id>', methods=['GET'])
def delete_coc(_id):
    '''
    Delete a Coc
    '''
    try:
        coc = Coc.objects.get(pk=_id)
        coc.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)


#ORGANIZATIONS
@app.route('/api/organization/create', methods=['POST'])
def create_organization():
    '''
    Create an Organization
    '''
    if request.form:
        try:
            organization = Organization(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
            organization.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except Exception as e:
            return str(e), status.HTTP_400_BAD_REQUEST

    elif request.json:
        try:
            organization = Organization(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.json))
            organization.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except Exception as e:
            return str(e), status.HTTP_400_BAD_REQUEST

    else:
        return 'Please use JSON or a FORM'



@app.route('/api/organization/read/<_id>', methods=['GET'])
def read_organization(_id):
    '''
    Get a organization
    '''
    try:
        organization = Organization.objects.get(pk=_id)
        return organization.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/organization/all', methods=['GET'])
def read_all_orgs():
    '''
    get a list of orgs
    '''

    try:
        orgs = Organization.objects
        return orgs.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/organization/update', methods=['POST'])
def update_organization():
    '''
    Update a organization
    '''
    if request.form:
        try:
            organization = Organization(**request.form)
            organization.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            organization = Organization(**json.loads(request.json))
            organization.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return 'Please use JSON or a FORM'


@app.route('/api/organization/delete/<_id>', methods=['GET'])
def delete_organization(_id):
    '''
    Delete a organization
    '''
    try:
        organization = Organization.objects.get(pk=_id)
        organization.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

# PERSON
@app.route('/api/person/create', methods=['POST'])
def create_person():
    '''
    Create a Person
    '''
    if request.form:
        try:
            person = Person(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
            person.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            person = Person(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.json))
            person.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return 'Please use JSON or a FORM'


@app.route('/api/person/read/<_id>', methods=['GET'])
def read_person(_id):
    '''
    Get a person
    '''
    try:
        person = Person.objects.get(pk=_id)
        return person.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/person/all', methods=['GET'])
def read_all_people():
    '''
    get a list of all people
    '''

    try:
        people = Person.objects
        return people.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/person/update', methods=['POST'])
def update_person(_id):
    '''
    Update a person
    '''
    if request.form:
        try:
            person = Person(**request.form)
            person.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            person = Person(**json.loads(request.json))
            person.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)
    else:
        return 'Please use JSON or a FORM'

@app.route('/api/person/delete/<_id>', methods=['GET'])
def delete_person(_id):
    '''
    Delete a person
    '''
    try:
        person = Person.objects.get(pk=_id)
        person.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

# USER
@app.route('/api/user/create', methods=['POST'])
def create_user():
    '''
    Create a User
    '''
    if request.form:
        try:
            user = User(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
            user.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            user = User(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.json))
            user.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return 'Please use JSON or a FORM'


@app.route('/api/user/read/<_id>', methods=['GET'])
def read_user(_id):
    '''
    Get a user
    '''
    try:
        user = User.objects.get(pk=_id)
        return user.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/user/all', methods=['GET'])
def read_all_users():
    '''
    get a list of users
    '''

    try:
        user = User.objects
        return user.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/user/update', methods=['POST'])
def update_user():
    '''
    Update a user
    '''
    if request.form:
        try:
            user = User(**request.form)
            user.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            user = User(**json.loads(request.json))
            user.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return "Please use JSON or a FORM"



@app.route('/api/user/delete/<_id>', methods=['GET'])
def delete_user(_id):
    '''
    Delete a user
    '''
    try:
        user = User(_id=_id)
        user.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

#FORM
@app.route('/api/form/create', methods=['POST'])
def create_form():
    '''
    Create a Form
    '''
    if request.form:
        try:
            form = Form(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
            form.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            form = Form(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.json))
            form.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return "Please use JSON or a FORM"

@app.route('/api/form/read/<_id>', methods=['GET'])
def read_form(_id):
    '''
    Get a form
    '''
    try:
        form = Form.objects.get(pk=_id)
        return form.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/form/all', methods=['GET'])
def read_all_forms():
    '''
    get a list of forms
    '''

    try:
        forms = Form.objects
        return forms.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/form/update', methods=['POST'])
def update_form():
    '''
    Update a form
    '''
    if request.form:
        try:
            form = Form(**request.form)
            form.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            form = Form(**json.loads(request.form))
            form.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return "Please use JSON or a FORM"

@app.route('/api/form/delete/<_id>', methods=['GET'])
def delete_form(_id):
    '''
    Delete a form
    '''
    try:
        form = Form.objects.get(pk=_id)
        form.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

#Question
@app.route('/api/question/create', methods=['POST'])
def create_question():
    '''
    Create a Question
    '''
    if request.form:
        try:
            question = Question(date_created=pytz.utc.localize(datetime.datetime.now()), **request.form)
            question.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            question = Question(date_created=pytz.utc.localize(datetime.datetime.now()), **json.loads(request.json))
            question.save(upsert=True)
            return str(status.HTTP_201_CREATED), status.is_success(status.HTTP_201_CREATED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return "Please use JSON or a FORM"

@app.route('/api/question/read/<_id>', methods=['GET'])
def read_question(_id):
    '''
    Get a question
    '''
    try:
        question = Question.objects.get(pk=_id)
        return question.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/question/all', methods=['GET'])
def read_all_questions():
    '''
    get a list of questions
    '''

    try:
        questions = Question.objects
        return questions.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)


@app.route('/api/question/update', methods=['POST'])
def update_question(_id):
    '''
    Update a question
    '''
    if request.form:
        try:
            question = Question(**request.form)
            question.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            question = Question(**json.loads(request.json))
            question.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return "Please use JSON or a FORM"


@app.route('/api/question/delete/<_id>', methods=['GET'])
def delete_question(_id):
    '''
    Delete a question
    '''
    try:
        question = Question.objects.get(pk=_id)
        question.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

#Logging
@app.route('/api/log/read/<_id>', methods=['GET'])
def read_log(_id):
    '''
    Get a log
    '''
    try:
        log = Log.objects.get(pk=_id)
        return log.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/log/all', methods=['GET'])
def read_all_logs():
    '''
    get a list of all logs
    '''

    try:
        logs = Log.objects
        return logs.to_json()
    except:
        return str(status.HTTP_400_BAD_REQUEST)


@app.route('/api/log/update', methods=['POST'])
def update_log(_id):
    '''
    Update a log
    '''
    if request.form:
        try:
            log = Log(**request.form)
            log.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    elif request.json:
        try:
            log = Log(**json.loads(request.json))
            log.save(upsert=True)
            return str(status.HTTP_202_ACCEPTED)
        except:
            return str(status.HTTP_400_BAD_REQUEST)

    else:
        return "Please use JSON or a FORM"

@app.route('/api/log/delete/<_id>', methods=['GET'])
def delete_log(_id):
    '''
    Delete a log
    '''
    try:
        log = Log.objects.get(pk=_id)
        log.delete()
        return str(status.HTTP_202_ACCEPTED)
    except:
        return str(status.HTTP_400_BAD_REQUEST)

@app.route('/api/message/<msg>/<name>/<number>', methods=['GET'])
def send_messages(msg, name, number):
    try:
        m = TwilioNotificationsMiddleware()

        # print("sending message to {}".format(key))
        m.client.send_message("hi {0} {1}".format(name, msg), number)

        return str(status.HTTP_202_ACCEPTED)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
    # app2 = app.test_client()
    # app2.post('/api/message', data={'jermell':'3142559197'})

    # question = Coc(rah_rah='1')
    # question.save()
