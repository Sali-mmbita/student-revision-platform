from flask import Blueprint, jsonify

search_bp = Blueprint("search", __name__)

@search_bp.route("/", methods=["GET"])
def search():
    return jsonify({"message": "Search endpoint works!"})
