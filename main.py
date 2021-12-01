from flask import Flask, render_template, send_file
import logging
app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/roadedgesaves", methods=["GET"])
def download():
    return send_file("/home/edgecase/.config/Epic/FactoryGame/Saved/SaveGames/server/testing_autosave_0.sav", as_attachment=True)


if __name__ == "__main__":
    logging.basicConfig(filename='server.log', level=logging.INFO, format='%(asctime)s: %(message)s')
    app.run(debug=True, port=80)
