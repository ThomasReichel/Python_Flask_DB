from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def formular():
    return render_template("form.html")


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        return render_template("index.html", text1=name1, text2=name2)


@app.route('/neu', methods=['GET', 'POST'])
def neu():
    return render_template("neu.html")


@app.route('/anzeigen', methods=['GET', 'POST'])
def anzeigen():
    if request.method == 'POST':
        name1 = request.form['name1']
        name2 = request.form['name2']
        name3 = request.form['name3']
        return render_template("anzeigen.html", text1=name1, text2=name2, text3=name3)


if __name__ == '__main__':
    app.run()
