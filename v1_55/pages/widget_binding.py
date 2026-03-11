"""F1 Team Settings - Widget Binding デモ"""

import streamlit as st
from datetime import date

# カスタムCSS
st.markdown("""
<style>
    .settings-header {
        background: linear-gradient(135deg, #2196F3 0%, #1565C0 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    .url-box {
        background: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #2196F3;
        font-family: monospace;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="settings-header">
        <h1>🔧 F1 Team Settings</h1>
        <p>Widget Binding でチーム設定とURLを自動同期</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    Streamlit 1.55.0 では、ほとんどのウィジェットに **bind** パラメータが追加されました。
    
    `bind="query-params"` を設定すると、ウィジェットの値が URL のクエリパラメータと
    **自動的に双方向同期**されます。
    
    📤 **チーム間で設定を即座に共有！** URLをコピーするだけで同じ分析条件を再現できます。
    """
)

st.divider()

# ========================================
# 1. ドライバー選択
# ========================================
st.subheader("🏎️ ドライバー選択")

st.markdown(
    """
    ドライバーを選択すると、URL が自動更新されます。
    このURLを共有すれば、同じドライバーが選択された状態で開けます。
    """
)

driver_col1, driver_col2 = st.columns([2, 1])

with driver_col1:
    selected_driver = st.selectbox(
        "メインドライバー",
        [
            "Max Verstappen (Red Bull)",
            "Lewis Hamilton (Mercedes)",
            "Charles Leclerc (Ferrari)",
            "Lando Norris (McLaren)",
            "Carlos Sainz (Ferrari)",
            "Sergio Perez (Red Bull)",
            "George Russell (Mercedes)",
            "Fernando Alonso (Aston Martin)",
        ],
        index=0,
        key="selected_driver",
        bind="query-params",  # ✨ URL と自動同期
    )

with driver_col2:
    st.metric(
        "選択中",
        selected_driver.split("(")[0].strip(),
        delta_description="メインドライバー"
    )

st.code(f"?selected_driver={selected_driver}", language="text")

st.divider()

# ========================================
# 2. サーキット選択
# ========================================
st.subheader("🏁 サーキット選択")

circuit = st.selectbox(
    "分析対象サーキット",
    [
        "Bahrain International Circuit",
        "Jeddah Corniche Circuit",
        "Albert Park Circuit",
        "Suzuka Circuit",
        "Miami International Autodrome",
        "Monaco Circuit",
        "Circuit de Barcelona-Catalunya",
        "Silverstone Circuit",
    ],
    index=0,
    key="circuit",
    bind="query-params",  # ✨ URL と自動同期
)

circuit_info = {
    "Bahrain International Circuit": {"laps": 57, "length": "5.412 km", "record": "1:31.447"},
    "Jeddah Corniche Circuit": {"laps": 50, "length": "6.174 km", "record": "1:30.734"},
    "Albert Park Circuit": {"laps": 58, "length": "5.278 km", "record": "1:20.235"},
    "Suzuka Circuit": {"laps": 53, "length": "5.807 km", "record": "1:30.983"},
}

if circuit in circuit_info:
    info = circuit_info[circuit]
    col1, col2, col3 = st.columns(3)
    col1.metric("周回数", info["laps"], delta_description="レース距離")
    col2.metric("1周の長さ", info["length"], delta_description="サーキット")
    col3.metric("コースレコード", info["record"], delta_description="最速ラップ")

st.code(f"?circuit={circuit}", language="text")

st.divider()

# ========================================
# 3. 分析パラメータ
# ========================================
st.subheader("📊 分析パラメータ")

st.markdown(
    """
    **複数のウィジェットを同時に設定**して、包括的な分析条件を作成できます。
    すべての設定がURLに反映されます。
    """
)

param_col1, param_col2 = st.columns(2)

with param_col1:
    lap_range = st.slider(
        "分析対象ラップ範囲",
        min_value=1,
        max_value=60,
        value=(10, 50),
        key="lap_range",
        bind="query-params",  # ✨ URL と自動同期
    )
    
    st.text(f"ラップ {lap_range[0]} ～ {lap_range[1]} を分析")

with param_col2:
    tire_compound = st.radio(
        "タイヤコンパウンド",
        ["Soft", "Medium", "Hard", "All"],
        index=3,
        horizontal=True,
        key="tire_compound",
        bind="query-params",  # ✨ URL と自動同期
    )
    
    compound_colors = {
        "Soft": "🔴",
        "Medium": "🟡",
        "Hard": "⚪",
        "All": "🎨"
    }
    st.markdown(f"**選択:** {compound_colors[tire_compound]} {tire_compound}")

