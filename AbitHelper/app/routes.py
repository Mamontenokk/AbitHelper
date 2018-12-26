from datetime import datetime
from flask import render_template, flash, redirect, request, url_for
from werkzeug.urls import url_parse
from app import app, db
from app.forms import SpecialityForm
import json
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')


@app.route('/get_specialities/', methods=['GET','POST'])
@app.route('/get_specialities/<choice>', methods=['GET','POST'])
def get_specialities(choice=24):

    data = []
    path = os.getcwd()
    with open(os.path.join(path,'app','static','data','specialities.txt'), 'r') as f:
        data = f.read().splitlines()
    form = SpecialityForm()
    form.specialities.choices = data

    if request.method == 'POST':
        option = request.form.get('spec_select')
        mark = form.mark.data
        with open('D:\\text.txt', 'w') as f:
            try:
                f.write(mark)
            except:
                pass
        # data = {}
        # with open('D:\\average.json', 'r', encode='utf-8') as f:
        #     data= json.load(f)
        # print(data)
        return redirect(url_for('get_specialities', choice = option))
    return render_template('specialities.html', title='Specialities', form=form, selection=choice)


