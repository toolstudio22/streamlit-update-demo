"""隠しページ - visibility="hidden" のデモ"""

import streamlit as st

st.title("🕵️ 隠しページ")

st.success(
    """
    おめでとうございます！このページを見つけました 🎉
    
    このページは `st.Page` の **visibility="hidden"** パラメータにより、
    サイドバーのナビゲーションには表示されませんが、URL から直接アクセスできます。
    """,
    icon="🎊"
)

st.divider()

# ========================================
# visibility="hidden" の説明
# ========================================
st.subheader("📚 visibility パラメータとは？")

st.markdown(
    """
    Streamlit 1.55.0 で追加された `st.Page` の **visibility** パラメータは、
    ページの表示方法を制御できます。
    
    ### 使用可能な値:
    
    - **`"visible"`** (デフォルト): ナビゲーションに表示される
    - **`"hidden"`**: ナビゲーションには表示されないが、URL から直接アクセス可能
    
    ### 活用シーン:
    
    1. **詳細ページ**: メインナビゲーションには表示したくないが、リンクからアクセスしたいページ
    2. **共有用ページ**: URL を知っている人だけがアクセスできる特別なページ
    3. **管理画面**: 通常ユーザーには見せたくない管理用ページ
    4. **下書きページ**: 開発中のページをナビゲーションから隠す
    """
)

st.divider()

# ========================================
# サンプルコード
# ========================================
st.subheader("💻 実装方法")

st.code(
    """
import streamlit as st

# app.py でページを登録
hidden_page = st.Page(
    "pages/hidden_page.py",
    title="隠しページ",
    icon="🕵️",
    visibility="hidden"  # ✨ ナビゲーションには表示されない
)

pg = st.navigation({
    "メイン": [overview],
    "特殊": [hidden_page],  # ここに含めても表示されない
})

pg.run()
    """,
    language="python"
)

st.divider()

# ========================================
# アクセス方法の例
# ========================================
st.subheader("🔗 隠しページへのアクセス方法")

st.markdown(
    """
    隠しページには以下の方法でアクセスできます：
    """
)

tab1, tab2, tab3 = st.tabs(["st.page_link", "st.switch_page", "直接URL"])

with tab1:
    st.markdown("### st.page_link を使う")
    st.code(
        """
# 他のページから隠しページへのリンクを作成
st.page_link(
    "pages/hidden_page.py",
    label="隠しページにアクセス",
    icon="🕵️"
)
        """,
        language="python"
    )
    st.caption("概要ページにこのようなリンクが設置されています")

with tab2:
    st.markdown("### st.switch_page を使う")
    st.code(
        """
# ボタンクリックで隠しページに遷移
if st.button("隠しページへ"):
    st.switch_page("pages/hidden_page.py")
        """,
        language="python"
    )
    
    if st.button("🏠 概要ページへ戻る（switch_page のデモ）", type="primary"):
        st.switch_page("pages/overview.py")

with tab3:
    st.markdown("### 直接 URL でアクセス")
    st.code(
        "http://localhost:8501/hidden_page",
        language="text"
    )
    st.caption("URL を直接ブラウザに入力してもアクセスできます")

st.divider()

# ========================================
# 実用例
# ========================================
st.subheader("💡 実用例")

example_col1, example_col2 = st.columns(2)

with example_col1:
    with st.container(border=True):
        st.markdown("##### 📊 レポート詳細ページ")
        st.caption(
            "ダッシュボードから特定のレポートをクリックした時だけ表示したいページ。"
            "ナビゲーションには表示せず、リンクからのみアクセス可能にする。"
        )

with example_col2:
    with st.container(border=True):
        st.markdown("##### 🎯 キャンペーンページ")
        st.caption(
            "特定の URL を知っているユーザーだけがアクセスできるキャンペーンページ。"
            "メールやSNSで URL を共有する。"
        )

example_col3, example_col4 = st.columns(2)

with example_col3:
    with st.container(border=True):
        st.markdown("##### 🔐 管理者ページ")
        st.caption(
            "管理者だけがアクセスする設定ページ。"
            "ナビゲーションに表示せず、管理者ダッシュボードからのみリンク。"
        )

with example_col4:
    with st.container(border=True):
        st.markdown("##### 🚧 開発中ページ")
        st.caption(
            "まだ完成していないページを隠しながら開発。"
            "準備ができたら visibility を visible に変更。"
        )

st.divider()

# ========================================
# まとめ
# ========================================
st.subheader("✅ メリット")

st.info(
    """
    ### visibility="hidden" の利点:
    
    - 🎯 **ナビゲーションをシンプルに保つ**: メインメニューに不要なページを表示しない
    - 🔗 **柔軟なアクセス制御**: URL を知っている人だけがアクセス可能
    - 📱 **UX の向上**: ユーザーに必要なページだけを表示
    - 🛠️ **開発の効率化**: 開発中のページを隠しながら作業できる
    """,
    icon="💡"
)

st.divider()

# ナビゲーションリンク
st.write("### 他のページへ")
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/overview.py", label="🏠 概要に戻る", icon="🏠")
    st.page_link("pages/dynamic_containers.py", label="📦 Dynamic Containers", icon="📦")

with col2:
    st.page_link("pages/widget_binding.py", label="🔗 Widget Binding", icon="🔗")
    st.page_link("pages/new_features.py", label="✨ その他の新機能", icon="✨")
