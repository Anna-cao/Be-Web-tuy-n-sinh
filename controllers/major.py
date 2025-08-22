from flask import jsonify
from services.major import MajorService
from schemas.major import MajorCreate, MajorUpdate, MajorResponse, APIResponse
from marshmallow import ValidationError

class MajorController:
    @staticmethod
    def get_all():
        majors = MajorService.get_all()
        result = MajorResponse(many=True).dump(majors)
        return jsonify(APIResponse().dump({"success": True, "message": "List of majors", "data": {"items": result}})), 200

    @staticmethod
    def get_by_id(id):
        major = MajorService.get_by_id(id)
        if not major:
            return jsonify(APIResponse().dump({"success": False, "message": "Major not found", "data": None})), 404
        result = MajorResponse().dump(major)
        return jsonify(APIResponse().dump({"success": True, "message": "Major details", "data": result})), 200

    @staticmethod
    def create(data):
        try:
            validated = MajorCreate().load(data)
            major = MajorService.create(validated)
            result = MajorResponse().dump(major)
            return jsonify(APIResponse().dump({"success": True, "message": "Major created successfully", "data": result})), 201
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def update(id, data):
        try:
            validated = MajorUpdate().load(data)
            major = MajorService.update(id, validated)
            if not major:
                return jsonify(APIResponse().dump({"success": False, "message": "Major not found", "data": None})), 404
            result = MajorResponse().dump(major)
            return jsonify(APIResponse().dump({"success": True, "message": "Major updated successfully", "data": result})), 200
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def delete(id):
        major = MajorService.delete(id)
        if not major:
            return jsonify(APIResponse().dump({"success": False, "message": "Major not found", "data": None})), 404
        return jsonify(APIResponse().dump({"success": True, "message": "Deleted successfully", "data": None})), 200
