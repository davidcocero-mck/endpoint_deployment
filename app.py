import os
import sys

sys.path.append("/app/project/prisma")
from api.routes import api
from flask import Flask
from flask_cors import CORS


def create_app():
    """Factory function to create Flask app"""
    app = Flask(__name__)

    # Enable CORS
    CORS(app)

    # Register API routes
    app.register_blueprint(api, url_prefix="/api")

    return app


app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
