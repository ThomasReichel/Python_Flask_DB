from flask import Flask

app = Flask(__name__)

@app.route('/')
def login():
    return 'Login'

@app.route('/index')
def index():
    return 'Index'

@app.route('/add')
def add_ds():
    return 'New'

@app.route('/change')
def change_ds():
    return 'Ändern'

@app.route('/view_on')
def view_on():
    return 'Zeige einen'

@app.route('/view_all')
def view_all():
    return 'Zeige alle'

@app.route('/delete')
def del_ds():
    return 'Lösche DS'


if __name__ == '__main__':
    app.run(debug=True)
