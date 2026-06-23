from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("gift.html")


@app.route("/gift")
def gift():
    return render_template("myself.html")


@app.route("/year1")
def year1():
    return render_template("year1.html")


@app.route("/year2")
def year2():
    return render_template("year2.html")


@app.route("/year3")
def year3():
    return render_template("year3.html")


@app.route("/year4")
def year4():
    return render_template("year4.html")

@app.route("/story")
def story():
    return render_template("story.html")


if __name__ == "__main__":
    app.run(debug=True)