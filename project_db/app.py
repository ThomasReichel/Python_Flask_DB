from flask import Flask, render_template, request
import sqlite3


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
        bezeichnung = request.form['name1']
        notiz = request.form['name2']
        anzahl = request.form['name3']

        verbindung = sqlite3.connect("database.db")
        cursor = verbindung.cursor()

        cursor.execute("""
                        INSERT INTO artikel 
                               VALUES (?,?,?)
                       """,
                       (bezeichnung, notiz, anzahl)
                       )

        verbindung.commit()
        verbindung.close()
        return render_template("anzeigen.html")


@app.route('/auslesen', methods=['GET', 'POST'])
def auslesen():
    verbindung = sqlite3.connect("database.db")
    zeiger = verbindung.cursor()
    zeiger.execute("SELECT bezeichnung, notiz, anzahl FROM artikel")
    inhalt = zeiger.fetchall()
    verbindung.close()
    return render_template("auslesen.html", bezeichnung=inhalt[0][0], notiz=inhalt[0][1], anzahl=inhalt[0][2])

if __name__ == '__main__':
    app.run()
