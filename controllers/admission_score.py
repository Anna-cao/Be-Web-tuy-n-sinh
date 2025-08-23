from flask import request, jsonify
from schemas.admission_score_schema import AdmissionScoreCreate, AdmissionScoreUpdate, AdmissionScoreResponse, APIResponse
from services.admission_score_service import AdmissionScoreService

score_create_schema = AdmissionScoreCreate()
score_update_schema = AdmissionScoreUpdate()
score_response_schema = AdmissionScoreResponse()
api_response_schema = APIResponse()

class AdmissionScoreController:
    @staticmethod
    def get_all():
        data = AdmissionScoreService.get_all()
        response = api_response_schema.dump({
            "success": True,
            "message": "List of admission scores",
            "data": [score_response_schema.dump(s) for s in data]
        })
        return jsonify(response)

    @staticmethod
    def get_by_id(id):
        s = AdmissionScoreService.get_by_id(id)
        if not s:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Admission score found",
            "data": score_response_schema.dump(s)
        })
        return jsonify(response)

    @staticmethod
    def create():
        data = score_create_schema.load(request.json)
        s = AdmissionScoreService.create(data)
        response = api_response_schema.dump({
            "success": True,
            "message": "Admission score created",
            "data": score_response_schema.dump(s)
        })
        return jsonify(response), 201

    @staticmethod
    def update(id):
        data = score_update_schema.load(request.json)
        s = AdmissionScoreService.update(id, data)
        if not s:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Admission score updated",
            "data": score_response_schema.dump(s)
        })
        return jsonify(response)

    @staticmethod
    def delete(id):
        s = AdmissionScoreService.delete(id)
        if not s:
            return jsonify(api_response_schema.dump({"success": False, "message": "Not found", "data": {}})), 404
        response = api_response_schema.dump({
            "success": True,
            "message": "Admission score deleted",
            "data": {}
        })
        return jsonify(response)
