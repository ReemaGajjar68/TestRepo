from flask import Flask, render_template, url_for, redirect, request
from werkzeg.security import generate_password_hash, check_password_hash

app =  Flask(__name__)

users={}

@app.route('/', methods=['GET','POST'])

def registration():
    if request.method='POST':
        username= request.form['username']
        email= request.form['email']
        password= request.form['password']

        hashed_password= generate_password_hash(password)

        users[username]={
            'email' : email,
            'password' : hashed_password
        }

        return redirect (url_for('home'))
        
    retrun render_template('registration.html')

@app.route('/home')
def home():
    return 'Welcome to the Home Page'

    
if __name__ = '__main__':
    app.run(debug=True)
