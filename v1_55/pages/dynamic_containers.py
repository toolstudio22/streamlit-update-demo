"""F1 Race Analytics - Dynamic Containers デモ"""

from datetime import datetime
import pandas as pd
import streamlit as st

# カスタムCSS
st.markdown("""
<style>
    .race-header {
        background: linear-gradient(135deg, #e60000 0%, #8B0000 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    .telemetry-box {
        background: #1a1a1a;
        color: white;
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #00ff00;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="race-header">
        <h1>📊 F1 Race Analytics</h1>
        <p>Dynamic Containers でレースデータをインタラクティブに管理</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    Streamlit 1.55.0 では、`st.expander`, `st.popover`, `st.tabs` に
    **on_change** パラメータが追加され、開閉をトリガーに処理を実行できるようになりました。
    
    レースデータの表示/非表示を動的に制御し、必要な情報だけを効率的に表示できます。
    """
)

st.divider()

# ========================================
# 1. Expander - セクタータイム分析
# ========================================
st.subheader("🏁 セクタータイム分析")

st.markdown(
    """
    セクター別のタイム分析を展開すると、リアルタイムでデータが読み込まれます。
    プログラムからも開閉を制御できます。
    """
)

# イベント履歴を保存する関数
def log_event(event_type: str, container_name: str):
    """イベント履歴をセッションステートに保存"""
    if "event_log" not in st.session_state:
        st.session_state.event_log = []
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    is_open = st.session_state.get(f"{container_name}_key", False)
    status = "展開" if is_open else "折りたたみ"
    
    st.session_state.event_log.insert(
        0,
        f"🕐 [{timestamp}] {container_name} を{status}しました"
    )
    
    # 最大10件まで保持
    st.session_state.event_log = st.session_state.event_log[:10]


# プログラムから開閉を制御する関数
def set_expander_state(state: bool):
    st.session_state.expander_key = state

# プログラムから開閉を制御するボタン
col1, col2 = st.columns(2)
with col1:
    st.button(
        "🔓 データを展開",
        use_container_width=True,
        on_click=set_expander_state,
        args=(True,),
        type="primary"
    )

with col2:
    st.button(
        "🔒 データを折りたたむ",
        use_container_width=True,
        on_click=set_expander_state,
        args=(False,)
    )

# Dynamic Expander - セクタータイムデータ
with st.expander(
    "📈 セクター別タイムデータを表示",
    expanded=False,
    key="expander_key",
    on_change=log_event,
    args=("on_change", "セクタータイム分析"),
):
    if st.session_state.get("expander_key", False):
        st.success(f"✅ データ読み込み完了 ({datetime.now().strftime('%H:%M:%S')})")
        
        # F1セクタータイムデータ
        sector_data = pd.DataFrame({
            "ドライバー": ["Verstappen", "Hamilton", "Leclerc", "Norris", "Sainz", "Perez"],
            "セクター1": ["28.234", "28.445", "28.567", "28.789", "28.892", "29.012"],
            "セクター2": ["37.891", "37.956", "38.023", "38.145", "38.234", "38.456"],
            "セクター3": ["22.567", "22.678", "22.789", "22.890", "22.945", "23.123"],
            "ラップタイム": ["1:28.692", "1:29.079", "1:29.379", "1:29.824", "1:30.071", "1:30.591"],
        })
        
        st.dataframe(
            sector_data,
            use_container_width=True,
            hide_index=True,
        )
        
        # チャート表示
        chart_data = pd.DataFrame({
            "ラップ": list(range(1, 11)),
            "Verstappen": [90.234, 89.567, 89.123, 88.891, 88.692, 88.567, 88.456, 88.345, 88.234, 88.123],
            "Hamilton": [90.567, 89.890, 89.456, 89.234, 89.079, 88.956, 88.834, 88.712, 88.590, 88.467],
        })
        
        st.line_chart(chart_data, x="ラップ", y=["Verstappen", "Hamilton"])
        st.caption("💡 このデータは Expander が開いている時のみレンダリングされます")
    else:
        st.info("セクターデータが折りたたまれています")

