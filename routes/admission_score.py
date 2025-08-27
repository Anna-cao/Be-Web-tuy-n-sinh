from flask import Blueprint
from models.admission_score import AdmissionScore
from schemas.admission_score import AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse, APIResponse
from database import db
from routes.utils import swagger_decorator, crud_handler

admission_score_bp = Blueprint("admission_score_bp", __name__)

get_all, get_by_id, create, update, delete = crud_handler(
    AdmissionScore, AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse, APIResponse
)

@admission_score_bp.route("/", methods=["GET"])
@swagger_decorator("get_all", "AdmissionScore")
def get_admission_scores():
    return get_all()

@admission_score_bp.route("/<string:id>", methods=["GET"])
@swagger_decorator("get_by_id", "AdmissionScore")
def get_admission_score(id):
    return get_by_id(id)

@admission_score_bp.route("/", methods=["POST"])
@swagger_decorator("create", "AdmissionScore")
def create_admission_score():
    return create()

@admission_score_bp.route("/<string:id>", methods=["PUT"])
@swagger_decorator("update", "AdmissionScore")
def update_admission_score(id):
    return update(id)

@admission_score_bp.route("/<string:id>", methods=["DELETE"])
@swagger_decorator("delete", "AdmissionScore")
def delete_admission_score(id):
    return delete(id)