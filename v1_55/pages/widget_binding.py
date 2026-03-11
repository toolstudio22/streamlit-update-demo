"""Widget Binding デモ - クエリパラメータとの同期"""

import streamlit as st

st.title("🔗 Widget Binding")

st.markdown(
    """
    Streamlit 1.55.0 では、ほとんどのウィジェットに **bind** パラメータが追加されました。
    
    `bind="query-params"` を設定すると、ウィジェットの値が URL のクエリパラメータと
    **自動的に双方向同期**されます。
    
    これにより、URL を共有するだけで同じ状態を再現できます！
    """
)

st.divider()

# ========================================
# 1. Slider with bind
# ========================================
st.subheader("1️⃣ Slider - 予算設定")

st.markdown(
    """
    スライダーを動かすと、URL のクエリパラメータが自動で更新されます。
    URL をコピーして新しいタブで開くと、同じ値が復元されます。
    """
)

budget = st.slider(
    "キャンペーン予算（万円）",
    min_value=10,
    max_value=200,
    value=50,
    step=10,
    key="budget",
    bind="query-params",  # ✨ URL と自動同期
)

col1, col2 = st.columns([2, 1])

with col1:
    st.metric(
        "設定された予算",
        f"¥{budget * 10000:,}",
        delta=f"{budget - 50}万円",
        delta_description="基準値(50万円)との差"
    )

with col2:
    st.code(f"?budget={budget}", language="text")

st.divider()

# ========================================
# 2. Select with bind
# ========================================
st.subheader("2️⃣ Selectbox - 地域選択")

region = st.selectbox(
    "対象地域",
    ["東京", "大阪", "名古屋", "福岡", "札幌"],
    index=0,
    key="region",
    bind="query-params",  # ✨ URL と自動同期
)

st.success(f"選択された地域: **{region}**")
st.code(f"?region={region}", language="text")

st.divider()

# ========================================
# 3. Multiselect with bind
# ========================================
st.subheader("3️⃣ Multiselect - 商品カテゴリ")

st.markdown(
    """
    **新機能**: `st.multiselect` は「すべて選択」ボタンも追加されました！
    ドロップダウンを開いて確認してみてください。
    """
)

categories = st.multiselect(
    "商品カテゴリ（複数選択可）",
    ["電子機器", "家具", "食品", "衣類", "書籍", "スポーツ用品"],
    default=["電子機器"],
    key="categories",
    bind="query-params",  # ✨ URL と自動同期
)

if categories:
    st.success(f"選択されたカテゴリ: **{', '.join(categories)}**")
else:
    st.warning("カテゴリが選択されていません")

st.code(f"?categories={categories}", language="text")

st.divider()

# ========================================
# 4. Text input with bind
# ========================================
st.subheader("4️⃣ Text Input - キャンペーン名")

campaign_name = st.text_input(
    "キャンペーン名",
    value="春のセール",
    key="campaign_name",
    bind="query-params",  # ✨ URL と自動同期
)

st.write(f"入力されたキャンペーン名: **{campaign_name}**")
st.code(f"?campaign_name={campaign_name}", language="text")

st.divider()

# ========================================
# 5. Date input with bind
# ========================================
st.subheader("5️⃣ Date Input - 開始日")

from datetime import date

start_date = st.date_input(
    "キャンペーン開始日",
    value=date(2026, 4, 1),
    key="start_date",
    bind="query-params",  # ✨ URL と自動同期
)

st.write(f"開始日: **{start_date}**")
st.code(f"?start_date={start_date}", language="text")

st.divider()

# ========================================
# 現在の URL を表示
# ========================================
st.subheader("📋 現在の URL")

st.markdown(
    """
    以下が現在の URL です。この URL を共有すると、
    同じウィジェットの状態を復元できます！
    """
)

# クエリパラメータを構築
query_params = st.query_params
if query_params:
    query_string = "&".join([f"{k}={v}" for k, v in query_params.items()])
    full_url = f"http://localhost:8501/widget_binding?{query_string}"
else:
    full_url = "http://localhost:8501/widget_binding"

st.code(full_url, language="text")

st.info(
    """
    💡 **使い方のヒント**:
    - ウィジェットを操作して、URL がリアルタイムで変化することを確認してください
    - URL をコピーして新しいタブで開くと、同じ状態が復元されます
    - チームメンバーと URL を共有して、同じ設定を再現できます
    """,
    icon="💡"
)

st.divider()

# ========================================
# まとめ
# ========================================
st.subheader("✅ Widget Binding のメリット")

col1, col2, col3 = st.columns(3)

with col1:
    with st.container(border=True):
        st.markdown("##### 🔗 状態の共有")
        st.caption("URL を共有するだけで同じ状態を再現できます")

with col2:
    with st.container(border=True):
        st.markdown("##### 🔄 自動同期")
        st.caption("ウィジェットと URL が双方向に自動同期されます")

with col3:
    with st.container(border=True):
        st.markdown("##### 🚀 簡単実装")
        st.caption("bind パラメータを追加するだけで使えます")
