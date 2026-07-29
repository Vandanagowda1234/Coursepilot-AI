import streamlit as st

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CoursePilot AI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- LOAD CSS ---------------- #

def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- HERO SECTION ---------------- #

st.markdown("""
<div class="hero">

<h1>🎓 CoursePilot AI</h1>

<p>
AI Powered Course Recommendation System
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FEATURE CARDS ---------------- #

col1,col2,col3,col4=st.columns(4)

with col1:
    st.markdown("""
    <div class="card">
    <h2>📚 1000+</h2>
    <p>Courses</p>
    </div>
    """,unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <h2>🎯 50+</h2>
    <p>Career Paths</p>
    </div>
    """,unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <h2>🤖 AI</h2>
    <p>Recommendation Engine</p>
    </div>
    """,unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="card">
    <h2>⚡ Fast</h2>
    <p>Personalized Learning</p>
    </div>
    """,unsafe_allow_html=True)

st.markdown("<br><br>",unsafe_allow_html=True)

# ---------------- GET STARTED ---------------- #

st.markdown("""
<h2 style="text-align:center;color:white;">
Start Your Learning Journey
</h2>
""",unsafe_allow_html=True)

if st.button("🚀 Get Started", use_container_width=True):
    st.switch_page("pages/Recommendation.py")