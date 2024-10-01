from flask import Flask, render_template, request, send_from_directory
from werkzeug.utils import secure_filename
import os

# makes flask app
app = Flask(__name__)
imagelist = []

# main webpage
@app.route("/", methods = ["GET", "POST"])
def index():
    # GET
    if request.method == "GET":
        return render_template("index.html", images=imagelist)

    # POST
    # gets the image and filename
    image = request.files.get("image")
    filename = secure_filename(image.filename)

    # saves image   
    image.save(os.path.join("uploads", filename))

    # adds image to imagelist
    imagelist.append(filename)

    # renders template
    return render_template("index.html", images=imagelist)


# gets image
@app.route('/uploads/<filename>')
def uploads(filename):
    if filename in imagelist:
        return send_from_directory("uploads", filename)

# runs web app
if __name__ == "__main__":
    app.run()
