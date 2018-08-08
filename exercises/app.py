from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
    if request.method == 'GET':
        return render_template('add.html')
    else:
        return 'Received POST request!', render_template('add.html')

    

app.run(debug=True)
