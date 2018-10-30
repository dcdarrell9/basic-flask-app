import json

import requests
from flask import Blueprint
from requests.exceptions import HTTPError
from structlog import get_logger

from basic_flask_app import app

health_bp = Blueprint('health_bp', __name__,  static_folder='static', template_folder='templates')

logger = get_logger()


def get_docker_health():
    logger.debug('Retrieving docker health')
    url = f'{app.config["SANIC_APP_URL"]}/health'
    response = requests.get(url)

    try:
        response.raise_for_status()
    except HTTPError:
        logger.exception('Docker health retrieval failed')
        raise Exception

    logger.debug('Successfully retrieved docker health')
    resp = response.json()
    return resp


@health_bp.route("/")
def health():
    test = get_docker_health()
    return json.dumps({"status": "ok"})


@health_bp.route("/<docker_id>")
def docker_id_health(docker_id):
    logger.debug('Retrieving docker health for id', docker_id=docker_id)
    url = f'{app.config["SANIC_APP_URL"]}/health'
    response = requests.get(url)

    try:
        response.raise_for_status()
    except HTTPError:
        logger.exception('Docker health retrieval failed', docker_id=docker_id)
        raise Exception

    logger.debug('Successfully retrieved docker health', docker_id=docker_id)
    resp = response.json()
    return resp