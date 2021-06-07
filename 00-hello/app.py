from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the user's name from the request args
    name = request.args.get('myName')
    
    # If they didn't enter a name, use "world"
    if name is None or name == '':
        name = 'World'

    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
