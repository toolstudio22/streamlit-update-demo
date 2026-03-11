"""その他の新機能デモ"""

import pandas as pd
import streamlit as st

st.title("✨ その他の新機能")

st.markdown(
    """
    Streamlit 1.55.0 で追加された、その他の便利な新機能を紹介します。
    """
)

st.divider()

# ========================================
# 1. st.image with link
# ========================================
st.subheader("1️⃣ クリック可能な画像 (st.image with link)")

st.markdown(
    """
    `st.image` に **link** パラメータが追加されました。
    画像をクリックすると、指定した URL に遷移します。
    """
)

col1, col2 = st.columns([3, 2])

with col1:
    st.image(
        "https://images.unsplash.com/photo-1498050108023-c5249f4df085?w=800&q=80",
        caption="クリックして Streamlit 公式サイトへ",
        use_container_width=True,
        link="https://streamlit.io",  # ✨ 画像をクリック可能に
    )

with col2:
    st.info(
        """
        👆 **画像をクリック**してみてください！
        
        Streamlit の公式サイトに遷移します。
        
        ```python
        st.image(
            "image.jpg",
            link="https://example.com"
        )
        ```
        """,
        icon="💡"
    )

st.divider()

# ========================================
# 2. Markdown CSS colors
# ========================================
st.subheader("2️⃣ Markdown で CSS カラーを使用")

st.markdown(
    """
    Markdown で **任意の CSS カラー** が使えるようになりました！
    
    背景色と文字色の両方をサポートしています。
    """
)

st.markdown(
    """
    - <span style="color: #FF6B6B;">赤色のテキスト</span>
    - <span style="color: #4ECDC4;">青緑色のテキスト</span>
    - <span style="color: #FFE66D;">黄色のテキスト</span>
    - <span style="background-color: #FFE66D; color: #000000; padding: 2px 8px;">ハイライト付きテキスト</span>
    - <span style="background-color: #FF6B6B; color: white; padding: 2px 8px;">赤背景の白テキスト</span>
    """,
    unsafe_allow_html=True
)

with st.expander("📝 サンプルコード"):
    st.code(
        """
st.markdown(
    '<span style="color: #FF6B6B;">赤色のテキスト</span>',
    unsafe_allow_html=True
)
        """,
        language="python"
    )

st.divider()

# ========================================
# 3. st.metric with delta_description
# ========================================
st.subheader("3️⃣ st.metric の delta_description")

st.markdown(
    """
    `st.metric` に **delta_description** パラメータが追加され、
    デルタ値に説明文を追加できるようになりました。
    """
)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "売上",
        "¥1,234,567",
        delta="123,456 (+11%)",
        delta_description="前月比",  # ✨ デルタの説明
    )

with col2:
    st.metric(
        "訪問者数",
        "45,678",
        delta="-2,345 (-5%)",
        delta_description="前週比",  # ✨ デルタの説明
        delta_color="inverse",
    )

with col3:
    st.metric(
        "コンバージョン率",
        "3.2%",
        delta="0.5%",
        delta_description="目標値との差",  # ✨ デルタの説明
    )

with st.expander("📝 サンプルコード"):
    st.code(
        """
st.metric(
    "売上",
    "¥1,234,567",
    delta="123,456 (+11%)",
    delta_description="前月比"  # ✨ 新機能
)
        """,
        language="python"
    )

st.divider()

# ========================================
# 4. st.table with height/width
# ========================================
st.subheader("4️⃣ st.table のサイズ指定")

st.markdown(
    """
    `st.table` に **height** と **width** パラメータが追加され、
    テーブルのサイズを明示的に指定できるようになりました。
    """
)

# サンプルデータ
df = pd.DataFrame({
    "商品名": ["ノートPC", "マウス", "キーボード", "モニター", "ヘッドセット", "Webカメラ", "USBハブ", "スタンド"],
    "価格": ["¥120,000", "¥3,500", "¥8,900", "¥35,000", "¥12,000", "¥7,800", "¥2,500", "¥4,500"],
    "在庫": [15, 120, 85, 32, 48, 67, 95, 55],
    "カテゴリ": ["PC", "周辺機器", "周辺機器", "ディスプレイ", "周辺機器", "周辺機器", "周辺機器", "周辺機器"],
})

col1, col2 = st.columns(2)

with col1:
    st.write("**デフォルト (サイズ指定なし)**")
    st.table(df.head(3))

with col2:
    st.write("**height を指定**")
    st.table(df, height=200)  # ✨ 高さを指定

with st.expander("📝 サンプルコード"):
    st.code(
        """
st.table(df, height=200)  # ✨ 高さを指定
st.table(df, width=600)   # ✨ 幅を指定
        """,
        language="python"
    )

st.divider()

# ========================================
# 5. st.multiselect の全選択機能
# ========================================
st.subheader("5️⃣ st.multiselect の全選択機能")

st.markdown(
    """
    `st.multiselect` でドロップダウンを開くと、
    **「すべて選択」** ボタンが表示されるようになりました。
    
    ワンクリックで全選択・全解除ができます！
    """
)

selected_items = st.multiselect(
    "商品を選択してください（ドロップダウンを開いて「すべて選択」を試してみてください）",
    [
        "ノートPC",
        "マウス",
        "キーボード",
        "モニター",
        "ヘッドセット",
        "Webカメラ",
        "USBハブ",
        "スタンド",
        "マウスパッド",
        "ケーブル",
    ],
    default=["ノートPC", "マウス"],
)

if len(selected_items) > 0:
    st.success(f"✅ {len(selected_items)} 個の商品が選択されています: {', '.join(selected_items)}")
else:
    st.info("商品が選択されていません")

st.info(
    """
    💡 **使い方**:
    1. ドロップダウンをクリックして開く
    2. 「すべて選択」ボタンをクリック
    3. すべての項目が一度に選択されます
    """,
    icon="💡"
)

st.divider()

# ========================================
# 6. Page title の Markdown サポート
# ========================================
st.subheader("6️⃣ Page Title の Markdown サポート")

st.markdown(
    """
    `st.Page` のタイトルと `st.navigation` のセクションラベルで
    **Markdown** が使えるようになりました。
    
    これにより、ナビゲーションをより視覚的に表現できます。
    """
)

st.code(
    """
# ナビゲーションでMarkdownを使用
overview = st.Page(
    "pages/overview.py",
    title="**概要** 🏠"  # ✨ Markdown が使える
)

pg = st.navigation({
    "**メインメニュー** 📋": [overview],  # ✨ セクションラベルでも使える
})
    """,
    language="python"
)

st.info(
    "このデモアプリのナビゲーションでも、絵文字や太字などが使われています！",
    icon="👀"
)

st.divider()

# まとめ
st.subheader("🎉 まとめ")

st.success(
    """
    Streamlit 1.55.0 では、これらの新機能により：
    
    - 🎯 **より直感的な UI** が作れる
    - 🔗 **状態の共有** が簡単になった
    - 📊 **データの可視化** がより柔軟に
    - 🎨 **デザインの自由度** が向上
    
    ぜひ、あなたのアプリでも試してみてください！
    """
)
