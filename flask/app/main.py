#from flask import Flask
from app import app 

#application = Flask(__name__)

@app.route('/')
def homepage():
    return "Hello World Everyone!!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000)
