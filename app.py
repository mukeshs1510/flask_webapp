from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def myfunc():
    return render_template('index.html')
    # return "Hello World!"


@app.route('/newpage')
def page():
    return "Hello pages!"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
