from pathlib import Path

import streamlit as st


ROOT = Path(__file__).parent

st.set_page_config(
    page_title="Streamlit 1.55.0 Demo",
    page_icon=":material/rocket_launch:",
    layout="wide",
)

pages = {
    "Experience 1.55.0": [
        st.Page(
            ROOT / "pages" / "overview.py",
            title="Overview",
            icon=":material/auto_awesome:",
            default=True,
        ),
        st.Page(
            ROOT / "pages" / "dynamic_containers.py",
            title="Dynamic Containers",
            icon=":material/animation:",
        ),
        st.Page(
            ROOT / "pages" / "hidden_route.py",
            title="Hidden Lab",
            icon=":material/visibility_off:",
            visibility="hidden",
        ),
    ]
}

st.navigation(pages).run()