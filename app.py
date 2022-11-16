from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    data1 = [
        ("01-01-2020", 10),
        ("02-01-2020", 15),
        ("03-01-2020", 5),
        ("04-01-2020", 8),
        ("05-01-2020", 23),
        ("06-01-2020", 19),
        ("07-01-2020", 35),
    ]
    
    data2 = [
        ("08-01-2020", 3),
        ("09-01-2020", 2),
        ("10-01-2020", 5),
        ("11-01-2020", 8),
        ("12-01-2020", 17),
        ("13-01-2020", 22),
        ("14-01-2020", 38),
    ]
    
    data3 = [
        ("15-01-2020", 18),
        ("16-01-2020", 15),
        ("17-01-2020", 6),
        ("18-01-2020", 14),
        ("19-01-2020", 9),
        ("20-01-2020", 12),
        ("21-01-2020", 25),
    ]
    
    labels1 = [row[0] for row in data1]
    values1 = [row[1] for row in data1]
    
    labels2 = [row[0] for row in data2]
    values2 = [row[1] for row in data2]
    
    labels3 = [row[0] for row in data3]
    values3 = [row[1] for row in data3]
    
    return render_template("graph.html", labels1 = labels1, values1 = values1, labels2 = labels2, values2 = values2, labels3 = labels3, values3 = values3)

@app.route("/temp")
def a():
    data = [
        ("01-01-2020", 10),
        ("02-01-2020", 15),
        ("03-01-2020", 5),
        ("04-01-2020", 8),
        ("05-01-2020", 23),
        ("06-01-2020", 19),
        ("07-01-2020", 35),
    ]
    
    labels = [row[0] for row in data]
    values = [row[1] for row in data]
    return render_template("graphTemp.html", labels = labels, values = values)

if __name__ == '__main__':
    app.run(debug=True)