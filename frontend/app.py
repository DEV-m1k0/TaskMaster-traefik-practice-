from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth/login')
def login():
    return render_template('login.html')

@app.route('/auth/register')
def register():
    return render_template('registration.html')


if __name__ == '__main__':
    app.run(debug=True)