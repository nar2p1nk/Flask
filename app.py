from flask import Flask, render_template,request,url_for
from markupsafe import escape

application = Flask(__name__)

@application.route('/', methods=['GET','POST'])
def default():
    return render_template('ass.html')
    if request.method == 'POST':
        return '<h1>POST request complete</h1>'
    else:
        return 'client-side error'
    

@application.route('/<name>/<int:age>')
def profile(name,age):
    return f'hey {escape(name)}, you are {escape(age)} old'

@application.route("/POST?")
def post():
    return '<h1>POST request complete</h1>'

with application.test_request_context():
    url_for()