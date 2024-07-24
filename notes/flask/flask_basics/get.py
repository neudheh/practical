from flask import Flask, render_template, request

# convention
app = Flask(__name__)

@app.route("/")
def index():
    # gets the name from the url
    # e.g. https://example.com/?name=Kevin, the name would be Kevin
    name = request.args.get("name", "World")
    return render_template("index.html", name=name)

# runs app
if __name__ == "__main__":
    app.run()