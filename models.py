from flask_sqlalchemy import SQLALCHEMY
from datetime import datetime, timezone

db = SQLALCHEMY()


class Task:
    id = db.Column(db.Intege, primary_key=True)
    title = db.Column(db.String(150), nullble=False)
    description = db.Column(db.Text, nullble=True)
    priority = db.Column(db.String(10), nullble=False)
    deadline = db.Column(db.DateTime, nullble=True)
    completed = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
