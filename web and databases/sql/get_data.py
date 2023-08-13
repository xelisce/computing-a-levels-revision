import sqlite3
from flask import render_template, Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("start.html")

@app.route("/results", methods=["POST"])
def results():
    location = request.form["location"]
    db = sqlite3.connect("inventory_database.db")
    cursor = db.execute('SELECT Name, Type, Price FROM Product WHERE Location = ? ORDER BY Price ASC', (location,))
    data = [x for x in cursor]
    print(data)
    db.close()
    return render_template("results.html", location=location, data=data)

if __name__ == "__main__":
    app.run(debug=True)