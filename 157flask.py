from flask import Flask, g, render_template, Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'top'

@app.route('/hello')
@app.route('/hello/<username>')
def hello_world2(username=None):
    return f'hello world {username}'

def main():
    app.debug = True
    app.run(host='127.0.0.1')

if __name__ == '__main__':
    main()
