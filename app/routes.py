"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import sqlite3
from app import app, db
from flask import  request, jsonify, json
#from app.forms import UserForm
from app.models import User, Employer,Licenses
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
from flask_table import Table, Col


@app.route('/check-pin/<employerCode>', methods=['POST'])

def check(employerCode):


    peter = User.query.all()

    class ItemTable(Table):
        campo = Col('Campo')
        tipo= Col('Tipo')

        name='kaa'
        items = [dict(campo= Employer.query.member_name, tipo= type(Employer.query.member_name)),
        dict(campo = Employer.query.member_code, tipo= type(Employer.query.member_code)),
        dict(campo = Employer.query.member_count, tipo= type (Employer.query.member_count)),
        dict(campo = Employer.query.thumbnail, tipo= type (Employer.query.thumbnail)),
        dict(campo = Employer.query.register_date, tipo= type (Employer.query.register_date))]

    print (type(peter))

    
    return jsonify(items,peter.serialize), 200

@app.route('/medical-license', methods=['POST'])
def submitMedicalLicense():



    '''
    rot= { 0 :{
            
        "initial_date": "01/10/2019",
        "final_date": "03/10/2019",
        "time": 65,
        "member_code": 1
        }
        }
    return  jsonify (request.get_json())'''

@app.route ('/medical-licenses', methods= ['GET'])
def attestation():
    '''
    if 'Licenses' in request.args:
        Licenses= int(request,args['Licenses']) 
    else:
        return "Error: No id field provided"

    results = []'''
    #c= connection.cursor()
    attest= Licenses.query.order_by().all()
    if (not 'id'):
        return jsonify ({}),404

    
    return jsonify (attest),200
    
    





@app.route('/employer/<employerCode>', methods=['GET'])
def api_employer(employerCode):
    peter= Employer.query.filter_by(employer_code= '<employerCode>').all()
    
    print(type(employerCode))
    if (not employerCode):
        return jsonify ({}),404

    
    return jsonify (employerCode),200
   