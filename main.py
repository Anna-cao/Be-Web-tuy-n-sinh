import os
from flask import Flask
from flasgger import Swagger
from flask_migrate import Migrate
from database import db
from routes import register_routes
from config import Config  

def create_app():
    app = Flask(__name__, static_folder='flagger_static')

    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)

    # Cấu hình Swagger
    template = {
        'swagger': '2.0',
        'info': {
            'title': 'Tuyển Sinh API',
            'description': 'API for university admission data',
            'version': '1.0.0'
        },
        'host': 'localhost:5000',  
        'basePath': '/api'
    }
    Swagger(app, template=template)

    register_routes(app)

    @app.route("/")
    def home():
        return "Welcome to Tuyển Sinh API!"

    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)