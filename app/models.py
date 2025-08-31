# app/models.py
from . import db
from datetime import datetime

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    full_name = db.Column(db.String(255))
    role = db.Column(db.String(20), default="student")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def check_password(self, password):
        from . import bcrypt
        return bcrypt.check_password_hash(self.password_hash, password)

class Material(db.Model):
    __tablename__ = "materials"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    filename = db.Column(db.String(512))
    storage_url = db.Column(db.String(1024))
    uploader_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    uploader = db.relationship("User", backref="materials")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    material_id = db.Column(db.Integer, db.ForeignKey("materials.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    material = db.relationship("Material", backref="comments")
    user = db.relationship("User", backref="comments")

class Donation(db.Model):
    __tablename__ = "donations"
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(10,2))
    currency = db.Column(db.String(10))
    payer = db.Column(db.String(255))  # optional display name/email
    status = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
