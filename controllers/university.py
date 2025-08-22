from flask import jsonify
from services.university import UniversityService
from schemas.university import UniversityCreate, UniversityUpdate, UniversityResponse, APIResponse
from marshmallow import ValidationError

class UniversityController:
    @staticmethod
    def get_all():
        universities = UniversityService.get_all()
        result = UniversityResponse(many=True).dump(universities)
        return jsonify(APIResponse().dump({"success": True, "message": "List of universities", "data": {"items": result}})), 200

    @staticmethod
    def get_by_id(id):
        university = UniversityService.get_by_id(id)
        if not university:
            return jsonify(APIResponse().dump({"success": False, "message": "University not found", "data": None})), 404
        result = UniversityResponse().dump(university)
        return jsonify(APIResponse().dump({"success": True, "message": "University details", "data": result})), 200

    @staticmethod
    def create(data):
        try:
            validated = UniversityCreate().load(data)
            university = UniversityService.create(validated)
            result = UniversityResponse().dump(university)
            return jsonify(APIResponse().dump({"success": True, "message": "Post created successfully", "data": result})), 201
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def update(id, data):
        try:
            validated = UniversityUpdate().load(data)
            university = UniversityService.update(id, validated)
            if not university:
                return jsonify(APIResponse().dump({"success": False, "message": "University not found", "data": None})), 404
            result = UniversityResponse().dump(university)
            return jsonify(APIResponse().dump({"success": True, "message": "University updated successfully", "data": result})), 200
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def delete(id):
        university = UniversityService.delete(id)
        if not university:
            return jsonify(APIResponse().dump({"success": False, "message": "University not found", "data": None})), 404
        return jsonify(APIResponse().dump({"success": True, "message": "Deleted successfully", "data": None})), 200
