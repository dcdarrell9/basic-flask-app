import time

from flask import g, render_template
from flask_api import FlaskAPI
from flask_cors import CORS
from structlog import get_logger

logger = get_logger()

app = FlaskAPI(__name__)
app.strict_slashes = False
CORS(app)


@app.before_request
def before_request():
    g.request_start_time = time.time()


@app.after_request
def after_request(response):
    if g.get('request_start_time') and g.get('response_time'):
        response_time = time.time() - g.request_start_time
        logger.info("Request Complete",
                    response_time=response_time,
                    processing_time=response_time - g.response_time)
    return response


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


import basic_flask_app.views  # NOQA
