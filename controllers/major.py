from flask import request, jsonify
from schemas.major import MajorCreate, MajorUpdate, MajorResponse, APIResponse
from services.major import MajorService

major_create_schema = MajorCreate()
major_update_schema = MajorUpdate()
major_response_schema = MajorResponse()
api_response_schema = APIResponse()

class MajorController:
    @staticmethod
    def get_all():
        data = MajorService.get_all()
        response = api_response_schema.dump({
            "success": True,
            "message": "List of majors",
            "data": [major_response_schema.dump(m) for m in data]
        })
        return jsonify(response)

    @staticmethod
    def get_by_id(major_id):
        m = MajorService.get_by_id(major_id)
        if not m:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Major found",
            "data": major_response_schema.dump(m)
        })
        return jsonify(response)

    @staticmethod
    def create():
        data = major_create_schema.load(request.json)
        m = MajorService.create(data)
        response = api_response_schema.dump({
            "success": True,
            "message": "Major created",
            "data": major_response_schema.dump(m)
        })
        return jsonify(response), 201

    @staticmethod
    def update(major_id):
        data = major_update_schema.load(request.json)
        m = MajorService.update(major_id, data)
        if not m:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Major updated",
            "data": major_response_schema.dump(m)
        })
        return jsonify(response)

    @staticmethod
    def delete(major_id):
        m = MajorService.delete(major_id)
        if not m:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Major deleted",
            "data": {}
        })
        return jsonify(response)