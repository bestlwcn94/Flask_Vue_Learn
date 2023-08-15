from flask import Flask
import os
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


@app.route('/',methods=['GET','POST'])
def hello_world1():  # put application's code here
    return 'Hello World1111111!'

if __name__ == '__main__':
    app.run()
