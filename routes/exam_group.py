from flask import Blueprint, request, jsonify
from models.exam_group import ExamGroup
from schemas.exam_group import ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse, APIResponse
from database import db

exam_group_bp = Blueprint("exam_group_bp", __name__)

eg_create_schema = ExamGroupCreate()
eg_update_schema = ExamGroupUpdate()
eg_response_schema = ExamGroupResponse()
api_response_schema = APIResponse()

@exam_group_bp.route("/", methods=["POST"])
def create_exam_group():
    data = eg_create_schema.load(request.json)
    new_eg = ExamGroup(**data)
    db.session.add(new_eg)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": "Exam group created",
        "data": eg_response_schema.dump(new_eg)
    })
    return jsonify(response), 201

@exam_group_bp.route("/", methods=["GET"])
def get_exam_groups():
    groups = ExamGroup.query.all()
    result = [eg_response_schema.dump(g) for g in groups]
    response = api_response_schema.dump({
        "success": True,
        "message": "List of exam groups",
        "data": result
    })
    return jsonify(response)

@exam_group_bp.route("/<string:code>", methods=["GET"])
def get_exam_group(code):
    eg = ExamGroup.query.get_or_404(code)
    response = api_response_schema.dump({
        "success": True,
        "message": "Exam group found",
        "data": eg_response_schema.dump(eg)
    })
    return jsonify(response)

@exam_group_bp.route("/<string:code>", methods=["PUT"])
def update_exam_group(code):
    eg = ExamGroup.query.get_or_404(code)
    data = eg_update_schema.load(request.json)
    for key, value in data.items():
        setattr(eg, key, value)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": "Exam group updated",
        "data": eg_response_schema.dump(eg)
    })
    return jsonify(response)

@exam_group_bp.route("/<string:code>", methods=["DELETE"])
def delete_exam_group(code):
    eg = ExamGroup.query.get_or_404(code)
    db.session.delete(eg)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": f"Exam group {code} deleted",
        "data": None
    })
    return jsonify(response)
