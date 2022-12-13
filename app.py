from flask import Flask
import main as m
app = Flask(__name__)

@app.route('/')
def hello_world():
    m.connection()
    return 'Hello, World!'
