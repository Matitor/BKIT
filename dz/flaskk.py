from flask import Flask
from gen import lazy_gen
app = Flask(__name__)

@app.route('/')
def hello():
  return 'hello, world!'
@app.route('/<int:i>')
def gen(i):
  return list(i for i in lazy_gen(i))
if __name__ == '__main__':
    app.run()