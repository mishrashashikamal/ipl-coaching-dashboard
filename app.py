# ============================================
# IPL PLAYER COACHING INTELLIGENCE DASHBOARD
# ============================================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dotenv import load_dotenv
import os
import google.generativeai as genai

# Load API key
load_dotenv(dotenv_path=r"C:\Users\Shashi Kamal Mishra\OneDrive\Documents\ipl-coaching-dashboard\.env")
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash")

# ============================================
# PAGE CONFIG
# ============================================
st.set_page_config(
    page_title="IPL Coaching Dashboard",
    page_icon="🏏",
    layout="wide"
)

# ============================================
# LOAD DATA
# ============================================
@st.cache_data
def load_data():
    deliveries = pd.read_csv('deliveries.csv')
    matches = pd.read_csv('matches.csv')
    return deliveries, matches

deliveries, matches = load_data()

# ============================================
# HEADER
# ============================================
st.title("🏏 IPL Player Coaching Intelligence Dashboard")
st.markdown("*Data-driven insights to help coaches and players improve performance*")
st.divider()

# ============================================
# PLAYER SELECTOR
# ============================================
all_batsmen = sorted(deliveries['batter'].unique())
player = st.selectbox("🔍 Select a Player", all_batsmen)

# Filter player data
player_data = deliveries[deliveries['batter'] == player].copy()

st.subheader(f"📊 Analysis for {player}")

# ============================================
# BASIC STATS ROW
# ============================================
total_balls = len(player_data)
total_runs = player_data['batsman_runs'].sum()
dismissals = player_data['is_wicket'].sum()
strike_rate = round((total_runs / total_balls) * 100, 2)
dot_pct = round((len(player_data[player_data['batsman_runs'] == 0]) / total_balls) * 100, 2)

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("🏏 Balls Faced", total_balls)
col2.metric("🎯 Runs Scored", total_runs)
col3.metric("❌ Dismissals", int(dismissals))
col4.metric("⚡ Strike Rate", strike_rate)
col5.metric("🔴 Dot Ball %", f"{dot_pct}%")

st.divider()

# ============================================
# ROW 1 — PHASE WISE + RUNS DISTRIBUTION
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Phase-wise Strike Rate")
    def get_phase(over):
        if over <= 5:
            return 'Powerplay'
        elif over <= 14:
            return 'Middle'
        else:
            return 'Death'

    player_data['phase'] = player_data['over'].apply(get_phase)
    phase_stats = player_data.groupby('phase').agg(
        balls=('batsman_runs', 'count'),
        runs=('batsman_runs', 'sum'),
    ).reset_index()
    phase_stats['strike_rate'] = (phase_stats['runs'] / phase_stats['balls'] * 100).round(2)

    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['#2ecc71', '#f39c12', '#e74c3c']
    bars = ax.bar(phase_stats['phase'], phase_stats['strike_rate'], color=colors)
    for bar, val in zip(bars, phase_stats['strike_rate']):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + 1, str(val), ha='center', fontweight='bold')
    ax.set_title(f'{player} — SR by Phase')
    ax.set_ylabel('Strike Rate')
    st.pyplot(fig)

