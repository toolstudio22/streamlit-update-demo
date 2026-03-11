"""VIP Analytics - 隠しページデモ"""

import streamlit as st
import pandas as pd

# カスタムCSS
st.markdown("""
<style>
    .vip-header {
        background: linear-gradient(135deg, #212121 0%, #424242 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        border: 3px solid #ffd700;
        margin-bottom: 1rem;
    }
    .telemetry-data {
        background: #1a1a1a;
        color: #00ff00;
        padding: 1rem;
        border-radius: 8px;
        font-family: 'Courier New', monospace;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="vip-header">
        <h1>👑 VIP Analytics Access</h1>
        <p style="font-size: 1.2rem;">プレミアム・テレメトリーデータと戦略分析</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.success(
    """
    🎊 **おめでとうございます！VIPエリアへようこそ**
    
    このページは `st.Page` の **visibility="hidden"** パラメータにより、
    サイドバーのナビゲーションには表示されませんが、URLから直接アクセスできます。
    """,
    icon="🔓"
)

st.divider()

# ========================================
# テレメトリーデータ
# ========================================
st.subheader("📡 リアルタイム・テレメトリーデータ")

st.markdown(
    """
    VIPメンバー限定の詳細テレメトリーデータです。
    車両の各種センサーから取得したデータをリアルタイムで確認できます。
    """
)

telemetry_col1, telemetry_col2 = st.columns(2)

with telemetry_col1:
    st.markdown("#### 🏎️ Verstappen - 最終周回")
    
    telemetry_data = pd.DataFrame({
        "距離(m)": [0, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000],
        "速度(km/h)": [280, 295, 312, 285, 195, 245, 298, 310, 275, 220, 285],
        "スロットル(%)": [100, 100, 100, 85, 20, 75, 100, 100, 90, 60, 95],
        "ブレーキ(%)": [0, 0, 15, 45, 100, 35, 0, 10, 55, 85, 20],
        "ギア": [7, 7, 7, 6, 3, 5, 7, 7, 6, 4, 6],
    })
    
    st.dataframe(telemetry_data, use_container_width=True, hide_index=True)
    
    st.line_chart(telemetry_data, x="距離(m)", y=["速度(km/h)"], height=200)

with telemetry_col2:
    st.markdown("#### 🔧 車両パラメータ")
    
    st.metric("エンジン回転数", "13,250 RPM", delta="+250", delta_description="ストレートエンド")
    st.metric("オイル温度", "102°C", delta="-3°C", delta_description="最適範囲内", delta_color="inverse")
    st.metric("タイヤ温度 (平均)", "98°C", delta="+2°C", delta_description="理想値")
    st.metric("燃料残量", "28.5 kg", delta="-1.8 kg/lap", delta_description="消費率")
    st.metric("DRS使用回数", "8回", delta_description="本レース")

st.divider()

# ========================================
# 戦略分析
# ========================================
st.subheader("🎯 レース戦略分析")

st.markdown(
    """
    AIによる戦略予測と最適化シミュレーション結果です。
    """
)

strategy_tabs = st.tabs(["🏁 ピット戦略", "🔮 予測モデル", "📊 シナリオ分析"])

with strategy_tabs[0]:
    st.markdown("### 最適ピット戦略")
    
    pit_strategies = pd.DataFrame({
        "戦略": ["1ストップ", "2ストップ", "3ストップ"],
        "初回ピット": ["Lap 22", "Lap 15", "Lap 10"],
        "タイヤ選択": ["Medium → Hard", "Soft → Medium → Hard", "Soft → Soft → Medium → Hard"],
        "予測順位": ["2位", "1位 🏆", "3位"],
        "成功確率": ["65%", "82%", "48%"],
        "リスク": ["低", "中", "高"],
    })
    
    st.dataframe(pit_strategies, use_container_width=True, hide_index=True)
    
    st.success("**推奨戦略**: 2ストップ - 成功確率 82% 🎯", icon="✅")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("予測ラップタイム", "1:28.234", delta_description="2ストップ戦略")
    col2.metric("燃料セーブ余地", "3.2 kg", delta_description="リスク管理")
    col3.metric("タイヤライフ", "18周", delta_description="ハードコンパウンド")

with strategy_tabs[1]:
    st.markdown("### AI予測: レース結果")
    
    st.markdown(
        """
        <div class="telemetry-data">
        <strong>>> AI RACE PREDICTION SYSTEM v2.5</strong><br>
        <strong>>> Analyzing 10,000 simulations...</strong><br>
        <br>
        [■■■■■■■■■■■■■■■■■■■■] 100%<br>
        <br>
        <strong>PREDICTION RESULTS:</strong><br>
        1st Place: Verstappen (Red Bull) - 78.5% probability<br>
        2nd Place: Hamilton (Mercedes) - 62.3% probability<br>
        3rd Place: Leclerc (Ferrari) - 54.8% probability<br>
        <br>
        <strong>KEY FACTORS:</strong><br>
        * Weather: Dry (90% confidence)<br>
        * Safety Car: 34% probability (Lap 25-45)<br>
        * Optimal Strategy: 2-stop (82% success rate)<br>
        <br>
        <strong>>> CONFIDENCE LEVEL: HIGH</strong>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    prediction_data = pd.DataFrame({
        "ドライバー": ["Verstappen", "Hamilton", "Leclerc", "Norris", "Sainz"],
        "優勝確率": ["78.5%", "12.3%", "5.2%", "2.8%", "1.2%"],
        "ポディウム確率": ["95.2%", "62.3%", "54.8%", "38.5%", "32.1%"],
        "ポイント獲得確率": ["99.8%", "98.5%", "96.2%", "89.3%", "85.7%"],
    })
    
    st.dataframe(prediction_data, use_container_width=True, hide_index=True)

with strategy_tabs[2]:
    st.markdown("### レースシナリオ分析")
    
    scenarios = st.multiselect(
        "シミュレーション条件を選択",
        ["晴天", "雨", "セーフティカー", "バーチャルSC", "赤旗中断", "タイヤトラブル"],
        default=["晴天", "セーフティカー"]
    )
    
    if scenarios:
        st.info(f"**選択中のシナリオ**: {', '.join(scenarios)}", icon="🔮")
        
        if "雨" in scenarios:
            st.warning("⚠️ 雨天シナリオ: インターミディエイト/ウェットタイヤへの変更が必要。ピット戦略を再評価中...")
        
        if "セーフティカー" in scenarios:
            st.info("🚗 セーフティカー: オポチュニティピットのタイミングを最適化")
        
        # シナリオ別予測
        scenario_data = pd.DataFrame({
            "シナリオ": ["ベースケース", "SC Lap 25", "雨 Lap 35", "赤旗 Lap 40"],
            "推奨戦略": ["2ストップ", "1ストップに変更", "雨天対応", "リスタート用タイヤ"],
            "順位予測": ["1位", "2位", "3位", "1位"],
            "ポイント": ["+25", "+18", "+15", "+25"],
        })
        
        st.dataframe(scenario_data, use_container_width=True, hide_index=True)

st.divider()

# ========================================
# visibility パラメータの説明
# ========================================
st.subheader("🔒 隠しページ機能について")

st.markdown(
    """
    Streamlit 1.55.0 で追加された `st.Page` の **visibility** パラメータは、
    ページの表示方法を制御できます。
    """
)

visibility_col1, visibility_col2 = st.columns(2)

with visibility_col1:
    st.markdown("#### ✅ visibility の使い方")
    
    st.code(
        """
# app.py
hidden_page = st.Page(
    "pages/hidden_page.py",
    title="VIP Analytics",
    icon="👑",
    visibility="hidden"  # ナビに表示されない
)

pg = st.navigation({
    "Main": [overview],
    "VIP": [hidden_page],  # ここに含めても表示されない
})
        """,
        language="python"
    )

with visibility_col2:
    st.markdown("#### 🎯 活用シーン")
    
    st.markdown(
        """
        1. **VIP/プレミアム機能**: 特別なユーザーのみアクセス
        2. **詳細分析ページ**: メインメニューには出さない詳細データ
        3. **管理画面**: スタッフ専用の設定ページ
        4. **共有用ページ**: URLを知っている人だけがアクセス
        5. **開発中機能**: リリース前のテスト
        """
    )

st.divider()

# ========================================
# アクセス方法
# ========================================
st.subheader("🔗 このページへのアクセス方法")

access_tabs = st.tabs(["st.page_link", "直接URL", "st.switch_page"])

with access_tabs[0]:
    st.markdown("### st.page_link でリンク作成")
    st.code(
        """
# 他のページからこのVIPページへのリンク
st.page_link(
    "v1_55/pages/hidden_page.py",
    label="VIP Analytics にアクセス",
    icon="👑"
)
        """,
        language="python"
    )
    st.caption("👆 ダッシュボードにこのようなリンクが設置されています")

with access_tabs[1]:
    st.markdown("### 直接URLでアクセス")
    st.code(
        "http://localhost:8501/VIP_Analytics",
        language="text"
    )
    st.caption("URLを直接ブラウザに入力してもアクセスできます")

with access_tabs[2]:
    st.markdown("### プログラムから遷移")
    st.code(
        """
if st.button("VIPページへ"):
    st.switch_page("v1_55/pages/hidden_page.py")
        """,
        language="python"
    )
    
    if st.button("🏁 ダッシュボードに戻る", type="primary", use_container_width=True):
        st.switch_page("v1_55/pages/overview.py")

st.divider()

# ========================================
# 実用例
# ========================================
st.subheader("💼 F1チームでの実用例")

use_case_col1, use_case_col2 = st.columns(2)

with use_case_col1:
    with st.container(border=True):
        st.markdown("##### 🏎️ チーム戦略ルーム")
        st.caption(
            "レースエンジニアとストラテジストのみがアクセスできる"
            "詳細なテレメトリーと戦略シミュレーションページ。"
        )

with use_case_col2:
    with st.container(border=True):
        st.markdown("##### 📊 スポンサー専用レポート")
        st.caption(
            "スポンサー企業向けの特別なパフォーマンスレポート。"
            "専用URLでアクセスを制限。"
        )

use_case_col3, use_case_col4 = st.columns(2)

with use_case_col3:
    with st.container(border=True):
        st.markdown("##### 🔧 エンジニアリング分析")
        st.caption(
            "テクニカルディレクターと設計チーム向けの"
            "詳細な車両データと開発フィードバック。"
        )

with use_case_col4:
    with st.container(border=True):
        st.markdown("##### 👥 ドライバー専用ページ")
        st.caption(
            "各ドライバー専用のパーソナライズされた"
            "パフォーマンス分析とトレーニングデータ。"
        )

st.divider()

# ========================================
# まとめ
# ========================================
st.success(
    """
    ### ✅ visibility="hidden" の利点
    
    - 🎯 **アクセス制御**: 特定のユーザーのみがアクセスできる
    - 🧹 **クリーンなUI**: メインナビゲーションをシンプルに保つ
    - 🔗 **柔軟な共有**: URL経由で必要な人にだけ共有
    - 🛡️ **セキュリティ**: URL を知らない限りアクセス不可
    - 🚀 **段階的リリース**: 準備ができたら visibility を変更
    """,
    icon="💡"
)

st.divider()

# ナビゲーションリンク
st.markdown("### 🏁 他のページへ")

nav_col1, nav_col2, nav_col3, nav_col4 = st.columns(4)

with nav_col1:
    st.page_link("v1_55/pages/overview.py", label="Dashboard", icon="🏎️")

with nav_col2:
    st.page_link("v1_55/pages/dynamic_containers.py", label="Race Analytics", icon="📊")

with nav_col3:
    st.page_link("v1_55/pages/widget_binding.py", label="Team Settings", icon="🔧")

with nav_col4:
    st.page_link("v1_55/pages/new_features.py", label="Advanced Features", icon="✨")