# 現在の状態を表示
status_icon = "🔓" if st.session_state.get('expander_key', False) else "🔒"
status_text = "展開中" if st.session_state.get('expander_key', False) else "折りたたみ中"
st.markdown(f"**現在の状態:** {status_icon} {status_text}")

st.divider()

# ========================================
# 2. Popover - ドライバー詳細情報
# ========================================
st.subheader("🏎️ ドライバー詳細情報")

st.markdown(
    """
    各ドライバーの詳細情報をポップオーバーで表示します。
    開閉イベントが記録されます。
    """
)

driver_col1, driver_col2, driver_col3, driver_col4 = st.columns(4)

with driver_col1:
    with st.popover(
        "🇳🇱 Verstappen",
        key="verstappen_popover",
        on_change=log_event,
        args=("on_change", "Verstappen詳細"),
    ):
        st.markdown("### Max Verstappen")
        st.image("https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=400&q=80")
        st.metric("ポイント", "125", delta="+25", delta_description="前戦から")
        st.metric("ポディウム", "4/4", delta="100%", delta_description="表彰台率")
        st.markdown("**チーム:** Red Bull Racing")
        st.markdown("**国籍:** オランダ 🇳🇱")

with driver_col2:
    with st.popover(
        "🇬🇧 Hamilton",
        key="hamilton_popover",
        on_change=log_event,
        args=("on_change", "Hamilton詳細"),
    ):
        st.markdown("### Lewis Hamilton")
        st.image("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?w=400&q=80")
        st.metric("ポイント", "98", delta="+18", delta_description="前戦から")
        st.metric("ポディウム", "3/4", delta="75%", delta_description="表彰台率")
        st.markdown("**チーム:** Mercedes-AMG")
        st.markdown("**国籍:** イギリス 🇬🇧")

with driver_col3:
    with st.popover(
        "🇲🇨 Leclerc",
        key="leclerc_popover",
        on_change=log_event,
        args=("on_change", "Leclerc詳細"),
    ):
        st.markdown("### Charles Leclerc")
        st.image("https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=400&q=80")
        st.metric("ポイント", "87", delta="+15", delta_description="前戦から")
        st.metric("ポディウム", "2/4", delta="50%", delta_description="表彰台率")
        st.markdown("**チーム:** Ferrari")
        st.markdown("**国籍:** モナコ 🇲🇨")

with driver_col4:
    with st.popover(
        "🇬🇧 Norris",
        key="norris_popover",
        on_change=log_event,
        args=("on_change", "Norris詳細"),
    ):
        st.markdown("### Lando Norris")
        st.image("https://images.unsplash.com/photo-1583121274602-3e2820c69888?w=400&q=80")
        st.metric("ポイント", "76", delta="+12", delta_description="前戦から")
        st.metric("ポディウム", "2/4", delta="50%", delta_description="表彰台率")
        st.markdown("**チーム:** McLaren")
        st.markdown("**国籍:** イギリス 🇬🇧")

st.info("💡 **ヒント**: 各ドライバー名をクリックして詳細情報を表示してください", icon="💡")

st.divider()

# ========================================
# 3. Tabs - レース詳細タブ
# ========================================
st.subheader("📋 レース詳細データ")

st.markdown(
    """
    タブを切り替えると、イベントが記録されます。
    各タブで異なるレース情報を確認できます。
    """
)


def log_tab_change():
    """タブ切り替えをログに記録"""
    if "tab_log" not in st.session_state:
        st.session_state.tab_log = []
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    current_tab = st.session_state.get("tabs_key", "順位表")
    
    st.session_state.tab_log.insert(
        0,
        f"🕐 [{timestamp}] {current_tab} タブに切り替え"
    )
    
    # 最大5件まで保持
    st.session_state.tab_log = st.session_state.tab_log[:5]


tabs = st.tabs(
    ["🏆 順位表", "⚡ ラップタイム", "🔧 ピット戦略", "📊 統計"],
    key="tabs_key",
    on_change=log_tab_change,
)

