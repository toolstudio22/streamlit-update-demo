"""Dynamic Containers デモ - on_change とプログラム制御"""

from datetime import datetime
import pandas as pd
import streamlit as st

st.title("📦 Dynamic Containers")

st.markdown(
    """
    Streamlit 1.55.0 では、`st.expander`, `st.popover`, `st.tabs` に
    **on_change** パラメータが追加され、開閉をトリガーに処理を実行できるようになりました。
    
    また、**key** を設定することで、プログラムから開閉を制御することも可能です。
    """
)

st.divider()

# ========================================
# 1. Expander with on_change
# ========================================
st.subheader("1️⃣ Expander with on_change")

st.markdown(
    """
    `st.expander` に `on_change` を設定すると、展開・折りたたみ時に
    コールバック関数を実行できます。また、`key` を設定することで
    `st.session_state[key]` で開閉状態を取得したり、プログラムから制御できます。
    """
)


# イベント履歴を保存する関数
def log_event(event_type: str, container_name: str):
    """イベント履歴をセッションステートに保存"""
    if "event_log" not in st.session_state:
        st.session_state.event_log = []
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    is_open = st.session_state.get(f"{container_name}_key", False)
    status = "開いた" if is_open else "閉じた"
    
    st.session_state.event_log.insert(
        0,
        f"[{timestamp}] {container_name} を{status}"
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
        "🔓 Expander を開く",
        use_container_width=True,
        on_click=set_expander_state,
        args=(True,)
    )

with col2:
    st.button(
        "🔒 Expander を閉じる",
        use_container_width=True,
        on_click=set_expander_state,
        args=(False,)
    )

# Dynamic Expander
with st.expander(
    "📊 データチャートを表示",
    expanded=False,
    key="expander_key",
    on_change=log_event,
    args=("on_change", "Expander"),
):
    if st.session_state.get("expander_key", False):
        st.success(f"✅ 現在開いています (レンダリング時刻: {datetime.now().strftime('%H:%M:%S')})")
        
        # サンプルデータ
        chart_data = pd.DataFrame({
            "売上": [120, 150, 180, 210, 240, 280],
            "利益": [30, 35, 42, 50, 58, 70],
        })
        
        st.line_chart(chart_data)
        st.caption("💡 このチャートは Expander が開いている時のみレンダリングされます")
    else:
        st.info("Expander が閉じられました")

# 現在の状態を表示
st.write(f"**現在の状態:** {'🔓 開いています' if st.session_state.get('expander_key', False) else '🔒 閉じています'}")

st.divider()

# ========================================
# 2. Popover with on_change
# ========================================
st.subheader("2️⃣ Popover with on_change")

st.markdown(
    """
    `st.popover` も同様に `on_change` とプログラム制御に対応しています。
    ポップオーバーを開くと、その時刻が記録されます。
    """
)

# Popover の状態設定関数
def set_popover_state(state: bool):
    st.session_state.popover_key = state

col3, col4 = st.columns(2)

with col3:
    with st.popover(
        "⚙️ 設定を開く",
        key="popover_key",
        on_change=log_event,
        args=("on_change", "Popover"),
    ):
        st.write("### ポップオーバー設定")
        
        if st.session_state.get("popover_key", False):
            st.success(f"✅ ポップオーバーが開かれました ({datetime.now().strftime('%H:%M:%S')})")
        
        theme = st.selectbox(
            "テーマ",
            ["Light", "Dark", "Auto"],
            key="theme_setting"
        )
        
        notifications = st.checkbox("通知を有効化", value=True)
        
        if st.button("保存", use_container_width=True):
            st.success("設定を保存しました！")

with col4:
    st.write(f"**Popover の状態:** {'🔓 開いています' if st.session_state.get('popover_key', False) else '🔒 閉じています'}")
    
    st.markdown("💡 **Note:** Popover はプログラムから開く操作がサポートされていないため、手動で開閉してください。")
    # Popover は expanded パラメータがないため、プログラムから開く操作は制限されます

st.divider()

# ========================================
# 3. Tabs with on_change
# ========================================
st.subheader("3️⃣ Tabs with on_change")

st.markdown(
    """
    `st.tabs` でも `on_change` を使用できます。タブ切り替え時にイベントを記録します。
    """
)


def log_tab_change():
    """タブ切り替えをログに記録"""
    if "tab_log" not in st.session_state:
        st.session_state.tab_log = []
    
    timestamp = datetime.now().strftime("%H:%M:%S")
    current_tab = st.session_state.get("tabs_key", "Tab 1")
    
    st.session_state.tab_log.insert(
        0,
        f"[{timestamp}] {current_tab} に切り替え"
    )
    
    # 最大5件まで保持
    st.session_state.tab_log = st.session_state.tab_log[:5]


tabs = st.tabs(
    ["📈 ダッシュボード", "📋 レポート", "⚙️ 設定"],
    key="tabs_key",
    on_change=log_tab_change,
)

with tabs[0]:
    st.write("### ダッシュボード")
    st.metric("訪問者数", "1,234", delta="123 (+11%)", delta_description="前月比")
    st.metric("売上", "¥456,789", delta="45,678 (+10%)", delta_description="前月比")

with tabs[1]:
    st.write("### レポート")
    st.write("詳細なレポートをここに表示します。")
    
    report_data = pd.DataFrame({
        "月": ["1月", "2月", "3月", "4月"],
        "売上": [100, 120, 150, 180],
        "利益": [20, 25, 32, 40],
    })
    
    st.dataframe(report_data, use_container_width=True)

with tabs[2]:
    st.write("### 設定")
    st.text_input("ユーザー名", value="user123")
    st.selectbox("言語", ["日本語", "English", "中文"])

# タブ切り替え履歴を表示
if "tab_log" in st.session_state and st.session_state.tab_log:
    with st.expander("📜 タブ切り替え履歴", expanded=False):
        for log in st.session_state.tab_log:
            st.text(log)

st.divider()

# ========================================
# イベント履歴
# ========================================
st.subheader("📜 イベント履歴")

if "event_log" in st.session_state and st.session_state.event_log:
    st.markdown("**最近のイベント:**")
    for event in st.session_state.event_log:
        st.text(event)
else:
    st.info("まだイベントがありません。上記の Expander や Popover を操作してみてください。")

# クリアボタン
if st.button("🗑️ イベント履歴をクリア"):
    st.session_state.event_log = []
    st.session_state.tab_log = []
    st.rerun()
