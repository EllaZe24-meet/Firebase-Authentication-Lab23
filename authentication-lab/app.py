from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

const firebaseConfig = {
  "apiKey": "AIzaSyC8EgAa3Z_GxBQk-2scxGsW_xvxpMoER5I",
  "authDomain": "example-628cb.firebaseapp.com",
  "projectId": "example-628cb",
  "storageBucket": "example-628cb.appspot.com",
  "messagingSenderId": "503931398850",
  "appId": "1:503931398850:web:1849895879eaad0a9aa95b",
  "measurementId": "G-TNSNY8XXLQ",
  "databaseURL": "https://example-628cb-default-rtdb.firebaseio.com/"
};



@app.route('/', methods=['GET', 'POST'])
def signin():
    return render_template("signin.html")
    if request.method == 'POST':
       email = request.form['email']
       password = request.form['password']
       try:
       		login_session['user'] = 
auth.sign_in_with_email_and_password(email, password)
   return render_template("add_tweet .html")
       except:
           error = "Authentication failed"
           return	render_template("signin.html")

firebase = pyrebase	.initialize_app(const firebaseConfig)
auth = firebase	.auth()
db = firebase.database

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	if request.method == 'POST':
		password = request.form['password']
		email = request.form['email']
    return render_template("signup.html")
    	try:
    		login_session['user'] = auth.sign_up_with_email_and_password(email,password)
    		   return render_template("add_tweet .html")
    	except:
    		eror = "Authentication failed"
    		return	render_template("signup.html")
    	
@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")


if __name__ == '__main__':
    app.run(debug=True)