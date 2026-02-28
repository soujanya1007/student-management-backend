from flask import Flask, request, jsonify
from config import Config
from models import db, Student

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

@app.route("/")
def home():
    return "Student Management System Backend Running!"


# ✅ Add Student (POST)
@app.route("/add-student", methods=["POST"])
def add_student():
    data = request.get_json()

    # Validate input
    if not data or not data.get("name") or not data.get("email") or not data.get("course"):
        return jsonify({"error": "All fields are required"}), 400

    # Check duplicate email
    existing_student = Student.query.filter_by(email=data["email"]).first()
    if existing_student:
        return jsonify({"error": "Email already exists"}), 400

    try:
        new_student = Student(
            name=data["name"],
            email=data["email"],
            course=data["course"]
        )

        db.session.add(new_student)
        db.session.commit()

        return jsonify({"message": "Student added successfully!"}), 201

    except Exception as e:
        return jsonify({"error": "Something went wrong"}), 500

# ✅ View Students (GET)
@app.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()

    output = []
    for student in students:
        student_data = {
            "id": student.id,
            "name": student.name,
            "email": student.email,
            "course": student.course
        }
        output.append(student_data)

    return jsonify(output)

# ✅ Delete Student
@app.route("/delete-student/<int:id>", methods=["DELETE"])
def delete_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    db.session.delete(student)
    db.session.commit()

    return jsonify({"message": "Student deleted successfully"})

# ✅ Update Student
@app.route("/update-student/<int:id>", methods=["PUT"])
def update_student(id):
    student = Student.query.get(id)

    if not student:
        return jsonify({"error": "Student not found"}), 404

    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    # Update only provided fields
    if "name" in data:
        student.name = data["name"]
    if "email" in data:
        student.email = data["email"]
    if "course" in data:
        student.course = data["course"]

    db.session.commit()

    return jsonify({"message": "Student updated successfully"})

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)