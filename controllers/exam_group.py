from flask import jsonify
from services.exam_group import ExamGroupService
from schemas.exam_group import ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse, APIResponse
from marshmallow import ValidationError

class ExamGroupController:
    @staticmethod
    def get_all():
        groups = ExamGroupService.get_all()
        result = ExamGroupResponse(many=True).dump(groups)
        return jsonify(APIResponse().dump({"success": True, "message": "List of exam groups", "data": {"items": result}})), 200

    @staticmethod
    def get_by_id(id):
        group = ExamGroupService.get_by_id(id)
        if not group:
            return jsonify(APIResponse().dump({"success": False, "message": "Exam group not found", "data": None})), 404
        result = ExamGroupResponse().dump(group)
        return jsonify(APIResponse().dump({"success": True, "message": "Exam group details", "data": result})), 200

    @staticmethod
    def create(data):
        try:
            validated = ExamGroupCreate().load(data)
            group = ExamGroupService.create(validated)
            result = ExamGroupResponse().dump(group)
            return jsonify(APIResponse().dump({"success": True, "message": "Exam group created successfully", "data": result})), 201
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def update(id, data):
        try:
            validated = ExamGroupUpdate().load(data)
            group = ExamGroupService.update(id, validated)
            if not group:
                return jsonify(APIResponse().dump({"success": False, "message": "Exam group not found", "data": None})), 404
            result = ExamGroupResponse().dump(group)
            return jsonify(APIResponse().dump({"success": True, "message": "Exam group updated successfully", "data": result})), 200
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def delete(id):
        group = ExamGroupService.delete(id)
        if not group:
            return jsonify(APIResponse().dump({"success": False, "message": "Exam group not found", "data": None})), 404
        return jsonify(APIResponse().dump({"success": True, "message": "Deleted successfully", "data": None})), 200
