from flask import Blueprint, jsonify

comments_bp = Blueprint("comments", __name__)

@comments_bp.route("/", methods=["GET"])
def get_comments():
    return jsonify({"message": "Comments endpoint works!"})
