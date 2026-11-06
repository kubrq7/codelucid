from flask import Flask
from .extensions import mail, login_manager
import os

def create_app(config_class="config.Config"):
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates")
    )

    # Config
    app.config.from_object(config_class)

    # Extensions
    mail.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # Blueprints
    from app.auth.routes import auth_bp
    from app.main.routes import main_bp
    from app.playground.routes import playground_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(playground_bp)

    print("Template folder:", app.template_folder)

    return app

