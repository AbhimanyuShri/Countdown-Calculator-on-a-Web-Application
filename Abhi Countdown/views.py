from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from datetime import datetime

views = Blueprint(__name__,"views")

surveyresponse=[]

@views.route('/login')
def login():
    return render_template("login.html")

@views.route("/")
def welcome():
        return render_template("welcome.html")

@views.route("/homepage")
def homepage():
     return render_template("homepage.html")
    

@views.route("/json")
def get_json():
    return jsonify({'name': 'abhi','coolness':10})

@views.route("/data")
def get_data():
       data=request.json
       return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.homepage"))

@views.route('/survey')
def survey():
    return render_template('survey.html')
        


@views.route('/resubmit', methods=['POST']) 
def resubmit():
    date_submitted=request.form['date']
    email=request.form['email']
    date_obj = datetime.strptime(date_submitted, '%Y-%m-%d').date()
    today = datetime.today().date()
    countdown= (date_obj - today).days
    surveyresponse.clear()
    surveyresponse.append({
        'email': email,
        'date': date_submitted,
        'countdown': countdown
    })
    return redirect(url_for('views.result'))


@views.route('/result')
def result():
    print(surveyresponse)
    return render_template('result.html',result=surveyresponse)



@views.route('/resulthome',methods=['POST'])
def gotohomefromresult():
      return redirect(url_for('views.homepage'))
    

   

