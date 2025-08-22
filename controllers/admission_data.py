from flask import jsonify
from services.admission_data import AdmissionScoreService
from schemas.admission_data import AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse, APIResponse
from marshmallow import ValidationError

class AdmissionScoreController:
    @staticmethod
    def get_all():
        scores = AdmissionScoreService.get_all()
        result = AdmissionScoreResponse(many=True).dump(scores)
        return jsonify(APIResponse().dump({"success": True, "message": "List of admission scores", "data": {"items": result}})), 200

    @staticmethod
    def get_by_id(id):
        score = AdmissionScoreService.get_by_id(id)
        if not score:
            return jsonify(APIResponse().dump({"success": False, "message": "Score not found", "data": None})), 404
        result = AdmissionScoreResponse().dump(score)
        return jsonify(APIResponse().dump({"success": True, "message": "Admission score details", "data": result})), 200

    @staticmethod
    def create(data):
        try:
            validated = AdmissionScoreCreate().load(data)
            score = AdmissionScoreService.create(validated)
            result = AdmissionScoreResponse().dump(score)
            return jsonify(APIResponse().dump({"success": True, "message": "Admission score created successfully", "data": result})), 201
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def update(id, data):
        try:
            validated = AdmissionScoreUpdate().load(data)
            score = AdmissionScoreService.update(id, validated)
            if not score:
                return jsonify(APIResponse().dump({"success": False, "message": "Score not found", "data": None})), 404
            result = AdmissionScoreResponse().dump(score)
            return jsonify(APIResponse().dump({"success": True, "message": "Admission score updated successfully", "data": result})), 200
        except ValidationError as err:
            return jsonify(APIResponse().dump({"success": False, "message": err.messages, "data": None})), 400

    @staticmethod
    def delete(id):
        score = AdmissionScoreService.delete(id)
        if not score:
            return jsonify(APIResponse().dump({"success": False, "message": "Score not found", "data": None})), 404
        return jsonify(APIResponse().dump({"success": True, "message": "Deleted successfully", "data": None})), 200
