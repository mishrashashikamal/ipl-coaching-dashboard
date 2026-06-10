# 🏏 IPL Player Coaching Intelligence Dashboard

A data-driven coaching tool that analyzes IPL batsman performance to help coaches and players identify weaknesses, strengths and generate AI-powered coaching reports!

## 🚀 Live App
👉 **[Click here to use the app](https://mishrashashikamal-ipl-coaching-dashboard-app-6hwbkh.streamlit.app/)**

---

## 📊 What the Dashboard Shows

- 📈 **Phase-wise Strike Rate** — Powerplay vs Middle vs Death overs
- 🎯 **Runs Distribution** — How often player scores 0, 1, 2, 4, 6
- 🎳 **Pace vs Spin Analysis** — Which bowling type troubles the player most
- 📉 **Over-wise Dismissals** — Which overs the player gets out most
- 🔥 **Weakness Heatmap** — Visual map of scoring patterns across all overs
- 📅 **Season-wise Evolution** — How the player evolved over the years
- 🏟️ **Venue Analysis** — Best and worst performing grounds
- 🤖 **AI Coaching Report** — Gemini AI generates personalized coaching report with practice drill suggestions!

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=for-the-badge&logo=python&logoColor=white)
![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%20AI-4285F4?style=for-the-badge&logo=google&logoColor=white)

---

## 📁 Dataset
IPL Ball-by-Ball data 2008-2024 from Kaggle (260,920 deliveries!)

---

## 🗂️ Project Structure

```
ipl-coaching-dashboard/
│
├── 01_data_exploration.ipynb    # Data analysis & visualization
├── 02_ai_coaching_report.ipynb  # Gemini API coaching report
├── app.py                       # Streamlit web application
├── requirements.txt             # Python dependencies
├── deliveries.csv               # Ball-by-ball IPL data
└── matches.csv                  # Match details
```

---

## ⚙️ How to Run Locally

```bash
# Clone the repo
git clone https://github.com/mishrashashikamal/ipl-coaching-dashboard.git

# Install dependencies
pip install -r requirements.txt

# Add your Gemini API key in .env file
GEMINI_API_KEY=your_key_here

# Run the app
streamlit run app.py
```

---

## 🎯 Key Insights Found (MS Dhoni)

- ⚡ Death overs SR: **168** — absolute finisher!
- 🎳 **79.87%** dismissals against pace bowling
- 🏟️ Best venue: Mohali (SR 179) | Worst: Delhi (SR 83)
- 💥 **136 sixes** in death overs alone!

---

## 👨‍💻 Built By

**Shashi Kamal Mishra**
B.Tech CSE (Data Science) | Bennett University

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shashi-kamal-mishra-05609228b/)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/mishrashashikamal)
[![LeetCode](https://img.shields.io/badge/LeetCode-Profile-FFA116?style=for-the-badge&logo=leetcode&logoColor=black)](https://leetcode.com/u/shashi_kamal_mishra/)

---

## ✅ Status
**LIVE** — Deployed on Streamlit Cloud 🚀
