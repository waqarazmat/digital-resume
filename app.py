from pathlib import Path
import streamlit as st
from PIL import Image

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Waqar_Azmat_CV.pdf"
profile_pic = current_dir / "assets" / "profilep.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Waqar Azmat"
PAGE_ICON = ":wave:"
NAME = "Waqar Azmat"
DESCRIPTION = """
Passionate data enthusiast and learner with a solid background in machine learning. 
Dedicated to leveraging technology to drive positive social impact. Skilled in Python programming, 
with hands-on experience in developing AI solutions and conducting data-driven research.
"""
EMAIL = "waqar.azmat@student.uhasselt.be"
SOCIAL_MEDIA = {
    "LinkedIn": "https://linkedin.com/in/waqarazmat",
}
PROJECTS = {
    "Alfred AI’s Clothing Extension": "https://tensorlabs.io/projects.php?slug=alfred_ai",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- HERO SECTION ---
st.image(profile_pic, width=230)
st.title(NAME)
st.write(DESCRIPTION)
st.download_button(
    label=" 📄 Download Resume",
    data=PDFbyte,
    file_name=resume_file.name,
    mime="application/octet-stream",
)
st.write("📫", EMAIL)

# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

st.write("🚧", "**Machine Learning Engineer | Tensor Labs**")
st.write("January 2023 - September 2023 | Islamabad, Pakistan")
st.write(
    """
- Developed and deployed machine learning initiatives, optimizing algorithms for enhanced performance.
- Collaborated with senior team members to analyze data sets and derive actionable insights for decision-making processes.
- Spearheaded the extraction and analysis of datasets crucial for the development of innovative solutions.
- Contributed to testing and validation procedures, ensuring the accuracy and reliability of machine learning models.
"""
)

# --- PROJECTS ---
st.write('\n')
st.subheader("Relevant Projects")
st.write("---")
st.write("🚀", "**Data Science Project Contributor | Alfred AI’s Clothing Extension | Tensor Labs**")
st.write(
    """
- Led the extraction of datasets and selection of relevant body characteristics for precise size recommendations.
- Implemented robust technical processes and user-centric features, enhancing the fashion recommendation extension.
- Utilized regression modeling techniques to provide tailored size recommendations, addressing diversity in body shapes.
"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write("🎓", "**Masters of Management - Data Science | Uhasselt**")
st.write("Expected Graduation: 2025 | Hasselt, Belgium")
st.write("🎓", "**Bachelor of Business Administration | FAST - National University of Computer and Emerging Sciences**")
st.write("2015 - 2019 | Islamabad, Pakistan")

# --- PROFESSIONAL SKILLS ---
st.write('\n')
st.subheader("Professional Skills")
st.write(
    """
- Problem Solving
- Team Collaboration
- Leadership
"""
)

# --- TECHNICAL SKILLS ---
st.write('\n')
st.subheader("Technical Skills")
st.write(
    """
- Python (Data Analysis, Machine Learning)
- Spreadsheets (Microsoft Excel, Google Sheets)
- SAP (Signavio)
- Statistical Analysis (IBM SPSS Statistics)
"""
)

# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write(
    """
- Machine Learning A-Z™: Python & R in Data Science - Udemy
- Python for Machine Learning & Data Science Masterclass - Udemy
"""
)

# --- SOCIAL INITIATIVE ---
st.write('\n')
st.subheader("Social Initiative")
st.write("---")
st.write("🌍", "**Founder | The Path**")
st.write("August 2021 - Present | Pakistan")
st.write(
    """
- Established a national educational initiative leveraging technology to provide quality education to underserved students.
- Developed strategic partnerships to scale the impact of the campaign and reach remote communities effectively.
"""
)
