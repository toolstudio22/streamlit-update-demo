"""
Streamlit 1.55.0 新機能デモアプリ

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
    page_title="Streamlit 1.55.0 デモ",
    page_icon="🎉",
    layout="wide",
)

# ナビゲーション設定
overview = st.Page("pages/overview.py", title="概要", icon="🏠")
dynamic_containers = st.Page(
    "pages/dynamic_containers.py",
    title="Dynamic Containers",
    icon="📦",
)
widget_binding = st.Page(
    "pages/widget_binding.py",
    title="Widget Binding",
    icon="🔗",
)
new_features = st.Page(
    "pages/new_features.py",
    title="その他の新機能",
    icon="✨",
)
hidden_page = st.Page(
    "pages/hidden_page.py",
    title="隠しページ",
    icon="🕵️",
    visibility="hidden",  # ナビゲーションには表示されない
)

pg = st.navigation(
    {
        "メイン": [overview],
        "主要機能": [dynamic_containers, widget_binding],
        "追加機能": [new_features],
        "特殊": [hidden_page],
    }
)

pg.run()
