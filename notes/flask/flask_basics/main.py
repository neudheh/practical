from flask import Flask, render_template

# convention
app = Flask(__name__)

# if the user goes to https://example.com/
@app.route("/")
def index():
    name = "Kevin"
    return render_template("index.html", name=name)

# runs app
if __name__ == "__main__":
    app.run()