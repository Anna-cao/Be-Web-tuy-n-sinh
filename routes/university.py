from flask import Blueprint, request, jsonify
from models.university import University
from schemas.university import UniversityCreate, UniversityUpdate, UniversityResponse, APIResponse
from database import db

university_bp = Blueprint("university_bp", __name__)

uni_create_schema = UniversityCreate()
uni_update_schema = UniversityUpdate()
uni_response_schema = UniversityResponse()
api_response_schema = APIResponse()


@university_bp.route("/", methods=["POST"])
def create_university():
    data = uni_create_schema.load(request.json)
    new_uni = University(**data)
    db.session.add(new_uni)
    db.session.commit()
    
    response = api_response_schema.dump({
        "success": True,
        "message": "University created",
        "data": uni_response_schema.dump(new_uni)
    })
    return jsonify(response), 201


@university_bp.route("/", methods=["GET"])
def get_universities():
    universities = University.query.all()
    result = [uni_response_schema.dump(u) for u in universities]
    
    response = api_response_schema.dump({
        "success": True,
        "message": "List of universities",
        "data": result
    })
    return jsonify(response)


@university_bp.route("/<string:id>", methods=["GET"])
def get_university(id):
    uni = University.query.get_or_404(id)
    response = api_response_schema.dump({
        "success": True,
        "message": "University found",
        "data": uni_response_schema.dump(uni)
    })
    return jsonify(response)


@university_bp.route("/<string:id>", methods=["PUT"])
def update_university(id):
    uni = University.query.get_or_404(id)
    data = uni_update_schema.load(request.json)
    
    for key, value in data.items():
        setattr(uni, key, value)
    
    db.session.commit()
    
    response = api_response_schema.dump({
        "success": True,
        "message": "University updated",
        "data": uni_response_schema.dump(uni)
    })
    return jsonify(response)


@university_bp.route("/<string:id>", methods=["DELETE"])
def delete_university(id):
    uni = University.query.get_or_404(id)
    db.session.delete(uni)
    db.session.commit()
    
    response = api_response_schema.dump({
        "success": True,
        "message": f"University {id} deleted",
        "data": None
    })
    return jsonify(response)
