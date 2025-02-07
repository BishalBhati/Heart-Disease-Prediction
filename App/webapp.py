import streamlit as st

home = st.Page(
    "pages/home.py",
    title="Home",
    icon=":material/home:",
    default=True,
)
project = st.Page(
    "pages/project.py",
    title="Project",
    icon=":material/bar_chart:",
)
dataset = st.Page(
    "pages/dataset.py",
    title="Dataset",
    icon=":material/analytics:",
)


pg = st.navigation(pages=[home, project, dataset])

pg.run()