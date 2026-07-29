
import streamlit as st
import json

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="CoursePilot AI",
    page_icon="🎓",
    layout="wide"
)

st.markdown("""
<style>

.stApp{
background:linear-gradient(to right,#e3f2fd,#ffffff);
}

h1{
color:#0D47A1;
font-weight:bold;
}

.stButton>button{
background:#1565C0;
color:white;
border-radius:12px;
height:50px;
font-size:18px;
font-weight:bold;
}

div[data-testid="stMetric"]{
background:#F5F9FF;
padding:15px;
border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD COURSES ---------------- #

with open("courses.json", "r") as f:
    courses = json.load(f)

# ---------------- HEADER ---------------- #

st.title("🎓 CoursePilot AI")
st.subheader("AI Powered Personalized Course Recommendation")

st.markdown("---")

# ---------------- FORM ---------------- #

with st.form("student_form"):

    col1, col2 = st.columns(2)

    with col1:

        name = st.text_input("👤 Full Name")

        email = st.text_input("📧 Email")

        qualification = st.selectbox(
            "🎓 Qualification",
            [
                "High School",
                "Diploma",
                "B.E/B.Tech",
                "BCA",
                "B.Sc",
                "MCA",
                "MBA"
            ]
        )

        experience = st.selectbox(
            "💼 Experience",
            [
                "Student",
                "Fresher",
                "Internship",
                "1-2 Years",
                "3-5 Years",
                "5+ Years"
            ]
        )

    with col2:

        career_goal = st.selectbox(
            "🎯 Career Goal",
            [
                "AI Engineer",
                "Data Scientist",
                "Cyber Security",
                "Full Stack Developer",
                "Cloud Engineer"
            ]
        )

        learning_style = st.selectbox(
            "📖 Preferred Learning Style",
            [
                "Video",
                "Projects",
                "Reading",
                "Mixed"
            ]
        )

        skills = st.multiselect(
            "💻 Current Skills",
            [
                "Python",
                "Java",
                "SQL",
                "HTML",
                "CSS",
                "JavaScript",
                "Git",
                "Linux",
                "Statistics",
                "Machine Learning",
                "Other"
            ]
        )
        

    submitted = st.form_submit_button(
        "🚀 Generate Recommendation",
        use_container_width=True
    )

# ==================================================
# RECOMMENDATION ENGINE
# ==================================================

if submitted:

    recommended = []
    missing = []

    for course in courses:

        if career_goal in course["career"]:

            if all(skill in skills for skill in course["prerequisites"]):

                recommended.append(course)

            else:

                for skill in course["prerequisites"]:

                    if skill not in skills and skill not in missing:

                        missing.append(skill)

    st.success("✅ Recommendation Generated Successfully!")

    st.title("🎓 Personalized Learning Report")

    st.markdown("---")
    # ==================================================
# STUDENT PROFILE
# ==================================================

    st.header("👤 Student Profile")

    c1, c2 = st.columns(2)

    with c1:
        st.write(f"**Name:** {name}")
        st.write(f"**Email:** {email}")
        st.write(f"**Qualification:** {qualification}")

    with c2:
        st.write(f"**Career Goal:** {career_goal}")
        st.write(f"**Experience:** {experience}")
        st.write(f"**Learning Style:** {learning_style}")

    st.divider()

# ==================================================
# CAREER READINESS SCORE
# ==================================================

    score = 100

    score -= len(missing) * 12

    if score < 40:
        score = 40

    st.header("📊 Career Readiness Score")

    st.progress(score / 100)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Overall Score", f"{score}%")

    with col2:
        st.metric("Skills", len(skills))

    with col3:
        st.metric("Missing Skills", len(missing))

    st.divider()

# ==================================================
# CURRENT SKILLS
# ==================================================

    st.header("💻 Current Skills")

    if skills:

        cols = st.columns(4)

        for i, skill in enumerate(skills):

            cols[i % 4].success(skill)

    else:

        st.warning("No skills selected.")

    st.divider()

# ==================================================
# SKILL GAP
# ==================================================

    st.header("📉 Skill Gap Analysis")

    if missing:

        st.warning(
            "The following skills are recommended before taking advanced courses."
        )

        for skill in missing:

            st.markdown(f"❌ **{skill}**")

    else:

        st.success("🎉 No Skill Gap Found")

    st.divider()

# ==================================================
# AI PROFILE ANALYSIS
# ==================================================

    st.header("🧠 AI Profile Analysis")

    analysis = f"""
You want to become a **{career_goal}**.

Based on your current profile, you already possess
**{len(skills)} technical skills**.

To become industry-ready, complete the recommended
courses in order and strengthen the missing
prerequisite skills.

Since your preferred learning style is
**{learning_style}**, practical project-based learning
is highly recommended.

Completing this roadmap will significantly improve
your internship and placement opportunities.
"""

    st.info(analysis)

    st.divider()
    # ==================================================
# RECOMMENDED COURSES
# ==================================================

    st.header("🎯 Recommended Courses")

    total_weeks = 0

    if recommended:

        for i, course in enumerate(recommended):

            weeks = int(course["duration"].split()[0])
            total_weeks += weeks

            with st.expander(f"📚 {i+1}. {course['name']}", expanded=True):

                st.write("⭐⭐⭐⭐⭐")

                st.write(f"**Duration:** {course['duration']}")

                st.write(f"**Why Recommended?**")

                st.success(course["reason"])

                st.write("""
After completing this course, build one
mini project before moving to the next course.

This improves your portfolio and interview skills.
""")

    else:

        st.warning("No direct recommendations found.")

    st.divider()

# ==================================================
# LEARNING ROADMAP
# ==================================================

    st.header("🗺 Personalized Learning Roadmap")

    for i, course in enumerate(recommended, start=1):

        st.markdown(f"""
### ✅ Step {i}

**{course['name']}**

⏱ Duration : {course['duration']}

⬇
""")

    st.success("🛠 Build Portfolio Projects")

    st.success("💼 Apply for Internships")

    st.success("🚀 Start Applying for Jobs")

    st.divider()

# ==================================================
# SUGGESTED PROJECTS
# ==================================================

    st.header("🛠 Suggested Projects")

    project_map = {

        "AI Engineer":[
            "House Price Prediction",
            "Resume Screening AI",
            "Face Recognition",
            "Fake News Detection",
            "Chatbot using Python"
        ],

        "Data Scientist":[
            "Sales Prediction",
            "Stock Prediction",
            "Customer Segmentation",
            "Movie Recommendation"
        ],

        "Cyber Security":[
            "Password Strength Checker",
            "Port Scanner",
            "Network Scanner",
            "Malware Detection"
        ],

        "Full Stack Developer":[
            "Hospital Management",
            "Food Ordering Website",
            "Portfolio Website",
            "E-Commerce Website"
        ],

        "Cloud Engineer":[
            "AWS Deployment",
            "Docker Project",
            "CI/CD Pipeline",
            "Kubernetes Demo"
        ]

    }

    for project in project_map.get(career_goal, []):

        st.success(project)

    st.divider()

# ==================================================
# FREE LEARNING RESOURCES
# ==================================================

    st.header("📚 Free Learning Resources")

    resources = [
        "Coursera",
        "freeCodeCamp",
        "Google AI",
        "Microsoft Learn",
        "YouTube",
        "Udemy",
        "edX",
        "Kaggle Learn"
    ]

    cols = st.columns(2)

    for i, resource in enumerate(resources):

        cols[i % 2].info(resource)

    st.divider()

# ==================================================
# ESTIMATED LEARNING TIME
# ==================================================

    st.header("⏳ Estimated Learning Duration")

    st.metric(
        "Total Duration",
        f"{total_weeks} Weeks"
    )

    st.metric(
        "Approximate Completion",
        f"{round(total_weeks/4,1)} Months"
    )

    st.divider()
    # ==================================================
# TOP HIRING COMPANIES
# ==================================================

    st.header("🏢 Top Hiring Companies")

    companies = {

        "AI Engineer":[
            "Google",
            "Microsoft",
            "Amazon",
            "OpenAI",
            "NVIDIA",
            "IBM",
            "Infosys",
            "Accenture"
        ],

        "Data Scientist":[
            "Amazon",
            "Flipkart",
            "Google",
            "IBM",
            "Deloitte",
            "EY",
            "TCS",
            "Wipro"
        ],

        "Cyber Security":[
            "Cisco",
            "Palo Alto Networks",
            "IBM Security",
            "Deloitte",
            "EY",
            "TCS",
            "Accenture",
            "Infosys"
        ],

        "Full Stack Developer":[
            "Google",
            "Microsoft",
            "Amazon",
            "Zoho",
            "Freshworks",
            "TCS",
            "Infosys",
            "Capgemini"
        ],

        "Cloud Engineer":[
            "AWS",
            "Microsoft Azure",
            "Google Cloud",
            "Oracle",
            "IBM Cloud",
            "Accenture",
            "Infosys",
            "TCS"
        ]

    }

    cols = st.columns(4)

    for i, company in enumerate(companies.get(career_goal, [])):
        cols[i % 4].success(company)

    st.divider()

# ==================================================
# EXPECTED SALARY
# ==================================================

    st.header("💰 Expected Salary")

    salary = {

        "AI Engineer":"₹6 LPA - ₹15 LPA",

        "Data Scientist":"₹5 LPA - ₹12 LPA",

        "Cyber Security":"₹5 LPA - ₹10 LPA",

        "Full Stack Developer":"₹4 LPA - ₹9 LPA",

        "Cloud Engineer":"₹6 LPA - ₹14 LPA"

    }

    st.metric(
        "Average Fresher Salary",
        salary.get(career_goal)
    )

    st.divider()

# ==================================================
# CAREER OPPORTUNITIES
# ==================================================

    st.header("💼 Career Opportunities")

    opportunities = {

        "AI Engineer":[
            "Machine Learning Engineer",
            "Deep Learning Engineer",
            "NLP Engineer",
            "Computer Vision Engineer",
            "AI Research Intern"
        ],

        "Data Scientist":[
            "Data Scientist",
            "Business Analyst",
            "ML Engineer",
            "Data Analyst"
        ],

        "Cyber Security":[
            "SOC Analyst",
            "Penetration Tester",
            "Ethical Hacker",
            "Security Analyst"
        ],

        "Full Stack Developer":[
            "Frontend Developer",
            "Backend Developer",
            "Software Engineer",
            "Web Developer"
        ],

        "Cloud Engineer":[
            "AWS Engineer",
            "Azure Engineer",
            "DevOps Engineer",
            "Cloud Architect"
        ]

    }

    for job in opportunities.get(career_goal, []):
        st.write("💼", job)

    st.divider()

# ==================================================
# AI CAREER ADVICE
# ==================================================

    st.header("🤖 AI Career Advice")

    st.success(f"""
Congratulations **{name}**!

Based on your profile, our AI recommends
focusing on **{career_goal}**.

### Next Steps

✅ Complete all recommended courses.

✅ Learn missing prerequisite skills.

✅ Build at least 3 portfolio projects.

✅ Upload projects to GitHub.

✅ Participate in Hackathons.

✅ Earn Industry Certifications.

✅ Practice Coding Daily.

✅ Apply for Internships.

Following this roadmap can significantly improve
your placement opportunities.
""")

    st.divider()

# ==================================================
# FINAL SUMMARY
# ==================================================

    st.header("📋 Recommendation Summary")

    st.info(f"""
👤 Student : {name}

🎯 Career Goal : {career_goal}

📊 Readiness Score : {score}%

📚 Recommended Courses : {len(recommended)}

❌ Missing Skills : {len(missing)}

⏳ Estimated Duration : {round(total_weeks/4,1)} Months

💰 Expected Salary : {salary.get(career_goal)}
""")

    st.download_button(
        label="📄 Download Recommendation Report",
        data=f"""
CoursePilot AI Report

Student : {name}

Career Goal : {career_goal}

Qualification : {qualification}

Skills : {', '.join(skills)}

Missing Skills : {', '.join(missing)}

Recommended Courses :

{chr(10).join([c['name'] for c in recommended])}
""",
        file_name="CoursePilot_Report.txt"
    )

    st.balloons()

    st.success("🎉 Thank you for using CoursePilot AI!")
