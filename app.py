from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("projects.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/projects/prime-supermarket")
def prime_supermarket():
    return render_template("prime-supermarket.html")

@app.route("/projects/budgeting")
def budgeting():
    return render_template("budgeting.html")

@app.route("/projects/earthecho")
def earthecho():
    return render_template("earthecho.html")

@app.route("/projects/lockbox")
def lockbox():
    return render_template("lockbox.html")

if __name__ == "__main__":
    app.run(debug=True)
