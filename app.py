from flask import Flask,request, url_for, redirect, render_template
import pandas as pd
import numpy as np
import pickle
import sqlite3
import cv2
import os

UPLOAD_FOLDER = 'static/uploads/'

model = pickle.load(open('model.pkl', 'rb'))


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/login')
def login():
	return render_template('signin.html')

@app.route('/logon')
def logon():
	return render_template('signup.html')

@app.route("/signup")
def signup():
    
    
    user = request.args.get('user','')
    name = request.args.get('name','')
    password = request.args.get('password','')

    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("insert into `info` (`user`,`name`, `password`) VALUES (?, ?, ?)",(user,name,password))
    con.commit()
    con.close()

    return render_template("signin.html")

@app.route("/signin")
def signin():

    mail1 = request.args.get('user','')
    password1 = request.args.get('password','')
    con = sqlite3.connect('signup.db')
    cur = con.cursor()
    cur.execute("select `name`, `password` from info where `name` = ? AND `password` = ?",(mail1,password1,))
    data = cur.fetchone()

    if data == None:
        return render_template("signin.html")    

    elif mail1 == 'admin' and password1 == 'admin':
        return render_template("index.html")

    elif mail1 == str(data[0]) and password1 == str(data[1]):
        return render_template("index.html")
    else:
        return render_template("signin.html")

@app.route('/index')
def index():
   return render_template('index.html')



@app.route('/notebook')
def notebook():
	return render_template('notebook.html')


@app.route('/predict',methods=['GET','POST'])
def predict():
    print("Entered")
    
    print("Entered here")
    file = request.files['files'] # fet input
    filename = file.filename        
    print("@@ Input posted = ", filename)
        
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(file_path)

    image = cv2.imread(file_path)

    image_array = cv2.resize(image , (64,64))

    img = image_array.reshape([-1, np.product((64,64,3))])

    ans = model.predict(img)

    if ans == 0:
        return render_template('result.html',prediction=f'Forgery signature detected.')
    else:
        return render_template('result.html',prediction=f'Genuine signature detected')

    
        




if __name__ == '__main__':
   app.run()