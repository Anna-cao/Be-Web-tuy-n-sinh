import os
from flask import Flask
from flasgger import Swagger
from flask_migrate import Migrate, upgrade
from database import db
from routes.university import university_bp
from routes.major import major_bp
from routes.exam_group import exam_group_bp
from routes.admission_score import admission_score_bp


def create_app():
    app = Flask(__name__)

    # Cấu hình DB
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(
        "DATABASE_URL",
        "postgresql+psycopg2://postgres:123456@localhost:5432/DuAn"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SWAGGER"] = {"title": "Tuyển Sinh API", "version": 3}

    # Khởi tạo DB & Migrate
    db.init_app(app)
    migrate = Migrate(app, db)

    # Đăng ký Swagger
    Swagger(app)

    # Đăng ký Blueprint
    app.register_blueprint(university_bp, url_prefix="/api/universities")
    app.register_blueprint(major_bp, url_prefix="/api/majors")
    app.register_blueprint(exam_group_bp, url_prefix="/api/exam-groups")
    app.register_blueprint(admission_score_bp, url_prefix="/api/admission-scores")

    # Route test
    @app.route("/")
    def home():
        return "Welcome to Tuyển Sinh API!"

    return app


# Khởi tạo app để Flask CLI nhận diện
app = create_app()

# Tự động áp dụng migration khi app start
with app.app_context():
    upgrade()

if __name__ == "__main__":
    # In tất cả các route ra màn hình
    for rule in app.url_map.iter_rules():
        print(rule)
    port = int(os.getenv("PORT", 5000))
    # debug=False khi deploy production
    app.run(host="0.0.0.0", port=port, debug=False)
