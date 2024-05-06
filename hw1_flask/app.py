from flask import Flask

app = Flask(__name__)


@app.route('/') # Ошибка заключалась в отсутсвии слеша в параметре декоратора
def home():
    return 'Hello Flask!'


@app.route('/user/<string:name>')
def user(name: str):
    return f'Hello {name.title()}!'


if __name__ == '__main__':
    app.run()
