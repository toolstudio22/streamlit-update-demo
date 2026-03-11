"""
Streamlit 1.55.0 新機能デモアプリ - F1 Racing Analytics

主な新機能：
- Dynamic Containers (on_change + programmatic control)
- Widget Binding (query params sync)
- st.image with link
- st.Page with visibility
- Markdown CSS colors
- st.metric delta_description
- st.table height/width
- st.multiselect select all
"""

import streamlit as st

st.set_page_config(
    page_title="F1 Racing Analytics | Streamlit 1.55.0",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ナビゲーション設定
overview = st.Page("pages/overview.py", title="🏁 Dashboard", icon="🏎️")
dynamic_containers = st.Page(
    "pages/dynamic_containers.py",
    title="📊 Race Analytics",
    icon="📈",
)
widget_binding = st.Page(
    "pages/widget_binding.py",
    title="🔧 Team Settings",
    icon="⚙️",
)
new_features = st.Page(
    "pages/new_features.py",
    title="✨ Advanced Features",
    icon="🎯",
)
hidden_page = st.Page(
    "pages/hidden_page.py",
    title="🔒 VIP Analytics",
    icon="👑",
    visibility="hidden",  # ナビゲーションには表示されない
)

pg = st.navigation(
    {
        "🏎️ Main": [overview],
        "📊 Analytics": [dynamic_containers, widget_binding],
        "⚡ Features": [new_features],
        "🔒 VIP": [hidden_page],
    }
)

pg.run()
