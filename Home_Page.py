import streamlit as st

st.set_page_config(page_title="Home", layout="centered")

st.title("Hey there! Welcome to my site")
st.subheader("I'm Fatih Özel – CS 1301 @ Georgia Tech")

st.markdown("---")

st.header("What's on this site?")

st.markdown("""
1. **My Portfolio**:  
A snapshot of my journey so far — from neuroscience and coding to swim coaching and EMS. This page highlights my background, classes, projects, and real-world experience.

2. **Swim Progress Tracker**:  
A page where you can explore swimmer performance data and see how athletes improve across different events. Includes interactive charts and progress stats.
""")

st.markdown("---")
st.write("Use the sidebar to navigate between pages. Thanks for stopping by!")
