import streamlit as st
from pathlib import Path
import datetime
import os

# ------------------------------
# Page setup
# ------------------------------
st.set_page_config(
    page_title="Miguel A. Gonzalez Almonte — Dev Portfolio",
    page_icon="💡",
    layout="wide",
)

# ------------------------------
# Helpers
# ------------------------------
ASSETS_DIR = Path(os.getcwd()) / "static"
IMG_PATH = ASSETS_DIR / "fsh.png"   # profile image
RESUME_PATH = Path("data_ai1.pdf")  # resume pdf

def file_bytes_if_exists(path: Path):
    try:
        if path.exists():
            return path.read_bytes()
    except Exception:
        pass
    return None

def ext_link(label: str, url: str, icon: str = ""):
    icon_txt = f"{icon} " if icon else ""
    st.markdown(
        f"<a href='{url}' target='_blank' style='text-decoration:none'>"
        f"<span style='font-weight:600'>{icon_txt}{label}</span> ↗</a>",
        unsafe_allow_html=True,
    )

def read_md(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"❌ Missing: {path}"

# -----------------
# STATE + HANDLERS
# -----------------
if "section" not in st.session_state:
    st.session_state.section = "None"
if "section2" not in st.session_state:
    st.session_state.section2 = "None"

def handle_section():
    if st.session_state.section != "None":
        st.session_state.section2 = "None"

def handle_section2():
    if st.session_state.section2 != "None":
        st.session_state.section = "None"

# -----------------
# SIDEBAR SELECTORS
# -----------------
st.sidebar.selectbox(
    "Pick a Category",
    [
        "None",
        "🖥️ Dashboard",
        "🐍 Core Language",
        "📦 Standard Library",
        "📊 Data Science",
        "🤖 Automation & Scripting",
        "🎯 Advanced Python",
        "📚 Notes"
    ],
    key="section",
    on_change=handle_section,
)

st.sidebar.selectbox(
    "Pick a Book",
    [
        "None",
        "📘 Python Crash Course",
        "📖 Automate the Boring Stuff with Python",
    ],
    key="section2",
    on_change=handle_section2,
)

# ------------------------------
# HOME / PROFILE (default page)
# ------------------------------
if st.session_state.section == "None" and st.session_state.section2 == "None":
    st.title("Miguel A Gonzalez Almonte")
    col1, col2 = st.columns([1, 2], vertical_alignment="center")
    with col1:
        if IMG_PATH.exists():
            st.image(str(IMG_PATH), use_container_width=True)
        else:
            st.image("https://placehold.co/600x600/png", caption="Profile image placeholder")

    with col2:
        st.subheader("Data Scientist · ML Engineer · AI Enthusiast")
        st.write("""
            Field-proven systems thinker with deep roots in operations leadership and a forward trajectory
            in AI engineering. I design intelligent tools using GPT, Python, and modular workflows to streamline
            processes, enforce lifecycle logic, and improve decision velocity for real-world teams.
        """)
        st.caption("Plano, TX · mg.systems.dev@gmail.com · 787-367-9843")

        lcol1, lcol2, lcol3 = st.columns(3)
        with lcol1:
            ext_link("Portfolio", "https://mgsystemsdev.github.io/Miguel-A-Gonzalez-portfolio/", "🌐")
        with lcol2:
            ext_link("GitHub", "https://github.com/mgsystemsdev", "💻")
        with lcol3:
            ext_link("LinkedIn", "https://linkedin.com/in/miguel-gonzalez-8a389791", "🔗")

    st.divider()
    st.header("Impact at a Glance")
    mc1, mc2, mc3, mc4 = st.columns(4)
    mc1.metric("Faster execution", "50%", "+ automation")
    mc2.metric("Annual savings", "$25K+", "vs. manual")
    mc3.metric("Dashboards delivered", "5+", "real-time KPIs")
    mc4.metric("Staff enabled", "50+", "trained in BI")
    st.divider()

    st.header("Core Skills")
    sc1, sc2, sc3 = st.columns(3)
    with sc1:
        st.subheader("Data Analysis & BI")
        st.write("Power BI · Excel · SQL · Data Cleaning & Transformation")
    with sc2:
        st.subheader("Automation & Workflows")
        st.write("Python · Pandas · API Integrations · Workflow Optimization")
    with sc3:
        st.subheader("Visualization & Reporting")
        st.write("Interactive Dashboards · KPI Tracking · Custom Reporting Systems")
    st.caption("Deployment & Tools: Supabase · Git · Replit · Low-Code Data Apps")
    st.divider()

    st.header("Featured Projects")
    with st.container(border=True):
        st.subheader("Make Ready Digital Board (DMRB)")
        st.write("Python + Power BI pipeline to automate unit-turnover visibility, cutting turnover time by ~50%.")
    with st.container(border=True):
        st.subheader("Python Training Board (PTB)")
        st.write("Interactive ETL simulation app for practicing data visualization workflows and KPI design.")
    with st.container(border=True):
        st.subheader("Blueprint Buddy")
        st.write("Generator that maps operational KPIs to dashboard requirements to reduce build thrash.")
    st.divider()

    st.header("Experience")
    with st.expander("Service Maintenance Manager — MAA (Dallas, TX) · Jun 2023 – Present", expanded=True):
        st.write("- Replaced spreadsheets with Python-powered data models.\n- Delivered real-time dashboards for 20+ users.")
    with st.expander("Service Manager — RPM Living (Dallas, TX) · May 2022 – Jun 2023"):
        st.write("- Built automated Excel + Power BI dashboards, improving reporting efficiency by 70%.")
    with st.expander("Residential Renovation Lead — First Choice (Dallas, TX) · Jan 2021 – May 2022"):
        st.write("- Leveraged milestone-based tools to track performance data and scheduling accuracy.")
    with st.expander("Earlier Roles"):
        st.write("Maintenance Technician II — American Community; Ops Assistant → Kitchen Manager — Universal Studios")
    st.divider()

    st.header("Education & Certifications")
    col_edu1, col_edu2 = st.columns(2)
    with col_edu1:
        st.write("B.B.A. Computer Information Systems — Ana G. Méndez University (In Progress)")
        st.write("IBM AI Engineering Certificate (In Progress)")
    with col_edu2:
        st.write("Python for Everybody — University of Michigan, 2025")
        st.write("Python 3: Intermediate Track — Coursera, 2025")
        st.write("Google Project Management Certificate — Coursera, 2025")
    st.divider()

    st.header("Résumé")
    resume_bytes = file_bytes_if_exists(RESUME_PATH)
    if resume_bytes:
        st.download_button(
            label="Download Résumé (PDF)",
            data=resume_bytes,
            file_name="Miguel_A_Gonzalez_Almonte_Resume.pdf",
            mime="application/pdf",
            use_container_width=True,
        )
    else:
        st.info("Add your resume PDF as 'data_ai1.pdf' to enable download.")
    st.divider()

    st.header("Contact")
    cc1, cc2 = st.columns([3, 2])
    with cc1:
        st.write("For collaboration, freelance projects, or roles in data platforms and AI automation, reach out:")
        st.write("• Email: mg.systems.dev@gmail.com")
        st.write("• Location: Plano, TX")
    with cc2:
        st.success("Open to roles: Data Engineer · BI/Analytics Engineer · ML/AI Engineer (automation focus)")
    st.caption(f"© {datetime.datetime.now().year} Miguel A. Gonzalez Almonte")

# -----------------
# CATEGORY CONTENT
# -----------------
elif st.session_state.section != "None":
    if st.session_state.section == "🖥️ Dashboard":
        tabs = st.tabs(["Overview", "Roadmap", "Books", "Interactivity"])
        with tabs[0]: st.markdown(read_md("dashboard/overview.md"))
        with tabs[1]: st.markdown(read_md("dashboard/roadmap.md"))
        with tabs[2]: st.markdown(read_md("dashboard/books.md"))
        with tabs[3]: st.markdown(read_md("dashboard/interactivity.md"))

    elif st.session_state.section == "🐍 Core Language":
        tabs = st.tabs([
            "Variables", "Dictionaries", "Sets", "Control Flow",
            "Functions", "Classes", "Exceptions", "Modules",
            "Comprehensions", "Iterators", "Decorators", "Context Managers",
            "List", "Tuples", "If"
        ])
        with tabs[0]: st.markdown(read_md("python_core/variables.md"))
        with tabs[1]: st.markdown(read_md("python_core/dicts.md"))
        with tabs[2]: st.markdown(read_md("python_core/sets.md"))
        with tabs[3]: st.markdown(read_md("python_core/control_flow.md"))
        with tabs[4]: st.markdown(read_md("python_core/functions.md"))
        with tabs[5]: st.markdown(read_md("python_core/classes.md"))
        with tabs[6]: st.markdown(read_md("python_core/exceptions.md"))
        with tabs[7]: st.markdown(read_md("python_core/modules.md"))
        with tabs[8]: st.markdown(read_md("python_core/comprehensions.md"))
        with tabs[9]: st.markdown(read_md("python_core/iterators.md"))
        with tabs[10]: st.markdown(read_md("python_core/decorators.md"))
        with tabs[11]: st.markdown(read_md("python_core/context_managers.md"))
        with tabs[12]: st.markdown(read_md("python_core/list.md"))
        with tabs[13]: st.markdown(read_md("python_core/tuples.md"))
        with tabs[14]: st.markdown(read_md("python_core/if.md"))

    elif st.session_state.section == "📦 Standard Library":
        tabs = st.tabs([
            "File I/O", "OS/Pathlib", "Datetime", "Math/Random",
            "Regex", "Collections", "Itertools", "Logging", "Argparse"
        ])
        with tabs[0]: st.markdown(read_md("stdlib/fileio.md"))
        with tabs[1]: st.markdown(read_md("stdlib/os_pathlib.md"))
        with tabs[2]: st.markdown(read_md("stdlib/datetime.md"))
        with tabs[3]: st.markdown(read_md("stdlib/math_random.md"))
        with tabs[4]: st.markdown(read_md("stdlib/regex.md"))
        with tabs[5]: st.markdown(read_md("stdlib/collections.md"))
        with tabs[6]: st.markdown(read_md("stdlib/itertools.md"))
        with tabs[7]: st.markdown(read_md("stdlib/logging.md"))
        with tabs[8]: st.markdown(read_md("stdlib/argparse.md"))

    elif st.session_state.section == "📊 Data Science":
        tabs = st.tabs([
            "Pandas", "NumPy", "Matplotlib", "Seaborn",
            "SciPy", "Scikit-learn", "Jupyter"
        ])
        with tabs[0]: st.markdown(read_md("datasci/pandas.md"))
        with tabs[1]: st.markdown(read_md("datasci/numpy.md"))
        with tabs[2]: st.markdown(read_md("datasci/matplotlib.md"))
        with tabs[3]: st.markdown(read_md("datasci/seaborn.md"))
        with tabs[4]: st.markdown(read_md("datasci/scipy.md"))
        with tabs[5]: st.markdown(read_md("datasci/sklearn.md"))
        with tabs[6]: st.markdown(read_md("datasci/jupyter.md"))

    elif st.session_state.section == "🤖 Automation & Scripting":
        tabs = st.tabs([
            "Streamlit", "Excel", "CSV & JSON", "Web",
            "Email", "APIs", "PyAutoGUI", "Schedule"
        ])
        with tabs[0]: st.markdown(read_md("automated/streamlit.md"))
        with tabs[1]: st.markdown(read_md("automated/excel.md"))
        with tabs[2]: st.markdown(read_md("automated/csv_json.md"))
        with tabs[3]: st.markdown(read_md("automated/web.md"))
        with tabs[4]: st.markdown(read_md("automated/email.md"))
        with tabs[5]: st.markdown(read_md("automated/apis.md"))
        with tabs[6]: st.markdown(read_md("automated/pyautogui.md"))
        with tabs[7]: st.markdown(read_md("automated/schedule.md"))

    elif st.session_state.section == "🎯 Advanced Python":
        tabs = st.tabs(["Typing", "Dataclasses", "Dunder Methods", "Concurrency"])
        with tabs[0]: st.markdown(read_md("advanced/typing.md"))
        with tabs[1]: st.markdown(read_md("advanced/dataclasses.md"))
        with tabs[2]: st.markdown(read_md("advanced/dunder.md"))
        with tabs[3]: st.markdown(read_md("advanced/concurrency.md"))

    elif st.session_state.section == "📚 Notes":
        tabs = st.tabs(["General Tips", "Best Practices", "Common Pitfalls"])
        with tabs[0]: st.markdown(read_md("notes/general_tips.md"))
        with tabs[1]: st.markdown(read_md("notes/best_practices.md"))
        with tabs[2]: st.markdown(read_md("notes/common_pitfalls.md"))

# -----------------
# BOOK CONTENT
# -----------------
elif st.session_state.section2 != "None":
    if st.session_state.section2 == "📘 Python Crash Course":
        tabs = st.tabs([
            "Ch2: Variables & Data Types",
            "Ch3: Lists",
            "Ch4: Working with Lists",
            "Ch5: if Statements",
            "Ch6: Dictionaries",
            "Ch7: User Input & while Loops",
            "Ch8: Functions",
            "Ch9: Classes",
            "Ch10: Files & Exceptions",
            "Ch11: Testing"
        ])
        with tabs[0]: st.markdown(read_md("pcc/ch2_variables.md"))
        with tabs[1]: st.markdown(read_md("pcc/ch3_lists.md"))
        with tabs[2]: st.markdown(read_md("pcc/ch4_working_lists.md"))
        with tabs[3]: st.markdown(read_md("pcc/ch5_if.md"))
        with tabs[4]: st.markdown(read_md("pcc/ch6_dicts.md"))
        with tabs[5]: st.markdown(read_md("pcc/ch7_loops.md"))
        with tabs[6]: st.markdown(read_md("pcc/ch8_functions.md"))
        with tabs[7]: st.markdown(read_md("pcc/ch9_classes.md"))
        with tabs[8]: st.markdown(read_md("pcc/ch10_files_exceptions.md"))
        with tabs[9]: st.markdown(read_md("pcc/ch11_testing.md"))

    elif st.session_state.section2 == "📖 Automate the Boring Stuff with Python":
        tabs = st.tabs([
            "Ch1: Python Basics",
            "Ch2: Flow Control",
            "Ch3: Functions",
            "Ch4: Lists",
            "Ch5: Dictionaries & Structuring Data",
            "Ch6: Strings",
            "Ch7: Pattern Matching with Regex",
            "Ch8: Input Validation",
            "Ch9: File Reading/Writing",
            "Ch10: Organizing Files"
        ])
        with tabs[0]: st.markdown(read_md("atbs/ch1_basics.md"))
        with tabs[1]: st.markdown(read_md("atbs/ch2_flow_control.md"))
        with tabs[2]: st.markdown(read_md("atbs/ch3_functions.md"))
        with tabs[3]: st.markdown(read_md("atbs/ch4_lists.md"))
        with tabs[4]: st.markdown(read_md("atbs/ch5_dicts.md"))
        with tabs[5]: st.markdown(read_md("atbs/ch6_strings.md"))
        with tabs[6]: st.markdown(read_md("atbs/ch7_regex.md"))
        with tabs[7]: st.markdown(read_md("atbs/ch8_input_validation.md"))
        with tabs[8]: st.markdown(read_md("atbs/ch9_files.md"))
        with tabs[9]: st.markdown(read_md("atbs/ch10_organizing_files.md"))
