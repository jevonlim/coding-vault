from flask import Flask, url_for, redirect, request, render_template
import json
from bson.objectid import ObjectId
import os
import pymongo


app = Flask(__name__)
MONGODB_URL = "mongodb+srv://jevonaugustianlim01_db_user:Lenny123@30daysofpython.mf4hdla.mongodb.net/?appName=30DaysOfPython"
client = pymongo.MongoClient(MONGODB_URL)
db = client['thirty_days_of_python']


@app.route("/students", methods = ["GET"])
def students_list():
    data = list(db.students.find())
    for item in data:
        item["_id"] = str(item["_id"])
    return render_template("student.html", students=data)


@app.route("/students/create", methods = ["GET", "POST"])
def create_student():
    if request.method == "POST":
        name = request.form["name"]
        country = request.form["country"]
        city = request.form["city"]
        age = int(request.form["age"])
        student = {
            "name": name,
            "country": country,
            "city": city,
            "age": age
        }
        db.students.insert_one(student)
        return redirect(url_for("students_list"))
    else:
        return render_template("create.html")

@app.route("/students/update/<id>", methods = ["GET" ,"POST"])
def update_student(id):
    if request.method == "POST":
        query = {"_id": ObjectId(id)}
        name = request.form["name"]
        country = request.form["country"]
        city = request.form["city"]
        age = int(request.form["age"])
        student = {
            "name": name,
            "country": country,
            "city": city,
            "age": age
        }
        db.students.update_one(query, {"$set": student})
        return redirect(url_for("students_list"))
    else:
        return render_template("update.html")

@app.route("/students/delete/<id>", methods=["POST"])
def delete_student(id):
    db.students.delete_one({"_id": ObjectId(id)})
    return redirect(url_for("students_list"))


if __name__ == "__main__":
    port  = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)