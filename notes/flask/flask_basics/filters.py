from flask import Flask, render_template, request

# convention
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"]) # Tells the URL to take both get and post requeusts
def index():
    # if it is a get request, return a form for them to put in their name
    if request.method == "GET":
        return render_template("form.html")
    # if it is a post request (which can only be sent by the form), get the name entered 
    # and return the rendered webpage
    name = request.form.get("name")
    return render_template("filters.html", name=name)

# runs app
if __name__ == "__main__":
    app.run()