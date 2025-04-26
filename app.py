from flask import Flask
from models import db
from routes import task_routes

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(task_routes)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=True)
