import streamlit as st


st.title("Hidden Route")
st.caption("このページは st.Page(..., visibility=\"hidden\") で登録されているため、ナビゲーションには表示されません。")

st.success("URL 直打ち、st.page_link、st.switch_page などからはアクセスできます。")

st.write(
    "この hidden page は 1.55.0 の visibility パラメータを使っています。"
    "メニューを増やしすぎずに、詳細ページや共有用の導線を用意したいときに便利です。"
)

st.page_link("pages/overview.py", label="Back to overview", icon=":material/arrow_back:")
st.page_link("pages/dynamic_containers.py", label="Go to dynamic containers", icon=":material/animation:")