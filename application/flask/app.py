from flask import Flask

from domain.services.math.c_math import CMath
from domain.services.math.py_math import PyMath

app = Flask(__name__)

pymath = PyMath()
cmath = CMath()


@app.route('/')
def index():
    return 'Hello!'


@app.route('/fibonacci/<int:n>')
def fibonacci(n: int):
    return {'result': pymath.fibonacci(n)}


@app.route('/fibonacci2/<int:n>')
def fibonacci2(n: int):
    return {'result': cmath.fibonacci(n)}
