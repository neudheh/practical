from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    classlist = [
        [2, "Ashton Too", 20],
        [7, "Kevin Chua", 18]
    ]
    return render_template("index.html", classlist=classlist)

if __name__ == "__main__":
    app.run()