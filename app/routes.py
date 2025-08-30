from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return "<h1>Welcome to Student Revision Platform</h1>"
