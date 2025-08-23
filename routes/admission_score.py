from flask import Blueprint, request, jsonify
from models.admission_score import AdmissionScore
from schemas.admission_score import AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse, APIResponse
from database import db

admission_score_bp = Blueprint("admission_score_bp", __name__)

as_create_schema = AdmissionScoreCreate()
as_update_schema = AdmissionScoreUpdate()
as_response_schema = AdmissionScoreResponse()
api_response_schema = APIResponse()

@admission_score_bp.route("/", methods=["POST"])
def create_admission_score():
    data = as_create_schema.load(request.json)
    new_as = AdmissionScore(**data)
    db.session.add(new_as)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": "Admission score created",
        "data": as_response_schema.dump(new_as)
    })
    return jsonify(response), 201

@admission_score_bp.route("/", methods=["GET"])
def get_admission_scores():
    scores = AdmissionScore.query.all()
    result = [as_response_schema.dump(s) for s in scores]
    response = api_response_schema.dump({
        "success": True,
        "message": "List of admission scores",
        "data": result
    })
    return jsonify(response)

@admission_score_bp.route("/<string:id>", methods=["GET"])
def get_admission_score(id):
    score = AdmissionScore.query.get_or_404(id)
    response = api_response_schema.dump({
        "success": True,
        "message": "Admission score found",
        "data": as_response_schema.dump(score)
    })
    return jsonify(response)

@admission_score_bp.route("/<string:id>", methods=["PUT"])
def update_admission_score(id):
    score = AdmissionScore.query.get_or_404(id)
    data = as_update_schema.load(request.json)
    for key, value in data.items():
        setattr(score, key, value)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": "Admission score updated",
        "data": as_response_schema.dump(score)
    })
    return jsonify(response)

@admission_score_bp.route("/<string:id>", methods=["DELETE"])
def delete_admission_score(id):
    score = AdmissionScore.query.get_or_404(id)
    db.session.delete(score)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": f"Admission score {id} deleted",
        "data": None
    })
    return jsonify(response)