with col2:
    st.subheader("🎯 Runs Distribution")
    runs_dist = player_data['batsman_runs'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    colors = ['#95a5a6','#3498db','#2ecc71','#f1c40f','#e67e22','#e74c3c']
    ax.bar(runs_dist.index, runs_dist.values, color=colors[:len(runs_dist)], edgecolor='white')
    ax.set_title(f'{player} — Runs Per Ball')
    ax.set_xlabel('Runs')
    ax.set_ylabel('Count')
    st.pyplot(fig)

st.divider()

# ============================================
# ROW 2 — PACE VS SPIN + OVER DISMISSALS
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎳 Pace vs Spin Dismissals")
    dismissals_only = player_data[player_data['is_wicket'] == 1]
    spin_bowlers = [
        'PP Ojha', 'CV Varun', 'YS Chahal', 'R Ashwin', 'Imran Tahir',
        'A Mishra', 'Harbhajan Singh', 'P Chawla', 'SR Watson',
        'RA Jadeja', 'SP Narine', 'Rashid Khan', 'Kuldeep Yadav'
    ]
    dismissals_only = dismissals_only.copy()
    dismissals_only['bowler_type'] = dismissals_only['bowler'].apply(
        lambda x: 'Spin' if x in spin_bowlers else 'Pace'
    )
    bowler_type_counts = dismissals_only['bowler_type'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(bowler_type_counts.values,
           labels=bowler_type_counts.index,
           colors=['#e74c3c', '#3498db'],
           autopct='%1.1f%%',
           explode=(0.05, 0.05))
    ax.set_title(f'{player} — Pace vs Spin')
    st.pyplot(fig)

with col2:
    st.subheader("📉 Over-wise Dismissals")
    over_dismissals = dismissals_only['over'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(over_dismissals.index, over_dismissals.values, color='#e74c3c')
    ax.set_title(f'{player} — Dismissals per Over')
    ax.set_xlabel('Over')
    ax.set_ylabel('Dismissals')
    st.pyplot(fig)

st.divider()

# ============================================
# ROW 3 — HEATMAP
# ============================================
st.subheader("🔥 Weakness Heatmap — Runs per Over")
heatmap_data = player_data.pivot_table(
    values='ball',
    index='over',
    columns='batsman_runs',
    aggfunc='count',
    fill_value=0
)
fig, ax = plt.subplots(figsize=(12, 6))
sns.heatmap(heatmap_data, cmap='YlOrRd', annot=True,
            fmt='d', linewidths=0.5, ax=ax)
ax.set_title(f'{player} — Runs Scored Per Over Heatmap')
st.pyplot(fig)

st.divider()

# ============================================
# ROW 4 — SEASON WISE + VENUE
# ============================================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📅 Season-wise Evolution")
    merged = deliveries.merge(
        matches[['id', 'season', 'venue']],
        left_on='match_id', right_on='id', how='left'
    )
    player_merged = merged[merged['batter'] == player]
    season_stats = player_merged.groupby('season').agg(
        balls=('batsman_runs', 'count'),
        runs=('batsman_runs', 'sum'),
    ).reset_index()
    season_stats['strike_rate'] = (season_stats['runs'] / season_stats['balls'] * 100).round(2)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(season_stats['season'], season_stats['strike_rate'],
            marker='o', color='#e74c3c', linewidth=2)
    ax.set_title(f'{player} — Season-wise SR')
    ax.set_ylabel('Strike Rate')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("🏟️ Venue Analysis")
    venue_stats = player_merged.groupby('venue').agg(
        balls=('batsman_runs', 'count'),
        runs=('batsman_runs', 'sum'),
    ).reset_index()
    venue_stats['strike_rate'] = (venue_stats['runs'] / venue_stats['balls'] * 100).round(2)
    venue_stats = venue_stats[venue_stats['balls'] >= 30]
    venue_stats = venue_stats.sort_values('strike_rate', ascending=False)
    top5 = venue_stats.head(5)
    bottom5 = venue_stats.tail(5)
    combined = pd.concat([top5, bottom5])
    combined['venue_short'] = combined['venue'].str[:20]
    colors = ['#2ecc71'] * 5 + ['#e74c3c'] * 5
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(combined['venue_short'], combined['strike_rate'], color=colors)
    ax.set_title(f'{player} — Best & Worst Venues')
    ax.set_xlabel('Strike Rate')
    st.pyplot(fig)

st.divider()

# ============================================
# AI COACHING REPORT
# ============================================
st.subheader("🤖 AI Coaching Report")
st.markdown("*Click the button to generate a personalized AI coaching report!*")

if st.button("🤖 Generate AI Coaching Report"):
    with st.spinner("Generating report... please wait 🤖"):
        prompt = f"""
        You are an expert IPL cricket coach. Based on this data for {player}:
        - Total Balls: {total_balls}, Runs: {total_runs}
        - Strike Rate: {strike_rate}, Dot Ball %: {dot_pct}%
        - Phase SR: {phase_stats.to_string()}

        Provide a professional coaching report with:
        1. Overall assessment (3-4 lines)
        2. Key strengths (3 points)
        3. Key weaknesses (3 points)
        4. Practice drills (4 drills)
        5. Match strategy (3 points)
        """
        response = model.generate_content(prompt)
        st.markdown(response.text)