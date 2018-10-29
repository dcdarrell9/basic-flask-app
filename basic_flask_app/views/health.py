import json

from flask import Blueprint

health_bp = Blueprint("health_bp", __name__,  static_folder='static', template_folder='templates')


@health_bp.route("/")
def health():
    return json.dumps({"status": "ok"})
