"""F1 Advanced Features - その他の新機能デモ"""

import pandas as pd
import streamlit as st

# カスタムCSS
st.markdown("""
<style>
    .feature-header {
        background: linear-gradient(135deg, #FF6B6B 0%, #cc0000 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1rem;
    }
    .showcase-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border: 2px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="feature-header">
        <h1>✨ F1 Advanced Features</h1>
        <p>Streamlit 1.55.0 の高度な機能を体験</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    Streamlit 1.55.0 で追加された、その他の便利な新機能を
    F1レーシングデータで紹介します。
    """
)

st.divider()

# ========================================
# 1. クリック可能な画像（サーキット）
# ========================================
st.subheader("🖼️ インタラクティブ・サーキットマップ")

st.markdown(
    """
    `st.image` に **link** パラメータが追加されました。
    サーキットマップをクリックすると、公式情報ページに遷移します。
    """
)

circuit_col1, circuit_col2, circuit_col3 = st.columns(3)

with circuit_col1:
    st.markdown("#### 🇯🇵 Suzuka Circuit")
    st.image(
        "https://images.unsplash.com/photo-1540747913346-19e32be4fac4?w=600&q=80",
        caption="クリックしてサーキット情報を見る",
        use_container_width=True,
        link="https://www.suzukacircuit.jp/",  # ✨ 画像をクリック可能に
    )
    st.caption("📍 三重県 | ⏱️ コースレコード: 1:30.983")

with circuit_col2:
    st.markdown("#### 🇲🇨 Monaco Circuit")
    st.image(
        "https://images.unsplash.com/photo-1558618666-fcd25c85cd64?w=600&q=80",
        caption="クリックしてサーキット情報を見る",
        use_container_width=True,
        link="https://www.acm.mc/",  # ✨ 画像をクリック可能に
    )
    st.caption("📍 モナコ | ⏱️ コースレコード: 1:12.909")

with circuit_col3:
    st.markdown("#### 🇮🇹 Monza Circuit")
    st.image(
        "https://images.unsplash.com/photo-1568605117036-5fe5e7bab0b7?w=600&q=80",
        caption="クリックしてサーキット情報を見る",
        use_container_width=True,
        link="https://www.monzanet.it/",  # ✨ 画像をクリック可能に
    )
    st.caption("📍 イタリア | ⏱️ コースレコード: 1:21.046")

st.info(
    """
    👆 **各サーキット画像をクリック**してみてください！
    
    ```python
    st.image(
        "circuit.jpg",
        link="https://circuit-info.com"
    )
    ```
    """,
    icon="💡"
)

st.divider()

# ========================================
# 2. Markdown でチームカラーを表現
# ========================================
st.subheader("🎨 チームカラーによるデータ表現")

st.markdown(
    """
    Markdown で **任意の CSS カラー** が使えるようになりました！
    F1チームのブランドカラーでデータを視覚的に表現できます。
    """
)

st.markdown(
    """
    ### 2026 シーズン参戦チーム
    
    - <span style="background-color: #1E41FF; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold;">🏎️ Red Bull Racing</span> - 最速チーム
    - <span style="background-color: #00D2BE; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold;">⭐ Mercedes-AMG</span> - 伝統の強豪
    - <span style="background-color: #DC0000; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold;">🐎 Ferrari</span> - 伝説のプランシングホース
    - <span style="background-color: #FF8700; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold;">🟠 McLaren</span> - 若手エース軍団
    - <span style="background-color: #006F62; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold;">💚 Aston Martin</span> - 躍進中
    - <span style="background-color: #0090FF; color: white; padding: 4px 12px; border-radius: 4px; font-weight: bold;">🔵 Alpine</span> - フランスの誇り
    
    **Color Coding で一目瞭然！**
    """,
    unsafe_allow_html=True
)

with st.expander("📝 実装コード"):
    st.code(
        """
st.markdown(
    '<span style="background-color: #DC0000; color: white; padding: 4px 12px;">Ferrari</span>',
    unsafe_allow_html=True
)
        """,
        language="python"
    )

