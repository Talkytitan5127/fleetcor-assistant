from flask import Flask
from accounts.app.ext.api_info import ApiInfo
from accounts.app.ext.routes_prefixer import RoutesPrefixer
from accounts.app.models import db
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

api_info = ApiInfo()

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    prefixer = RoutesPrefixer(app, app.config['APPLICATION_ROOT'])

    api_info.init_app(app)
    db.init_app(app)

    migrate = Migrate(app, db)

    from accounts.app.auth import jwt
    jwt.init_app(app)

    from accounts.app.accounts import accounts
    app.register_blueprint(accounts, url_prefix='/accounts')

    from accounts.app.app_error import process_error
    app.register_error_handler(404, process_error)

    from accounts.app.bills import bills
    app.register_blueprint(bills, url_prefix='/bills')

    from accounts.app.auth import auth
    app.register_blueprint(auth)

    return app
