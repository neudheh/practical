from flask import Flask, render_template

# convention
app = Flask(__name__)

@app.route("/hello")
def hello():
    return render_template("hello_world.html")

@app.route("/<year>")
def year(year):
    return render_template("year.html", year=year)

@app.route("/")
def index():
    return render_template("index.html")

# runs app
if __name__ == "__main__":
    app.run()