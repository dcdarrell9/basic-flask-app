import json

import requests
from flask import Blueprint
from requests.exceptions import HTTPError
from structlog import get_logger

from basic_flask_app import app

health_bp = Blueprint('health_bp', __name__, static_folder='static', template_folder='templates')

logger = get_logger()


def get_docker_health(docker_id):
    logger.debug('Retrieving docker health from sanic app')
    session = requests.Session()
    session.trust_env = False
    url = f'{app.config["SANIC_APP_URL"]}/health'
    url2 = f'http://{docker_id}:8000/health'
    response = session.get(url)
    response2 = session.get(url2)

    try:
        response.raise_for_status()
        response2.raise_for_status()
    except HTTPError:
        logger.exception(f'Docker health retrieval failed with error: {response.status_code}')
        raise Exception

    logger.debug('Successfully retrieved docker health')
    resp = response.json()
    resp2 = response2.json()
    return {
        "sanic_response": resp,
        "specific_response": resp2
    }


@health_bp.route("/", methods=['GET'])
def health():
    return json.dumps({"status": "ok"})


@health_bp.route("/<docker_id>")
def docker_id_health(docker_id):
    resp = get_docker_health(docker_id)
    return json.dumps(resp)
