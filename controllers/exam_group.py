from flask import request, jsonify
from schemas.exam_group import ExamGroupCreate, ExamGroupUpdate, ExamGroupResponse, APIResponse
from services.exam_group import ExamGroupService

group_create_schema = ExamGroupCreate()
group_update_schema = ExamGroupUpdate()
group_response_schema = ExamGroupResponse()
api_response_schema = APIResponse()

class ExamGroupController:
    @staticmethod
    def get_all():
        data = ExamGroupService.get_all()
        response = api_response_schema.dump({
            "success": True,
            "message": "List of exam groups",
            "data": [group_response_schema.dump(g) for g in data]
        })
        return jsonify(response)

    @staticmethod
    def get_by_id(group_code):
        g = ExamGroupService.get_by_id(group_code)
        if not g:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Exam group found",
            "data": group_response_schema.dump(g)
        })
        return jsonify(response)

    @staticmethod
    def create():
        data = group_create_schema.load(request.json)
        g = ExamGroupService.create(data)
        response = api_response_schema.dump({
            "success": True,
            "message": "Exam group created",
            "data": group_response_schema.dump(g)
        })
        return jsonify(response), 201

    @staticmethod
    def update(group_code):
        data = group_update_schema.load(request.json)
        g = ExamGroupService.update(group_code, data)
        if not g:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Exam group updated",
            "data": group_response_schema.dump(g)
        })
        return jsonify(response)

    @staticmethod
    def delete(group_code):
        g = ExamGroupService.delete(group_code)
        if not g:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Exam group deleted",
            "data": {}
        })
        return jsonify(response)