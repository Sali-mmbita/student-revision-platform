from flask import Blueprint, jsonify

donations_bp = Blueprint("donations", __name__)

@donations_bp.route("/", methods=["POST"])
def donate():
    return jsonify({"message": "Donations endpoint works!"})
