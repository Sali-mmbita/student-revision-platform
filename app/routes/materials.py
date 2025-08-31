# app/routes/materials.py
from flask import Blueprint, request, jsonify
from .. import db
from ..models import Material

materials_bp = Blueprint("materials", __name__)

@materials_bp.route("/", methods=["GET"])
def list_materials():
    q = Material.query.order_by(Material.created_at.desc()).limit(100).all()
    out = [
        {
            "id": m.id,
            "title": m.title,
            "description": m.description,
            "uploader_id": m.uploader_id,
            "created_at": m.created_at.isoformat(),
        }
        for m in q
    ]
    return jsonify({"materials": out})

@materials_bp.route("/", methods=["POST"])
def create_material():
    data = request.get_json() or {}
    title = data.get("title")
    description = data.get("description", "")
    uploader_id = data.get("uploader_id")  # in reality get from JWT

    if not title or not uploader_id:
        return jsonify({"msg": "title and uploader_id required"}), 400

    m = Material(title=title, description=description, uploader_id=uploader_id)
    db.session.add(m)
    db.session.commit()

    return jsonify({"id": m.id, "msg": "material created"}), 201
