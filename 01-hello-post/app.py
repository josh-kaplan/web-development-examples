from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    # If the request was a POST (i.e. form submitted), get the user's name 
    if request.method == 'POST':
        name = request.form.get('myName')
    else:
        name = None
        
    # If they didn't enter a name, use "world"
    if name is None or name == '':
        name = 'World'

    return render_template('hello.html', name=name)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