st.divider()

# ========================================
# 4. 比較ドライバー選択
# ========================================
st.subheader("⚖️ 比較ドライバー選択")

st.markdown(
    """
    **新機能**: `st.multiselect` は「すべて選択」ボタンが追加されました！
    ドロップダウンを開いて確認してみてください。
    """
)

comparison_drivers = st.multiselect(
    "比較対象ドライバー（複数選択可）",
    [
        "Max Verstappen",
        "Lewis Hamilton",
        "Charles Leclerc",
        "Lando Norris",
        "Carlos Sainz",
        "Sergio Perez",
        "George Russell",
        "Fernando Alonso",
        "Oscar Piastri",
        "Pierre Gasly",
    ],
    default=["Max Verstappen", "Lewis Hamilton"],
    key="comparison_drivers",
    bind="query-params",  # ✨ URL と自動同期
)

if comparison_drivers:
    st.success(f"✅ {len(comparison_drivers)} 名のドライバーを比較: {', '.join(comparison_drivers)}")
else:
    st.warning("比較ドライバーが選択されていません")

st.code(f"?comparison_drivers={comparison_drivers}", language="text")

st.divider()

# ========================================
# 5. セッション日時
# ========================================
st.subheader("📅 セッション日時")

session_date = st.date_input(
    "分析対象日",
    value=date(2026, 3, 9),
    key="session_date",
    bind="query-params",  # ✨ URL と自動同期
)

session_type = st.selectbox(
    "セッションタイプ",
    ["予選", "決勝", "フリー走行1", "フリー走行2", "フリー走行3"],
    index=1,
    key="session_type",
    bind="query-params",  # ✨ URL と自動同期
)

col1, col2 = st.columns(2)
col1.write(f"**日付:** {session_date}")
col2.write(f"**セッション:** {session_type}")

st.code(f"?session_date={session_date}&session_type={session_type}", language="text")

st.divider()

# ========================================
# 現在の設定URL
# ========================================
st.subheader("🔗 設定URL")

st.markdown(
    """
    以下が現在の設定を含むURLです。このURLを**チームメンバーと共有**すると、
    同じ分析条件を即座に再現できます！
    """
)

# クエリパラメータを構築
query_params = st.query_params
if query_params:
    query_string = "&".join([f"{k}={v}" for k, v in query_params.items()])
    full_url = f"http://localhost:8501/Team_Settings?{query_string}"
else:
    full_url = "http://localhost:8501/Team_Settings"

st.markdown(
    f"""
    <div class="url-box">
        <strong>共有用URL:</strong><br>
        {full_url}
    </div>
    """,
    unsafe_allow_html=True
)

st.info(
    """
    💡 **使い方のヒント**:
    - ウィジェットを操作して、URLがリアルタイムで変化することを確認
    - URLをコピーして新しいタブで開くと、同じ設定が復元されます
    - チームメンバーとURLを共有して、同じ分析条件を共有できます
    - ブックマークに保存して、よく使う設定に素早くアクセス
    """,
    icon="💡"
)

st.divider()

# ========================================
# まとめ
# ========================================
st.subheader("✅ Widget Binding の利点")

benefit_col1, benefit_col2, benefit_col3 = st.columns(3)

with benefit_col1:
    with st.container(border=True):
        st.markdown("### 🚀 即座に共有")
        st.caption("URLをコピーするだけで、チーム全体で同じ設定を共有")

with benefit_col2:
    with st.container(border=True):
        st.markdown("### 🔄 自動同期")
        st.caption("ウィジェットとURLが双方向に自動同期。コード不要")

with benefit_col3:
    with st.container(border=True):
        st.markdown("### 📌 設定保存")
        st.caption("ブックマークやリンクとして保存。いつでも同じ状態に戻れる")

# 実践例
st.markdown("### 🎯 実践例")

st.markdown(
    """
    <div style="background: linear-gradient(135deg, #212121 0%, #424242 100%); 
                padding: 1.5rem; border-radius: 8px; color: white;">
        <h4 style="margin-top: 0;">レースエンジニアの活用シーン</h4>
        <p>
        1. <strong>レース前分析</strong>: 特定のドライバーとサーキットの組み合わせをURL化<br>
        2. <strong>チーム会議</strong>: 全員が同じ分析条件でデータを確認<br>
        3. <strong>履歴管理</strong>: 過去のレースの分析条件を簡単に再現<br>
        4. <strong>レポート共有</strong>: メールやSlackでURLを送るだけで状態共有
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
