# there are 2 serevr frame works
# 1/ Flask Framework (mirco framework)
# 2/ Django framework (very big framework)
# pip freeze > requirements.txt - gets all the required software libs in that virtual env
# copy this requirements.txt into the actual folder

from flask import Flask, render_template, url_for
from flask import request, redirect
import csv
# simple flask app makes its own html file
# render template helps us to make a templet html file
# Note flask always tries to look for template html in template folder
# Hence we need to create one template folder to used render template
app = Flask(__name__)

@app.route('/') #decorator # root address
def my_index():
    return render_template('index.html')
'''
@app.route('/index.html') #decorator # root address
def home():
    return render_template('index.html')

@app.route('/about.html') #decorator # root address
def about():
    return render_template('about.html')

@app.route('/works.html') #decorator # root address
def works():
    return render_template('works.html')

@app.route('/contact.html') #decorator # root address
def contact():
    return render_template('contact.html')
'''
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2,delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        return redirect('/thanks.html')
    else:
        print('Some Thing Went Wrong')
