from flask import render_template, Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from structlog import get_logger

from config import Config

logger = get_logger()

app = Flask(__name__)
app.config.from_object(Config)
app.strict_slashes = False
CORS(app)
csrf = CSRFProtect(app)


@app.route('/', methods=['GET'])
def root():
    return render_template('index.html')


import basic_flask_app.views  # NOQA
