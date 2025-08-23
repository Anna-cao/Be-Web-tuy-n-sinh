from flask import Blueprint, request, jsonify
from models.major import Major
from schemas.major import MajorCreate, MajorUpdate, MajorResponse, APIResponse
from database import db

major_bp = Blueprint("major_bp", __name__)

major_create_schema = MajorCreate()
major_update_schema = MajorUpdate()
major_response_schema = MajorResponse()
api_response_schema = APIResponse()

@major_bp.route("/", methods=["POST"])
def create_major():
    data = major_create_schema.load(request.json)
    new_major = Major(**data)
    db.session.add(new_major)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": "Major created",
        "data": major_response_schema.dump(new_major)
    })
    return jsonify(response), 201

@major_bp.route("/", methods=["GET"])
def get_majors():
    majors = Major.query.all()
    result = [major_response_schema.dump(m) for m in majors]
    response = api_response_schema.dump({
        "success": True,
        "message": "List of majors",
        "data": result
    })
    return jsonify(response)

@major_bp.route("/<string:id>", methods=["GET"])
def get_major(id):
    major = Major.query.get_or_404(id)
    response = api_response_schema.dump({
        "success": True,
        "message": "Major found",
        "data": major_response_schema.dump(major)
    })
    return jsonify(response)

@major_bp.route("/<string:id>", methods=["PUT"])
def update_major(id):
    major = Major.query.get_or_404(id)
    data = major_update_schema.load(request.json)
    for key, value in data.items():
        setattr(major, key, value)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": "Major updated",
        "data": major_response_schema.dump(major)
    })
    return jsonify(response)

@major_bp.route("/<string:id>", methods=["DELETE"])
def delete_major(id):
    major = Major.query.get_or_404(id)
    db.session.delete(major)
    db.session.commit()
    response = api_response_schema.dump({
        "success": True,
        "message": f"Major {id} deleted",
        "data": None
    })
    return jsonify(response)
