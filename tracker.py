import streamlit as st
import json
import os

# Define the learning plan structure
learning_plan = {
    "Level 1: Foundations of AI & ML": {
        "Understanding AI & ML": False,
        "Experimenting with AI APIs": False,
        "First AI Mini-Project": False
    },
    "Level 2: AI Application Development": {
        "Using AI APIs in Applications": False,
        "Building AI-Powered Learning Tools": False,
        "Vector Databases & AI Memory": False
    },
    "Level 3: Advanced AI Customization": {
        "Fine-Tuning AI Models": False,
        "Building Adaptive AI Systems": False,
        "Deploying Custom AI Applications": False
    },
    "Level 4: AI Engineering & Deployment": {
        "Running AI Models in Production": False,
        "Deploying AI to the Cloud": False,
        "Optimizing AI for Real-World Use": False
    }
}

# Load progress if available
progress_file = "ai_learning_progress.json"
if os.path.exists(progress_file):
    with open(progress_file, "r") as f:
        progress_data = json.load(f)
else:
    progress_data = learning_plan

# Streamlit UI
st.title("🚀 AI Learning Tracker")
st.subheader("Track your progress as you learn AI!")

# Display learning levels and progress checkboxes
for level, topics in progress_data.items():
    st.markdown(f"### {level}")
    for topic, completed in topics.items():
        checked = st.checkbox(topic, value=completed, key=f"{level}-{topic}")
        progress_data[level][topic] = checked

# Save progress when the user checks/unchecks items
with open(progress_file, "w") as f:
    json.dump(progress_data, f)

st.success("Progress saved!")

# Notes section
st.subheader("📝 Learning Notes & Reflections")
user_notes = st.text_area("Write down your thoughts, reflections, or questions here...")

# Display AI learning resources
st.subheader("📚 AI Learning Resources")
st.markdown("[AI for Everyone](https://www.coursera.org/learn/ai-for-everyone) - Intro to AI")
st.markdown("[Hugging Face Course](https://huggingface.co/course) - Learn AI model fine-tuning")
st.markdown("[Fast.ai Practical Deep Learning](https://course.fast.ai/) - Hands-on AI learning")

st.success("Your AI learning path is ready! 🚀")
