from flask import Blueprint, request, jsonify
from models import db, Task
from datetime import datetime

task_routes = Blueprint("tasks", __name__)


# get all tasks
@task_routes.route("/tasks", methods=["GET"])
def tasks():
    tasks = Task.query.order_by(Task.priority.desc(), Task.deadline).all()
    return jsonify(
        [
            {
                "id": task.id,
                "title": task.title,
                "description": task.description if task.description else None,
                "priority": task.priority,
                "deadline": task.deadline.isoformat() if task.deadline else None,
                "completed": task.completed,
                "created_at": task.created_at,
            }
            for task in tasks
        ]
    )
