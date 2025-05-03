import streamlit as st
from PIL import Image

# ------------ CONFIG ------------
st.set_page_config(page_title="Saidul Islam | Portfolio", page_icon="💼", layout="centered")

# ------------ HEADER ------------
st.title("👨‍💻 Saidul Islam")
st.write("### Data Analyst | ML/AI Learner | Developer | AI Agent")
st.markdown("💡 Passionate about building data-driven solutions and learning cutting-edge technologies.")

# ------------ IMAGE (optional) ------------
img = Image.open("saidul.png")  # Replace with your image file
st.image(img, width=180)

# ------------ ABOUT ------------
st.subheader("📘 About Me")
st.write("""
I'm a university student and aspiring **data analyst** with experience in:
- Python, pandas, matplotlib, seaborn
- Streamlit, Power BI, Looker Studio
- Basic ML with scikit-learn
- Django, SQL

Actively working on real-world projects and open to collaborations!
""")

# ------------ SKILLS ------------
st.subheader("🛠️ Skills")
st.write("""
- **Languages**: Python, C++, SQL
- **Libraries**: pandas, numpy, scikit-learn, seaborn, plotly
- **Tools**: Power BI, Looker Studio, Git, Jupyter, Streamlit
- **Web**: Django (basic), HTML/CSS (basic)
""")

# ------------ PROJECTS ------------
st.subheader("📂 Projects")

st.markdown("""
🔹 [**Streamlit Productivity Dashboard**](https://github.com/your-username/streamlit-productivity-dashboard)  
_A personal dashboard with to-do list, learning tracker, motivational quotes, and video._

🔹 [**Hospital Management System (C++)**](https://github.com/your-username/hospital-management-cpp)  
_A terminal-based system for managing patients and doctor appointments._

🔹 [**US Accidents Analysis**](https://github.com/your-username/us-accidents-analysis)  
_EDA on US traffic accident data using Python and visualizations._

🔹 [**Virtual Study Buddy (Django)**](https://github.com/your-username/virtual-study-buddy)  
_A Django web app for students to store materials, track goals, and manage tasks._
""")

# ------------ CERTIFICATES ------------
st.subheader("📜 Certificates")

st.markdown("""
- **Django Web Framework** – Meta via Coursera  
- **Applied Data Science Lab** – WorldQuant University  
- **Data Analytics with Python** – Prodigy Infotech Internship  
- **Quantum Computing Basics** – QWorld
""")

# ------------ RESUME DOWNLOAD (Optional) ------------
with open("Saidul_Islam_Data_Analyst_CV.pdf", "rb") as file:
    btn = st.download_button(
        label="📄 Download My Resume",
        data=file,
        file_name="Saidul_Islam_Data_Analyst_CV.pdf",
        mime="application/pdf"
    )

# ------------ CONTACT INFO ------------
st.subheader("📫 Contact Me")
st.markdown("""
- 📧 Email: [23303345@iubat.edu](mailto:23303345@iubat.edu)
- 🌐 GitHub: [@saidulislam2003](https://github.com/saidulislam2003)
- 💼 LinkedIn: [Saidul Islam](https://www.linkedin.com/in/saidulislam2003)
""")

st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

