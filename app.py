from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


"""
if __name__ == __main__ indicates that we can launch this script filly if we launch it straitforward.
If we don't have  if __name__ == __main__ then while importing the file to another file we will
launch the whole code automatically but it's not a proper way. So we should use this expression to be able of
taking just needed parts of the code while importing it.
"""
if __name__ == '__main__':
    app.run()
