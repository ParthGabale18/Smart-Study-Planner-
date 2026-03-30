from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import random

app = Flask(__name__)
CORS(app)

def calculate_priority(difficulty, days_left):
    return (difficulty * 0.7) + (1 / days_left * 0.3)

@app.route("/")
def home():
    return "Backend running"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    subjects = data["subjects"]
    hours = data["hours"]

    today = datetime.today()
    schedule = {}

    for s in subjects:
        days = max((datetime.strptime(s["exam_date"], "%Y-%m-%d") - today).days, 1)
        s["priority"] = calculate_priority(s["difficulty"], days)
        s["days"] = days

    for d in range(7):
        date = (today + timedelta(days=d)).strftime("%Y-%m-%d")
        schedule[date] = []

        total = sum(s["priority"] for s in subjects)

        for s in subjects:
            h = (s["priority"]/total)*hours*random.uniform(0.9,1.1)
            h = round(h,1)

            reason = "Exam near" if s["days"]<3 else "High difficulty" if s["difficulty"]>=4 else "Balanced"

            schedule[date].append({
                "subject": s["name"],
                "hours": h,
                "reason": reason
            })

    return jsonify(schedule)

if __name__ == "__main__":
    app.run(debug=True)