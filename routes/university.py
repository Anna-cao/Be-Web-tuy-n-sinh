
from flask import Blueprint
from models.university import University
from schemas.university import UniversityCreate, UniversityUpdate, UniversityResponse, APIResponse
from database import db
from routes.utils import swagger_decorator, crud_handler

university_bp = Blueprint("university_bp", __name__)

get_all, get_by_id, create, update, delete = crud_handler(
    University, UniversityCreate, UniversityUpdate, UniversityResponse, APIResponse
)

@university_bp.route("/", methods=["GET"])
@swagger_decorator("get_all", "University")
def get_universities():
    return get_all()

@university_bp.route("/<string:id>", methods=["GET"])
@swagger_decorator("get_by_id", "University")
def get_university(id):
    return get_by_id(id)

@university_bp.route("/", methods=["POST"])
@swagger_decorator("create", "University")
def create_university():
    return create()

@university_bp.route("/<string:id>", methods=["PUT"])
@swagger_decorator("update", "University")
def update_university(id):
    return update(id)

@university_bp.route("/<string:id>", methods=["DELETE"])
@swagger_decorator("delete", "University")
def delete_university(id):
    return delete(id)
