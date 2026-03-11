import pandas as pd
import streamlit as st


st.title("Streamlit 1.55.0 Feature Demo")
st.caption("Version 1.55.0 の追加機能を、共有しやすい URL とインタラクションで体感するデモです。")

left, middle, right = st.columns(3)
left.metric("Dynamic containers", "2", delta="new", delta_description="expander と popover")
middle.metric("Widget binding", "URL sync", delta="1 click", delta_description="query params と連動")
right.metric("Hidden routes", "1", delta="new", delta_description="URL ではアクセス可能")

st.divider()

st.subheader("1. Widget binding with query params")
st.write("スライダーを動かすと URL のクエリ文字列が更新されます。URL を共有すると同じ状態を再現できます。")

budget = st.slider(
    "Campaign budget",
    min_value=10,
    max_value=100,
    value=45,
    step=5,
    format="yen",
    key="budget",
    bind="query-params",
)

st.markdown(
    f"現在の budget は **{budget}** です。URL にある `budget` パラメータと双方向に同期されます。",
    width="auto",
)
st.write("Current query params", dict(st.query_params))

st.divider()

st.subheader("2. Clickable images")
st.write("1.55.0 から st.image に link パラメータが追加され、画像そのものをリンク化できます。")

st.image(
    "https://images.unsplash.com/photo-1545239351-1141bd82e8a6?auto=format&fit=crop&w=1200&q=80",
    caption="Click this hero image to open the Streamlit release notes.",
    use_container_width=True,
    link="https://docs.streamlit.io/develop/quick-reference/release-notes",
)

st.divider()

st.subheader("3. Table sizing and metric descriptions")
feature_table = pd.DataFrame(
    [
        {"Feature": "Dynamic containers", "What changed": "open/close can trigger reruns", "Demo page": "Dynamic Containers"},
        {"Feature": "Widget binding", "What changed": "widgets can sync with query params", "Demo page": "Overview"},
        {"Feature": "st.image(link=...)", "What changed": "images can navigate to URLs", "Demo page": "Overview"},
        {"Feature": "Hidden pages", "What changed": "st.Page visibility can be hidden", "Demo page": "Hidden Lab"},
    ]
)
st.table(feature_table, width="stretch", height=280)

st.divider()

st.subheader("4. Hidden route demo")
st.write("このボタンで、ナビゲーションには出てこない hidden page に移動できます。")
st.page_link("pages/hidden_route.py", label="Open the hidden page", icon=":material/open_in_new:")