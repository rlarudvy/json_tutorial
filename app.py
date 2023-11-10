
# A very simple Flask Hello World app for you to get started with...

from flask import Flask
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



