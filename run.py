import os

from basic_flask_app import app
from structlog import get_logger

from config import Config

logger = get_logger()

if __name__ == '__main__':
    if not os.getenv('APP_SETTINGS'):
        os.environ['APP_SETTINGS'] = 'DevelopmentConfig'
    logger.info("Starting listening on port {}".format(Config.PORT))
    app.run(debug=Config.DEBUG, host='0.0.0.0', port=int(Config.PORT))
