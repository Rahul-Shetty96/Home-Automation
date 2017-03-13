from flask import Flask, redirect, url_for, request
from flask import jsonify
app = Flask(__name__)



@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int);
    b = request.args.get('b', 0, type=int);
    print a,b
    return "k("+str(a)+")";

if __name__ == '__main__':
   app.run(debug = True)