with tabs[0]:
    st.markdown("### 🏆 ドライバーズ選手権順位")
    
    standings_data = pd.DataFrame({
        "順位": [1, 2, 3, 4, 5, 6, 7, 8],
        "ドライバー": ["Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "Lando Norris", 
                   "Carlos Sainz", "Sergio Perez", "George Russell", "Fernando Alonso"],
        "チーム": ["Red Bull", "Mercedes", "Ferrari", "McLaren", 
                 "Ferrari", "Red Bull", "Mercedes", "Aston Martin"],
        "ポイント": [125, 98, 87, 76, 65, 58, 52, 45],
        "優勝回数": [2, 1, 1, 0, 0, 0, 0, 0],
    })
    
    st.dataframe(standings_data, use_container_width=True, hide_index=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("トップのリード", "+27pts", delta_description="2位との差")
    col2.metric("最多優勝", "Verstappen", delta="2勝", delta_description="現シーズン")
    col3.metric("最多ポールポジション", "Verstappen", delta="3回", delta_description="現シーズン")

with tabs[1]:
    st.markdown("### ⚡ ファステストラップ")
    
    fastest_laps = pd.DataFrame({
        "サーキット": ["バーレーン", "サウジアラビア", "オーストラリア", "日本"],
        "ドライバー": ["Verstappen", "Leclerc", "Hamilton", "Verstappen"],
        "タイム": ["1:31.447", "1:28.997", "1:18.235", "1:30.983"],
        "平均速度": ["203.8 km/h", "251.2 km/h", "237.5 km/h", "198.6 km/h"],
    })
    
    st.dataframe(fastest_laps, use_container_width=True, hide_index=True)
    
    st.line_chart(
        pd.DataFrame({
            "ラップ": range(1, 21),
            "ラップタイム(秒)": [91.5, 90.8, 90.2, 89.8, 89.5, 89.3, 89.1, 88.9, 88.7, 88.5,
                            88.4, 88.3, 88.3, 88.2, 88.2, 88.3, 88.4, 88.5, 88.7, 89.0]
        }),
        x="ラップ",
        y="ラップタイム(秒)"
    )

with tabs[2]:
    st.markdown("### 🔧 ピット戦略")
    
    pit_strategy = pd.DataFrame({
        "ドライバー": ["Verstappen", "Hamilton", "Leclerc", "Norris"],
        "ピット回数": [2, 2, 3, 2],
        "初回ピット": ["Lap 18", "Lap 16", "Lap 12", "Lap 20"],
        "タイヤ戦略": ["Medium → Hard", "Soft → Medium", "Soft → Medium → Hard", "Medium → Hard"],
        "ピット滞在時間": ["2.4秒", "2.6秒", "2.3秒", "2.8秒"],
    })
    
    st.dataframe(pit_strategy, use_container_width=True, hide_index=True)
    
    st.info("最速ピットストップ: **Leclerc (2.3秒)** 🏎️", icon="⚡")

with tabs[3]:
    st.markdown("### 📊 シーズン統計")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("平均ラップタイム", "1:32.456", delta="-0.234秒", delta_description="前戦比")
        st.metric("平均ピット回数", "2.1回", delta_description="レースあたり")
        st.metric("最高速度", "352.3 km/h", delta="+5.2 km/h", delta_description="シーズン最高")
    
    with col2:
        st.metric("リタイア率", "8.3%", delta="-2.1%", delta_description="前年比")
        st.metric("セーフティカー率", "25%", delta_description="全レース中")
        st.metric("平均オーバーテイク", "18.5回", delta="+3.2", delta_description="レースあたり")

# タブ切り替え履歴を表示
if "tab_log" in st.session_state and st.session_state.tab_log:
    with st.expander("📜 タブ切り替え履歴", expanded=False):
        for log in st.session_state.tab_log:
            st.text(log)

st.divider()

# ========================================
# イベント履歴
# ========================================
st.subheader("📜 アクティビティログ")

if "event_log" in st.session_state and st.session_state.event_log:
    st.markdown("**最近のアクション:**")
    
    log_container = st.container(border=True)
    with log_container:
        for event in st.session_state.event_log:
            st.text(event)
else:
    st.info("まだアクティビティがありません。上記のデータを操作してみてください。", icon="ℹ️")

# クリアボタン
if st.button("🗑️ ログをクリア", use_container_width=True):
    st.session_state.event_log = []
    st.session_state.tab_log = []
    st.rerun()
