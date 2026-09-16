from flask import Flask, render_template, request, redirect

app = Flask(__name__)


# ==========================================
# STUDENT DATA
# No SQL / No Database
# ==========================================

students = [
    {
        "id": 1,
        "name": "Abjanur Sekh",
        "age": 20,
        "gender": "Male",
        "course": "BCA",
        "phone": "9876543210"
    },
    {
        "id": 2,
        "name": "Sajahan Ali",
        "age": 19,
        "gender": "Male",
        "course": "BCA",
        "phone": "9876543211"
    },
    {
        "id": 3,
        "name": "Roni Paul",
        "age": 21,
        "gender": "Male",
        "course": "BCA",
        "phone": "9876543212"
    },
    {
        "id": 4,
        "name": "Sneha Das",
        "age": 20,
        "gender": "Female",
        "course": "B.Tech IT",
        "phone": "9876543213"
    },
    {
        "id": 5,
        "name": "Emran Mandal",
        "age": 22,
        "gender": "Male",
        "course": "B.Tech IT",
        "phone": "9876543214"
    },
    {
        "id": 6,
        "name": "Pooja Patel",
        "age": 19,
        "gender": "Female",
        "course": "BBA",
        "phone": "9876543215"
    },
    {
        "id": 7,
        "name": "Manan Ali",
        "age": 20,
        "gender": "Male",
        "course": "MCA",
        "phone": "9876543216"
    },
    {
        "id": 8,
        "name": "Tosif Raja",
        "age": 21,
        "gender": "Male",
        "course": "MBA",
        "phone": "9876543217"
    },
    {
        "id": 9,
        "name": "Amit",
        "age": 22,
        "gender": "Male",
        "course": "MCA",
        "phone": "9876543218"
    },
    {
        "id": 10,
        "name": "Chummuk",
        "age": 20,
        "gender": "Female",
        "course": "B.Sc",
        "phone": "9876543219"
    }
]


# ==========================================
# HOME / VIEW STUDENTS
# ==========================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        students=students
    )


# ==========================================
# ADD STUDENT
# ==========================================

@app.route("/add", methods=["POST"])
def add_student():

    name = request.form.get("name")
    age = request.form.get("age")
    gender = request.form.get("gender")
    course = request.form.get("course")
    phone = request.form.get("phone")

    # Generate new ID
    if students:
        new_id = max(student["id"] for student in students) + 1
    else:
        new_id = 1

    new_student = {
        "id": new_id,
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "phone": phone
    }

    students.append(new_student)

    return redirect("/")


# ==========================================
# SEARCH STUDENT
# ==========================================

@app.route("/search")
def search_student():

    keyword = request.args.get("keyword", "").strip().lower()

    if keyword == "":
        return render_template(
            "index.html",
            students=students,
            keyword=""
        )

    search_results = []

    for student in students:

        if (
            keyword in student["name"].lower()
            or keyword in student["course"].lower()
            or keyword in student["phone"].lower()
        ):
            search_results.append(student)

    return render_template(
        "index.html",
        students=search_results,
        keyword=keyword
    )


# ==========================================
# UPDATE STUDENT
# ==========================================

@app.route("/update/<int:id>", methods=["GET", "POST"])
def update_student(id):

    student = None

    # Find student
    for item in students:

        if item["id"] == id:
            student = item
            break

    # Student not found
    if student is None:
        return redirect("/")

    # Update
    if request.method == "POST":

        student["name"] = request.form.get("name")
        student["age"] = request.form.get("age")
        student["gender"] = request.form.get("gender")
        student["course"] = request.form.get("course")
        student["phone"] = request.form.get("phone")

        return redirect("/")

    return render_template(
        "index.html",
        students=students,
        student=student
    )


# ==========================================
# DELETE STUDENT
# ==========================================

@app.route("/delete/<int:id>")
def delete_student(id):

    global students

    students = [
        student
        for student in students
        if student["id"] != id
    ]

    return redirect("/")


# ==========================================
# RUN FLASK
# ==========================================

if __name__ == "__main__":

    app.run(debug=True)