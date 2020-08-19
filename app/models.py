from app import db
import sqlite3
from flask_table import Table, Col

'''
connection = sqlite3.connect('teste.db')
c= connection.cursor()


def   DROP TABLE IF EXISTS users():

  c.execute('CREATE TABLE dados (id integer, unix real, \
                  datestamp text, value real) ')

create_table()
'''

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True)



    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
           'id'  : self.id,
           'name': self.name,
           # This is an example how to deal with Many2Many relations
           'email' : self.email
       }


class Employer(db.Model):
   
  __tablename__ = 'employer'
  id = db.Column(db.Integer, primary_key=True)
  employer_name = db.Column(db.String(100))
  employer_code = db.Column(db.String(120))
  member_count = db.Column(db.String(3))
  thumbnail = db.Column(db.String(255))
  register_date = db.Column(db.Numeric(10))


  def __init__(self, employer_name=None, employer_code=None, member_count=None, thumbnail=None, register_date=None):
      self.employer_name = employer_name
      self.employer_code = employer_code
      self.member_count = member_count
      self.thumbnail = thumbnail
      self.register_date = register_date


  def __repr__(self):
      return '<User %r>' % self.name
      

  @property
  def serialize(self):

    return {
       'id'  : self.id,
       'employer_name': self.employer_name,
       # This is an example how to deal with Many2Many relations
       'employer_code' : self.employer_code,
       'member_count' : self.member_count,
       'thumbnail' : self.thumbnail,
       'register_date' : self.register_date,
       }       



class Licenses(db.Model):
    __tablename__ = 'licenses'
    id = db.Column(db.Integer, primary_key=True)
    initial_date = db.Column(db.Numeric(10))
    final_date = db.Column(db.Numeric(10))
    time = db.Column(db.Numeric(5))

    def __init__ (self, initial_date=None, final_date=None, time=None):
      self.initial_date= initial_date
      self.final_date= final_date
      self.time= time


    def __repr__(self):
        return '<User %r>' % self.name

    @property
    def serialize(self):
       
       return {
           'id'  : self.id,
           'initial_date': self.initial_date,
           'final_date' : self.final_date,
           'time' : self.time,
           
       }           
