from flask import Flask, render_template, request, make_response, jsonify, redirect, url_for
import subprocess
import streamlit as st
import mysql.connector
from mysql.connector import Error
import json

app = Flask(__name__)

#index

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# register
@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/regdata', methods =  ['GET','POST'])
def regdata():
    #Data gathering
    name = request.args['name'] 
    username = request.args['username'] 
    email = request.args['email']
    gender = request.args['gender']
    pswd = request.args['pswd']
    cfpswd = request.args['cfpswd']

    #Data transmission to db
    connection = mysql.connector.connect(host ='localhost', database ='userdb', user ='root', password='')
    sqlquery="insert into userdata(username,name,email,gender,pswd,cfpswd) values('"+username+"','"+name+"','"+email+"','"+gender+"','"+pswd+"','"+cfpswd+"')"
    print(sqlquery)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    connection.commit() 
    connection.close()
    cursor.close()
    msg="Data Saved Successfully"
    #return render_template('register.html')
    resp = make_response(json.dumps(msg))
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp

# login
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logdata', methods =  ['GET','POST'])
def logdata():
    #Data gathering
    username = request.args['username']
    pswd = request.args['pswd']
    #Data transmission to db
    connection = mysql.connector.connect(host ='localhost', database ='userdb', user ='root', password='')
    sqlquery="select count(*) from userdata where username='"+username+"' and pswd='"+pswd+"'"
    print(sqlquery)
    cursor = connection.cursor()
    cursor.execute(sqlquery)
    data = cursor.fetchall()
    print(data)
    connection.close()
    cursor.close()
    msg=""
    if data[0][0]==0:
        msg="Failure"
    else:
        msg="Success"
        # Run the Streamlit app using subprocess
        subprocess.run(['streamlit', 'run', 'streamlit_app.py'])
        return redirect(url_for('streamlit_app'))  # Redirect to the Streamlit app route upon successful login
    
    resp = make_response(json.dumps(msg))
    print(msg, flush=True)
    #return render_template('register.html',data=msg)
    return resp
 

if __name__=="__main__":
    app.run(debug=True)