st.divider()

# ========================================
# 3. st.metric with delta_description
# ========================================
st.subheader("📊 詳細なパフォーマンスメトリクス")

st.markdown(
    """
    `st.metric` に **delta_description** パラメータが追加され、
    デルタ値に詳しい説明を追加できるようになりました。
    """
)

metric_col1, metric_col2, metric_col3, metric_col4 = st.columns(4)

with metric_col1:
    st.metric(
        "ポールポジション",
        "1:18.234",
        delta="-1.234秒",
        delta_description="前戦 vs 今戦",  # ✨ デルタの説明
    )

with metric_col2:
    st.metric(
        "トップスピード",
        "352.3 km/h",
        delta="+5.2 km/h",
        delta_description="シーズン最高速",  # ✨ デルタの説明
    )

with metric_col3:
    st.metric(
        "ピットストップ",
        "2.3秒",
        delta="-0.2秒",
        delta_description="チーム平均比",  # ✨ デルタの説明
        delta_color="inverse",
    )

with metric_col4:
    st.metric(
        "タイヤ劣化率",
        "0.089秒/周",
        delta="+0.012",
        delta_description="ソフトコンパウンド",  # ✨ デルタの説明
        delta_color="inverse",
    )

st.success("**解説付きメトリクス**で、データの意味を明確に伝達！", icon="✅")

with st.expander("📝 実装コード"):
    st.code(
        """
st.metric(
    "ポールポジション",
    "1:18.234",
    delta="-1.234秒",
    delta_description="前戦 vs 今戦"  # ✨ 新機能
)
        """,
        language="python"
    )

st.divider()

# ========================================
# 4. st.table with height/width
# ========================================
st.subheader("📋 最適化されたレース順位表")

st.markdown(
    """
    `st.table` に **height** と **width** パラメータが追加され、
    テーブルのサイズを明示的に指定できるようになりました。
    """
)

