from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html', name='World')

@app.route('/', methods=['POST'])
def hello_user():
    name = request.form.get('myName')
    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
