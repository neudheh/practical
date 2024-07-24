from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    score = int(request.form.get("score"))
    return render_template("index.html", score=score)

if __name__ == "__main__":
    app.run()