# サンプルデータ
race_results = pd.DataFrame({
    "順位": list(range(1, 21)),
    "ドライバー": [
        "M. Verstappen", "L. Hamilton", "C. Leclerc", "L. Norris", "C. Sainz",
        "S. Perez", "G. Russell", "F. Alonso", "O. Piastri", "P. Gasly",
        "E. Ocon", "Y. Tsunoda", "A. Albon", "V. Bottas", "K. Magnussen",
        "N. Hulkenberg", "L. Stroll", "D. Ricciardo", "G. Zhou", "L. Sargeant"
    ],
    "チーム": [
        "Red Bull", "Mercedes", "Ferrari", "McLaren", "Ferrari",
        "Red Bull", "Mercedes", "Aston Martin", "McLaren", "Alpine",
        "Alpine", "AlphaTauri", "Williams", "Alfa Romeo", "Haas",
        "Haas", "Aston Martin", "AlphaTauri", "Alfa Romeo", "Williams"
    ],
    "タイム": [
        "1:34:24.567", "+12.345", "+18.901", "+24.567", "+31.234",
        "+35.678", "+42.123", "+48.901", "+54.234", "+1:02.567",
        "+1:08.901", "+1:15.234", "+1 Lap", "+1 Lap", "+1 Lap",
        "+2 Laps", "+2 Laps", "DNF", "DNF", "DNF"
    ],
    "ポイント": [25, 18, 15, 12, 10, 8, 6, 4, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
})

table_col1, table_col2 = st.columns(2)

with table_col1:
    st.markdown("**デフォルトサイズ**")
    st.table(race_results.head(5))

with table_col2:
    st.markdown("**カスタムサイズ (height=300)**")
    st.table(race_results, height=300)  # ✨ 高さを指定

st.caption("💡 右側のテーブルは高さを指定してスクロール可能にしています")

with st.expander("📝 実装コード"):
    st.code(
        """
st.table(race_results, height=300)  # ✨ 高さを指定
st.table(race_results, width=800)   # ✨ 幅を指定
        """,
        language="python"
    )

st.divider()

# ========================================
# 5. st.multiselect の全選択機能
# ========================================
st.subheader("☑️ 一括ドライバー選択")

st.markdown(
    """
    `st.multiselect` でドロップダウンを開くと、
    **「すべて選択」** ボタンが表示されるようになりました。
    
    レースデータ分析で複数ドライバーを選択する時に便利！
    """
)

selected_for_analysis = st.multiselect(
    "分析対象ドライバーを選択（ドロップダウンを開いて「すべて選択」を試してみてください）",
    [
        "Max Verstappen (Red Bull)",
        "Sergio Perez (Red Bull)",
        "Lewis Hamilton (Mercedes)",
        "George Russell (Mercedes)",
        "Charles Leclerc (Ferrari)",
        "Carlos Sainz (Ferrari)",
        "Lando Norris (McLaren)",
        "Oscar Piastri (McLaren)",
        "Fernando Alonso (Aston Martin)",
        "Lance Stroll (Aston Martin)",
    ],
    default=["Max Verstappen (Red Bull)", "Lewis Hamilton (Mercedes)"],
)

if len(selected_for_analysis) > 0:
    st.success(f"✅ {len(selected_for_analysis)} 名のドライバーが選択されています")
    
    # 選択されたドライバーをチップ表示
    st.markdown("**選択中:**")
    chips = " ".join([f"`{driver.split('(')[0].strip()}`" for driver in selected_for_analysis])
    st.markdown(chips)
else:
    st.warning("ドライバーが選択されていません")

st.info(
    """
    💡 **使い方**:
    1. ドロップダウンをクリックして開く
    2. 「すべて選択」ボタンをクリック
    3. 全ドライバーが一度に選択されます
    4. チーム別分析などに便利！
    """,
    icon="💡"
)

st.divider()

# ========================================
# 6. ページタイトルの Markdown サポート
# ========================================
st.subheader("📝 リッチなナビゲーション")

st.markdown(
    """
    `st.Page` のタイトルと `st.navigation` のセクションラベルで
    **Markdown** が使えるようになりました。
    
    このアプリのナビゲーションでも絵文字や装飾を活用しています！
    """
)

st.code(
    """
# ナビゲーションでMarkdownを使用
overview = st.Page(
    "pages/overview.py",
    title="🏁 Dashboard",  # ✨ 絵文字が使える
    icon="🏎️"
)

pg = st.navigation({
    "🏎️ Main": [overview],  # ✨ セクションラベルでも使える
})
    """,
    language="python"
)

st.info(
    "サイドバーのナビゲーションを確認してください。視覚的で分かりやすいメニューになっています！",
    icon="👀"
)

st.divider()

# ========================================
# まとめ
# ========================================
st.subheader("🏁 まとめ")

st.markdown(
    """
    <div style="background: linear-gradient(135deg, #212121 0%, #424242 100%); 
                padding: 2rem; border-radius: 10px; color: white;">
        <h3 style="color: #ffd700; margin-top: 0;">🏆 Streamlit 1.55.0 で実現する F1 Analytics</h3>
        <p>
        <strong>Dynamic Containers:</strong> リアルタイムでレースデータを管理<br>
        <strong>Widget Binding:</strong> チーム間で設定を即座に共有<br>
        <strong>クリック可能な画像:</strong> サーキット情報に直接アクセス<br>
        <strong>詳細メトリクス:</strong> パフォーマンスを明確に可視化<br>
        <strong>最適化テーブル:</strong> 大量のレース結果を効率的に表示<br>
        <strong>リッチUI:</strong> チームカラーやアイコンで直感的に
        </p>
        <p style="margin-bottom: 0; margin-top: 1.5rem;">
        <strong>→ より速く、より効率的に、F1データを分析できます！</strong>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.success(
    """
    🏎️ **これらの機能をあなたのF1アプリでも活用してみてください！**
    
    Streamlit 1.55.0 は、モータースポーツデータ分析を次のレベルへ導きます。
    """,
    icon="🚀"
)
