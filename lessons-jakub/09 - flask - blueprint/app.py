import secrets
from flask import Flask
from flask_bs4 import Bootstrap

from main.routes import main_bp
from auth.routes import auth_bp


def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    app.config['SECRET_KEY'] = secrets.token_urlsafe(32)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix='/auth')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)