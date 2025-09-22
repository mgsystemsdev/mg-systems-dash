import streamlit as st
from pathlib import Path

def read_md(path):
    try:
        return Path(path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return f"❌ Missing: {path}"

st.set_page_config(page_title="Python Cheat Sheets", layout="wide")
st.title("🐍 MG Systems Dev  Hub")

section = st.sidebar.selectbox("Pick a Category", [
    "🖥️ Dashboard",
    "🐍 Core Language",
    "📦 Standard Library",
    "📊 Data Science",
    "🤖 Automation & Scripting",
    "🎯 Advanced Python",
    "📘 Python Crash Course",
    "📚 Notes"
])





if section == "🖥️ Dashboard":
    tabs = st.tabs([
        "Overview", "Roadmap", "Books", "Interactivity"
    ])
    with tabs[0]: st.markdown(read_md("dashboard/overview.md"))
    with tabs[1]: st.markdown(read_md("dashboard/roadmap.md"))
    with tabs[2]: st.markdown(read_md("dashboard/books.md"))
    with tabs[3]: st.markdown(read_md("dashboard/interactivity.md"))

elif section == "🐍 Core Language":
    tabs = st.tabs([
        "Variables", "Dictionaries", "Sets", "Control Flow",
        "Functions", "Classes", "Exceptions", "Modules",
        "Comprehensions", "Iterators", "Decorators", "Context Managers", "List",
        "Tuples", "If"
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

elif section == "📦 Standard Library":
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

elif section == "📊 Data Science":
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

elif section == "🤖 Automation & Scripting":
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

elif section == "🎯 Advanced Python":
    tabs = st.tabs(["Typing", "Dataclasses", "Dunder Methods", "Concurrency"])
    with tabs[0]: st.markdown(read_md("advanced/typing.md"))
    with tabs[1]: st.markdown(read_md("advanced/dataclasses.md"))
    with tabs[2]: st.markdown(read_md("advanced/dunder.md"))
    with tabs[3]: st.markdown(read_md("advanced/concurrency.md"))

elif section == "📘 Python Crash Course":
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

elif section == "📚 Notes":
    tabs = st.tabs([
        "General Tips",
        "Best Practices",
        "Common Pitfalls"
    ])
    with tabs[0]: st.markdown(read_md("notes/general_tips.md"))
    with tabs[1]: st.markdown(read_md("notes/best_practices.md"))
    with tabs[2]: st.markdown(read_md("notes/common_pitfalls.md"))