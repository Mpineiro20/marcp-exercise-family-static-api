"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# create dictionaires to add to jackson family list (array)
# python a list of dictionaries is = in js an array of objects
# create 3 dictionaries of family members in the instructions and add them to jackson family. 

jackson_family.add_member({
    'id':jackson_family._generateId(),
    'first-name': 'John',
    'last-name':'Jackson' ,
    'age':33 ,
    'lucky_numbers':[7,13,22]

})
jackson_family.add_member({
    'id':jackson_family._generateId(),
    'first-name': 'Jane',
    'last-name':'Jackson' ,
    'age':35 ,
    'lucky_numbers':[10,14,3]

})
jackson_family.add_member({
    'id':jackson_family._generateId(),
    'first-name': 'Jimmy',
    'last-name':'Jackson' ,
    'age':5 ,
    'lucky_numbers':[1]

})


# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)





@app.route('/members', methods=['GET'])
def get_all_family_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
   return jsonify(members), 200

@app.route ('/member/<int:member_id>',methods= ['GET]')
def get_single_family_member(member_id):
    member = jackson_family.get_member(member id)
        return jsonify(),200

@app.route('/member', methods=['POST'])
def handle_add_member():
    data = request.json
    jackson_family.add_member(data)
    return jsonify(data), 200