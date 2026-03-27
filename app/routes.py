from flask import Blueprint, request, jsonify
from .models import db, Student

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return "Student Management System Backend Running!"


@main.route("/add-student", methods=["POST"])
def add_student():
    data = request.get_json()

    if not data or not data.get("name") or not data.get("email") or not data.get("course"):
        return jsonify({"error": "All fields are required"}), 400

    existing_student = Student.query.filter_by(email=data["email"]).first()
    if existing_student:
        return jsonify({"error": "Email already exists"}), 400

    new_student = Student(
        name=data["name"],
        email=data["email"],
        course=data["course"]
    )

    db.session.add(new_student)
    db.session.commit()

    return jsonify({"message": "Student added successfully!"}), 201


@main.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    output = []
    for student in students:
        output.append({
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "course": student.course
        })

    return jsonify(output)


@main.route("/update-student/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    if "name" in data:
        student.name = data["name"]
    if "email" in data:
        student.email = data["email"]
    if "course" in data:
        student.course = data["course"]

    db.session.commit()

    return jsonify({"message": "Student updated successfully"})


@main.route("/delete-student/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"})