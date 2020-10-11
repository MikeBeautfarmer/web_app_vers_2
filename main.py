from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")  # Done
def welcome():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")


@app.route("/fakebook")  # Done
def fakebook():
    return render_template("fakebook.html")


@app.route("/fakegoogle")  # Done
def fakegoogle():
    return render_template("fakegoogle.html")


@app.route("/hairdresser")  # Done
def hairdresser():
    return render_template("hairdresser.html")


if __name__ == "__main__":
    app.run(debug=True)
