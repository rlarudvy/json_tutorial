
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template,request, Response
from collections import Counter
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    user_string = ('안녕하세요 안녕하세요 안녕하세요 안녕하세요 안녕하세요 안녕하세요'
                   '반갑습니다 ')
    counter = dict(Counter(user_string))
    result = json.dumps(counter)
    return result

@app.get("/count/")
def count():
    return render_template('count.html')

@app.post("/result/")
def result():
    user_input = request.form['userinput']
    word_dict = dict(Counter(user_input.split()))
    result = json.dumps(word_dict)
    return Response(result,
                    mimetype='application/json',
                    headers={'Content_Disposition':'attachment; filename=count.json'})