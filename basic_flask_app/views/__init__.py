from basic_flask_app import app
from basic_flask_app.views.health import health_bp
from basic_flask_app.views.info import info_bp


app.register_blueprint(health_bp, url_prefix="/health")
app.register_blueprint(info_bp, url_prefix="/info")

