from flask import Blueprint, jsonify

api_bp = Blueprint("api", __name__, url_prefix="/api/v1")

@api_bp.route("/wards/<int:ward_id>/candidates", methods=["GET"])
def get_candidates_by_ward(ward_id):
    """
    Simple endpoint for testing.
    Returns stub data.
    """
    try:
        data = [
            {"id": 1, "name": "Candidate A", "ward_id": ward_id},
            {"id": 2, "name": "Candidate B", "ward_id": ward_id},
        ]
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
