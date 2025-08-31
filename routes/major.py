
from flask import Blueprint
from models.major import Major
from schemas.major import MajorCreate, MajorUpdate, MajorResponse, APIResponse
from database import db
from routes.utils import swagger_decorator, crud_handler

major_bp = Blueprint("major_bp", __name__)

get_all, get_by_id, create, update, delete = crud_handler(
    Major, MajorCreate, MajorUpdate, MajorResponse, APIResponse
)

@major_bp.route("/", methods=["GET"])
@swagger_decorator("get_all", "Major")
def get_majors():
    return get_all()

@major_bp.route("/<string:id>", methods=["GET"])
@swagger_decorator("get_by_id", "Major")
def get_major(id):
    return get_by_id(id)

@major_bp.route("/", methods=["POST"])
@swagger_decorator("create", "Major")
def create_major():
    return create()

@major_bp.route("/<string:id>", methods=["PUT"])
@swagger_decorator("update", "Major")
def update_major(id):
    return update(id)

@major_bp.route("/<string:id>", methods=["DELETE"])
@swagger_decorator("delete", "Major")
def delete_major(id):
    return delete(id)
