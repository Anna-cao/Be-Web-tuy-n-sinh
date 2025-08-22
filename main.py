import os
from flask import Flask
from flasgger import Swagger
from database import db
from routes.university import university_bp
from routes.major import major_bp
from routes.exam_group import exam_group_bp
from routes.admission_data import admission_score_bp

def create_app():
    app = Flask(__name__)

    
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "mssql+pyodbc://localhost/DuAn?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SWAGGER"] = {"title": "Tuyển Sinh API", "universion": 3}

    db.init_app(app)
    Swagger(app)

    app.register_blueprint(university_bp, url_prefix="/api/universities")
    app.register_blueprint(major_bp, url_prefix="/api/majors")
    app.register_blueprint(exam_group_bp, url_prefix="/api/exam-groups")
    app.register_blueprint(admission_score_bp)

    @app.route("/")
    def home():
        return "Welcome to Tuyển Sinh API!"

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
