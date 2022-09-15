from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models import model_dojo


@app.route('/')
def index():

    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    if not model_dojo.Dojo.validate(request.form):
        return redirect('/')

    data = {
        **request.form
    }
    model_dojo.Dojo.create(data)
    return redirect('/result')

@app.route('/result')
def result():

    dojo = model_dojo.Dojo.result()
    return render_template('show.html', dojo=dojo)