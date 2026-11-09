from flask import Flask
import os

def create_app(config_class="config.Config"):
    app = Flask(
        __name__,
        template_folder=os.path.join(os.path.dirname(__file__), "templates")
    )
    app.config.from_object(config_class)

    # Blueprints
    from app.main.routes import main_bp
    from app.playground.routes import playground_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(playground_bp)

    print("Template folder:", app.template_folder)
    return app