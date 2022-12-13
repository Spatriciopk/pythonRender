from flask import Flask
import main as m
app = Flask(__name__)

@app.route('/')
def hello_world():
    print(m.connection()[0][1])
    data = m.connection()[0][1]
    return data