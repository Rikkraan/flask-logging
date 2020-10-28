from flask import Flask, Response, render_template
from time import sleep
from loguru import logger
import datetime

logger.add("app/static/job.log", format="{time} - {message}")

APP = Flask(__name__, static_folder="app/static/", template_folder="app/static/")
@APP.route("/", methods=["GET"])
def root():
    """index page"""
    return render_template("index.html")


def flask_logger():
    """creates logging information"""
    for i in range(100):
        current_time = datetime.datetime.now().strftime('%H:%M:%S') + "\n"
        yield current_time.encode()
        sleep(1)



@APP.route("/log_stream", methods=["GET"])
def log_stream():
    """returns logging information"""
    return Response(flask_logger(), mimetype="text/plain", content_type="text/event-stream")


if __name__ == "__main__":
    APP.run(host="0.0.0.0", port=5000, threaded=True)