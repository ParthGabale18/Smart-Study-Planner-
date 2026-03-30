# Smart-Study-Planner-
AI-based Smart Study Planner that generates optimized study schedules using greedy algorithms and heuristic-based time allocation.

🎓 Smart Study Planner (AI-Based)

📌 Introduction

Managing study time effectively is a common problem among students. Many students struggle to decide which subject to prioritize and how much time to allocate, especially when exams are near.

This project presents a Smart Study Planner, an AI-based web application that generates an optimized study schedule using simple yet effective AI techniques.

🚀 Features

📚 Add subjects with difficulty level and exam date

⏳ Input daily available study hours

🧠 AI-based schedule generation

📅 7-day study plan

📊 Graph visualization of study hours

🧾 Download schedule as PDF

🌙 Dark/Light mode toggle

💡 AI explanation for schedule decisions

🧠 Concepts Used

Greedy Algorithm – prioritizes important subjects first

Heuristic Function – calculates subject importance

Priority-Based Scheduling

Proportional Time Allocation

⚙️ How It Works

Step 1: Input

User provides:

Subject name
Difficulty level (1–5)
Exam date
Daily study hours
Step 2: Priority Calculation

Priority = (Difficulty × 0.7) + (Urgency × 0.3)
Urgency = 1 / Days Left

Step 3: Time Allocation

Allocated Time = (Subject Priority / Total Priority) × Daily Hours

Step 4: Schedule Generation
A 7-day schedule is created
Slight variation is added for realism
Each decision includes an explanation

🛠 Tech Stack

Frontend:

HTML
CSS
JavaScript

Backend:

Python (Flask)

Libraries Used:

Chart.js (for graphs)
jsPDF (for PDF download)
Flask-CORS

📂 Project Structure

smart-study-planner/

│

├── frontend/

│ ├── index.html 

│
├── backend/

│ └── app.py 

│
├──Report.pdf

│── Algorithm.pdf 

│

├── README.md 

⚡️ Installation & Setup
Clone the Repository

git clone <your-repo-link>
cd smart-study-planner

Install Dependencies

pip install flask flask-cors

Run Backend

cd backend
python app.py

Run Frontend

Open: frontend/index.html

📊 Example Output

Math → 3.2 hrs

Physics → 1.8 hrs

Chemistry → 1.0 hr

⚠️ Challenges Faced

Designing an effective heuristic function

Handling frontend-backend communication

Fixing CORS issues

Making schedule realistic

📈 Future Improvements

User login & data storage

Mobile application

Calendar integration

Machine learning-based personalization

👨‍💻 Author

Parth Gabale 
