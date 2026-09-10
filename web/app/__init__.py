from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    @app.get("/")
    def index() -> str:
        return "Daedalus-Control Panel"

    return app
