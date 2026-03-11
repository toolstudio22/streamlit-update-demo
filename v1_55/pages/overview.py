"""F1 Racing Analytics Dashboard - Streamlit 1.55.0の新機能"""

import streamlit as st

# カスタムCSS - モダンなデザイン
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #e60000 0%, #8B0000 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .metric-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #2d2d2d 100%);
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #e60000;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
    }
    .feature-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
        transition: all 0.3s ease;
    }
    .feature-box:hover {
        border-color: #e60000;
        box-shadow: 0 4px 8px rgba(230,0,0,0.1);
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="main-header">
        <h1>🏎️ F1 Racing Analytics Platform</h1>
        <p style="font-size: 1.2rem; margin-top: 1rem;">Powered by Streamlit 1.55.0</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    **Streamlit 1.55.0** の最新機能とF1レーシングデータを組み合わせた、
    次世代のモータースポーツ分析プラットフォームです。
    """
)

st.divider()

# レースシーズン統計
st.markdown("## 🏁 2026年シーズン概要")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "開催済レース",
        "4 / 24",
        delta="+1",
        delta_description="今週末開催",
    )

with col2:
    st.metric(
        "平均ラップタイム",
        "1:24.532",
        delta="-0.845秒",
        delta_description="前戦比較",
    )

with col3:
    st.metric(
        "総観客動員数",
        "485,000",
        delta="+12.5%",
        delta_description="前年同期比",
    )

with col4:
    st.metric(
        "ポールポジション平均",
        "1:18.234",
        delta="-1.234秒",
        delta_description="シーズンベスト",
    )

st.divider()

# 主要機能のハイライト
st.markdown("## ⚡ プラットフォーム機能")

feature_col1, feature_col2 = st.columns(2)

with feature_col1:
    with st.container(border=True):
        st.markdown("### 📊 リアルタイムレース分析")
        st.markdown(
            """
            <div style="padding: 1rem; background: linear-gradient(135deg, #ff4444 0%, #cc0000 100%); 
                        border-radius: 8px; color: white; margin: 1rem 0;">
                <h4 style="margin: 0;">Dynamic Containers</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">
                リアルタイムでレースデータを展開・折りたたみ可能。<br>
                <code style="background: rgba(255,255,255,0.2); padding: 2px 6px; border-radius: 3px;">on_change</code> 
                パラメータでデータ更新時に自動再読み込み。
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("**主な機能:**")
        st.markdown("- 🔄 レース詳細の動的表示/非表示")
        st.markdown("- 📈 セクタータイムの展開コントロール")
        st.markdown("- 🎯 ドライバー統計のポップオーバー")
        
        st.page_link("pages/dynamic_containers.py", label="➡️ レース分析を見る", icon="📊")

with feature_col2:
    with st.container(border=True):
        st.markdown("### 🔧 チーム設定とURL共有")
        st.markdown(
            """
            <div style="padding: 1rem; background: linear-gradient(135deg, #2196F3 0%, #1565C0 100%); 
                        border-radius: 8px; color: white; margin: 1rem 0;">
                <h4 style="margin: 0;">Widget Binding</h4>
                <p style="margin: 0.5rem 0 0 0; opacity: 0.9;">
                レース設定とURLを自動同期。チーム間で簡単に共有。<br>
                <code style="background: rgba(255,255,255,0.2); padding: 2px 6px; border-radius: 3px;">bind="query-params"</code> 
                で瞬時に設定を共有。
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )
        
        st.markdown("**主な機能:**")
        st.markdown("- 🏎️ ドライバーとサーキット選択")
        st.markdown("- 🔗 設定URLの自動生成")
        st.markdown("- 📤 ワンクリックで状態共有")
        
        st.page_link("pages/widget_binding.py", label="➡️ チーム設定を開く", icon="🔧")

st.divider()

# その他の機能紹介
st.markdown("## ✨ 高度な機能")

tech_col1, tech_col2, tech_col3 = st.columns(3)

with tech_col1:
    with st.container(border=True):
        st.markdown("##### 🖼️ インタラクティブ画像")
        st.markdown(
            '<span style="color: #e60000; font-weight: bold;">st.image link</span>',
            unsafe_allow_html=True
        )
        st.caption("サーキットマップやチーム写真をクリック可能なリンクに")

with tech_col2:
    with st.container(border=True):
        st.markdown("##### 🔒 VIP専用ページ")
        st.markdown(
            '<span style="color: #e60000; font-weight: bold;">visibility="hidden"</span>',
            unsafe_allow_html=True
        )
        st.caption("特別な分析データへの限定アクセス")

with tech_col3:
    with st.container(border=True):
        st.markdown("##### 🎨 カスタムスタイリング")
        st.markdown(
            '<span style="color: #e60000; font-weight: bold;">CSS カラー</span>',
            unsafe_allow_html=True
        )
        st.caption("チームカラーでデータを視覚的に表現")

tech_col4, tech_col5, tech_col6 = st.columns(3)

with tech_col4:
    with st.container(border=True):
        st.markdown("##### 📊 詳細メトリクス")
        st.markdown(
            '<span style="color: #e60000; font-weight: bold;">delta_description</span>',
            unsafe_allow_html=True
        )
        st.caption("ラップタイムの詳細な比較説明を表示")

with tech_col5:
    with st.container(border=True):
        st.markdown("##### 📋 データテーブル")
        st.markdown(
            '<span style="color: #e60000; font-weight: bold;">height/width 指定</span>',
            unsafe_allow_html=True
        )
        st.caption("レース順位表のサイズを最適化")

with tech_col6:
    with st.container(border=True):
        st.markdown("##### ☑️ 一括選択")
        st.markdown(
            '<span style="color: #e60000; font-weight: bold;">全選択機能</span>',
            unsafe_allow_html=True
        )
        st.caption("複数ドライバーをワンクリックで選択")

st.page_link("pages/new_features.py", label="➡️ すべての機能を見る", icon="✨")

st.divider()

# VIPページへの案内
st.markdown(
    """
    <div style="background: linear-gradient(135deg, #212121 0%, #424242 100%); 
                padding: 2rem; border-radius: 10px; border: 2px solid #ffd700;
                box-shadow: 0 4px 8px rgba(255,215,0,0.3);">
        <h3 style="color: #ffd700; margin-top: 0;">👑 VIP Analytics Access</h3>
        <p style="color: white; margin-bottom: 1rem;">
        このプラットフォームには、ナビゲーションに表示されない特別な分析ページがあります。
        詳細なテレメトリーデータと戦略分析にアクセスできます。
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.page_link("pages/hidden_page.py", label="➡️ VIP Analyticsにアクセス", icon="👑")

st.divider()

# フッター
st.markdown(
    """
    <div style="text-align: center; padding: 2rem; background: #f8f9fa; border-radius: 8px;">
        <p style="color: #666; margin: 0;">
        🏎️ <strong>F1 Racing Analytics</strong> | Powered by Streamlit 1.55.0<br>
        <a href="https://docs.streamlit.io/develop/quick-reference/release-notes" 
           style="color: #e60000; text-decoration: none;">📚 リリースノートを見る</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
