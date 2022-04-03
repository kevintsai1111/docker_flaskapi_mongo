import json
import pymongo 
from pymongo import MongoClient
from flask import Flask,request,jsonify



app = Flask(__name__)

@app.route('/')

def hello_word():
    return '666'  


@app.route('/log',methods=["POST"])

def log():
    data = request.get_json()
    name = data["name"]
    gender = data["gender"]
    collections_name = "test2"
    client = pymongo.MongoClient("mongodb+srv://kevin:FidQm1vLwEa4iZOe@cluster0.srhl7.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
    db = client.test
    mycol = db[collections_name]
    mycol.insert_one(data)
    return jsonify({'result':'success','name':name,'gender':gender})




if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')