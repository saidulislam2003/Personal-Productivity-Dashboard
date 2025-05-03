import streamlit as st
import datetime
import random

# Title
st.title("📊 My Personal Productivity Dashboard")

# To-Do List
st.subheader("✅ Daily To-Do")
tasks = st.text_area("Write your tasks separated by commas", "Learn Python, Read a blog, Exercise")
task_list = [task.strip() for task in tasks.split(',') if task.strip()]
for task in task_list:
    st.checkbox(task)

# Progress Tracker
st.subheader("📈 Learning Tracker")
topics = ["Python", "Machine Learning", "SQL", "Web Dev"]
for topic in topics:
    st.slider(f"{topic} Progress", 0, 100)

# Motivational Quotes
st.subheader("💬 Quote of the Day")
quotes = [
    "Believe you can and you're halfway there.",
    "You are capable of amazing things.",
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn't come from what you do occasionally. It comes from what you do consistently.",
    "The most dangerous phrase in the language is, ‘We’ve always done it this way."
]
st.info(random.choice(quotes))

# YouTube Embed
st.subheader("📹 Motivational Video")
st.video("https://www.youtube.com/watch?v=dWQydgGBOEE")  # Feel free to change this link

# Date
st.sidebar.write("📅 Today is", datetime.date.today())
