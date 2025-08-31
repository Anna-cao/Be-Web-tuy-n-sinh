
from flask import request, jsonify
from schemas.university import UniversityCreate, UniversityUpdate, UniversityResponse, APIResponse
from services.university import UniversityService

uni_create_schema = UniversityCreate()
uni_update_schema = UniversityUpdate()
uni_response_schema = UniversityResponse()
api_response_schema = APIResponse()

class UniversityController:
    @staticmethod
    def get_all():
        data = UniversityService.get_all()
        response = api_response_schema.dump({
            "success": True,
            "message": "List of universities",
            "data": [uni_response_schema.dump(u) for u in data]
        })
        return jsonify(response)

    @staticmethod
    def get_by_id(id):
        u = UniversityService.get_by_id(id)
        if not u:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "University found",
            "data": uni_response_schema.dump(u)
        })
        return jsonify(response)

    @staticmethod
    def create():
        data = uni_create_schema.load(request.json)
        u = UniversityService.create(data)
        response = api_response_schema.dump({
            "success": True,
            "message": "University created",
            "data": uni_response_schema.dump(u)
        })
        return jsonify(response), 201

    @staticmethod
    def update(id):
        data = uni_update_schema.load(request.json)
        u = UniversityService.update(id, data)
        if not u:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "University updated",
            "data": uni_response_schema.dump(u)
        })
        return jsonify(response)

    @staticmethod
    def delete(id):
        u = UniversityService.delete(id)
        if not u:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "University deleted",
            "data": {}
        })
        return jsonify(response)
