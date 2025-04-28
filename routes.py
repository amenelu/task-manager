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


# create a new task
@task_routes.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    task = Task(
        title=data["title"],
        description=data.get("description", ""),
        priority=data.get("priority", "low"),
        deadline=(
            datetime.fromisoformat(data["deadline"]) if "deadline" in data else None
        ),
    )
    db.session.add(task)
    db.session.commit()
    return jsonify({"message": "Task created", "task_id": task.id}), 201


# update a task
@task_routes.route("/task/<int>:id", methods=["PUT"])
def update_task(id):
    data = request.get_json()
    task = Task.query.get_or_404(id)
    task.title = data.get("title", task.title)
    task.description = data.get("description", task.description)
    task.priority = data.get("priority", task.priority)
    if "deadline" in data:
        task.deadline = datetime.fromisoformat(data["deadline"])
    task.completed = data.get("completed", task.completed)
    db.session.commit()
    return jsonify({"message": "Task updated!"})


# delete task
@task_routes.route("/tasks/<int>:id", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "task deleted"})
