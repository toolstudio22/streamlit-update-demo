"""概要ページ - Streamlit 1.55.0の新機能の紹介"""

import streamlit as st

st.title("🎉 Streamlit 1.55.0 新機能デモ")

st.markdown(
    """
    このデモアプリでは、**Streamlit 1.55.0** で追加された主要な新機能を
    インタラクティブに体験できます。
    """
)

st.divider()

# 主要機能のハイライト
st.subheader("📌 主要な新機能")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        ### 🍿 Dynamic Containers
        `st.tabs`, `st.popover`, `st.expander` に **on_change** パラメータが追加されました。
        これにより、コンテナの開閉時にアプリを再実行できます。
        また、キーを設定することでプログラムから開閉を制御することも可能です。
        
        **新しいパラメータ:**
        - `on_change`: 開閉時のコールバック関数
        - `key`: セッションステートでの識別子
        - `.open`: 現在の開閉状態を取得
        """
    )
    
    st.page_link("pages/dynamic_containers.py", label="➡️ Dynamic Containers を試す", icon="📦")

with col2:
    st.markdown(
        """
        ### 🖇️ Widget Binding
        ほとんどのウィジェットに **bind** パラメータが追加され、
        ウィジェットの状態とクエリパラメータを簡単に同期できるようになりました。
        
        **特徴:**
        - `bind="query-params"` で URL と自動同期
        - URL を共有すると同じ状態を再現
        - リアルタイムで双方向同期
        """
    )
    
    st.page_link("pages/widget_binding.py", label="➡️ Widget Binding を試す", icon="🔗")

st.divider()

# その他の新機能
st.subheader("✨ その他の新機能")

feature_col1, feature_col2, feature_col3 = st.columns(3)

with feature_col1:
    with st.container(border=True):
        st.markdown("##### 🔗 クリック可能な画像")
        st.caption("`st.image` に `link` パラメータが追加され、画像をクリック可能なリンクにできます。")

with feature_col2:
    with st.container(border=True):
        st.markdown("##### 🥷 隠しページ")
        st.caption("`st.Page` に `visibility` パラメータが追加され、ナビゲーションに表示せずにルーティング可能なページを作成できます。")

with feature_col3:
    with st.container(border=True):
        st.markdown("##### 🎨 Markdown CSS カラー")
        st.caption("Markdown で任意の CSS カラーを使用できるようになりました。")

feature_col4, feature_col5, feature_col6 = st.columns(3)

with feature_col4:
    with st.container(border=True):
        st.markdown("##### 📐 Metric 説明文")
        st.caption("`st.metric` に `delta_description` パラメータが追加され、デルタ値に説明を追加できます。")

with feature_col5:
    with st.container(border=True):
        st.markdown("##### 🏓 Table サイズ指定")
        st.caption("`st.table` に `height` と `width` パラメータが追加され、テーブルのサイズを指定できます。")

with feature_col6:
    with st.container(border=True):
        st.markdown("##### 🏄‍♂️ Multiselect 全選択")
        st.caption("`st.multiselect` でワンクリックで全選択・全解除ができるようになりました。")

st.page_link("pages/new_features.py", label="➡️ その他の新機能を試す", icon="✨")

st.divider()

# 隠しページへのリンク
st.info(
    """
    💡 **隠しページ機能を試す**: このデモには、ナビゲーションに表示されない隠しページがあります。
    以下のリンクからアクセスしてみてください！
    """,
    icon="🕵️",
)
st.page_link("pages/hidden_page.py", label="➡️ 隠しページにアクセス", icon="🕵️")

st.divider()

# フッター
st.caption(
    """
    📚 **詳細情報**: [Streamlit 1.55.0 リリースノート](https://docs.streamlit.io/develop/quick-reference/release-notes)
    """
)
