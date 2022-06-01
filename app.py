from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '119 메인창 프로젝트!'


if __name__ == '__main__':
    app.run()
