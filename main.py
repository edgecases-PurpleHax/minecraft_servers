from flask import Flask, render_template, send_file
import logging
from logging.handlers import TimedRotatingFileHandler
app = Flask("app")


@app.route("/")
def index():
    return render_template("index.html")
@app.route("/roadedgesaves", methods=["GET"])
def download():
    return send_file("/home/edgecase/.config/Epic/FactoryGame/Saved/SaveGames/server/testingRockyDesert_autosave_0.sav", as_attachment=True)


if __name__ == "__main__":
    logger = logging.getLogger('werkzeug')
    handler = TimedRotatingFileHandler('access.log', when="midnight", interval=1, backupCount=1)
    handler.suffix = "%Y%m%d"
    logger.addHandler(handler)
    app.run(host="0.0.0.0", debug=False, port=8080)
