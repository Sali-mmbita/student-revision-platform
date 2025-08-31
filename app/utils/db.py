import mysql.connector
from flask import current_app, g

def init_db(app):
    """Initialize DB connection settings."""
    app.teardown_appcontext(close_db)

def get_db():
    """Get a database connection, store it in Flask 'g' object."""
    if "db" not in g:
        g.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="student_revision"
        )
    return g.db

def close_db(e=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
