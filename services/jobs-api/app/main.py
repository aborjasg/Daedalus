from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health() -> dict[str, str]:
        return {"service": "jobs-api", "status": "ok"}

    return app


app = create_app()
