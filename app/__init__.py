from flask import Flask
def create_app():
    app = Flask(__name__)

    from .routes.universities import universities_bp
    from .routes.majors import majors_bp
    from .routes.exam_groups import exam_groups_bp
    from .routes.admission_scores import admission_scores_bp

    app.register_blueprint(universities_bp)
    app.register_blueprint(majors_bp)
    app.register_blueprint(exam_groups_bp)
    app.register_blueprint(admission_scores_bp)

    return app
