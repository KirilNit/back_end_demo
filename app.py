from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import CreateTable
# from sqlalchemy import Table, Column, String, MetaData, Integer, DateTime, create_engine
from sqlalchemy import *
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@127.0.0.1:5433/postgres"
db = SQLAlchemy(app)

class Notes(db.Model):
    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(64), nullable=False)
    note = Column(db.String(1024), nullable=False)

    def __init__(self, name, note):
        self.name = name
        self.note = note

db.create_all()

@app.route('/postnotes', methods=["GET", "POST"])
def hello_world():
    some_json = request.get_json()
    if (request.method == "POST"):
        some_json = request.get_json()
        db.session.add(Notes(some_json['name'], some_json['note']))
        return jsonify({'you sent': some_json}), 201
    elif (request.method == 'GET'):
        return jsonify(Notes.query.all())

@app.route('/default', methods=["GET", "POST"])
def default():
    return jsonify({'default_resp':'New String For Default response'})


if __name__ == '__main__':
    app.run()
