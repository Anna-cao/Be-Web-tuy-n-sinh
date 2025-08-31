
from flask import Blueprint
from models.exam_group import ExamGroup
from schemas.exam_group import ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse, APIResponse
from database import db
from routes.utils import swagger_decorator, crud_handler

exam_group_bp = Blueprint("exam_group_bp", __name__)

get_all, get_by_id, create, update, delete = crud_handler(
    ExamGroup, ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse, APIResponse, id_param="code"
)

@exam_group_bp.route("/", methods=["GET"])
@swagger_decorator("get_all", "ExamGroup")
def get_exam_groups():
    return get_all()

@exam_group_bp.route("/<string:code>", methods=["GET"])
@swagger_decorator("get_by_id", "ExamGroup")
def get_exam_group(code):
    return get_by_id(code)

@exam_group_bp.route("/", methods=["POST"])
@swagger_decorator("create", "ExamGroup")
def create_exam_group():
    return create()

@exam_group_bp.route("/<string:code>", methods=["PUT"])
@swagger_decorator("update", "ExamGroup")
def update_exam_group(code):
    return update(code)

@exam_group_bp.route("/<string:code>", methods=["DELETE"])
@swagger_decorator("delete", "ExamGroup")
def delete_exam_group(code):
    return delete(code)
