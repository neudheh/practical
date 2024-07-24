from flask import Flask, render_template

# convention
app = Flask(__name__)

# if the user goes to https://example.com/Kevin, the name will be Kevin
@app.route("/<name>")
def index(name):
    return render_template("index.html", name=name)

# runs app
if __name__ == "__main__":
    app.run()