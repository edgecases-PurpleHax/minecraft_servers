from flask import Flask, render_template

app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=80)
