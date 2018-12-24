from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/nomes')
def lista_nomes():
    return 'Gustavo, Rachel, Júlia, Eduardo'


if __name__ == '__main__':
    app.run()
