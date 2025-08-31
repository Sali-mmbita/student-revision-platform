# app/routes/__init__.py
from flask import Flask
from .auth import auth_bp
from .materials import materials_bp
from .search import search_bp
from .comments import comments_bp
from .donations import donations_bp
from .main import main_bp

def register_routes(app: Flask):
    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(materials_bp, url_prefix="/api/materials")
    app.register_blueprint(search_bp, url_prefix="/api/search")
    app.register_blueprint(comments_bp, url_prefix="/api/comments")
    app.register_blueprint(donations_bp, url_prefix="/api/donations")
    app.register_blueprint(main_bp)  # root '/'
