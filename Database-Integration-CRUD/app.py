from flask import Flask, request, jsonify, render_template
from database import db
from models import User

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()


# ---------------- HOME PAGE ---------------- #

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- CREATE USER ---------------- #

@app.route("/users", methods=["POST"])
def create_user():

    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid data"}), 400

    name = data.get("name")
    email = data.get("email")
    age = data.get("age")

    if not name or not email:
        return jsonify({"message": "Name and Email are required"}), 400

    existing = User.query.filter_by(email=email).first()

    if existing:
        return jsonify({"message": "Email already exists"}), 409

    user = User(
        name=name,
        email=email,
        age=age
    )

    db.session.add(user)
    db.session.commit()

    return jsonify(user.to_dict()), 201


# ---------------- READ ALL USERS ---------------- #

@app.route("/users", methods=["GET"])
def get_users():

    users = User.query.all()

    return jsonify([user.to_dict() for user in users])


# ---------------- READ SINGLE USER ---------------- #

@app.route("/users/<int:id>", methods=["GET"])
def get_user(id):

    user = User.query.get_or_404(id)

    return jsonify(user.to_dict())


# ---------------- UPDATE USER ---------------- #

@app.route("/users/<int:id>", methods=["PUT"])
def update_user(id):

    user = User.query.get_or_404(id)

    data = request.get_json()

    email = data.get("email")

    duplicate = User.query.filter(
        User.email == email,
        User.id != id
    ).first()

    if duplicate:
        return jsonify({
            "message": "Email already exists"
        }), 409

    user.name = data.get("name", user.name)
    user.email = email
    user.age = data.get("age", user.age)

    db.session.commit()

    return jsonify(user.to_dict())


# ---------------- DELETE USER ---------------- #

@app.route("/users/<int:id>", methods=["DELETE"])
def delete_user(id):

    user = User.query.get_or_404(id)

    db.session.delete(user)

    db.session.commit()

    return jsonify({
        "message": "User deleted successfully"
    })


# ---------------- RUN ---------------- #

if __name__ == "__main__":
    app.run(debug=True)
