# Streamlit 1.55.0 新機能デモアプリ

このフォルダでは **Streamlit 1.55.0** で追加された新機能を体感できるデモアプリを提供しています。

## 🚀 セットアップ

依存パッケージをインストール:

```bash
pip install -r v1_55/requirements.txt
```

デモアプリを起動:

```bash
streamlit run v1_55/app.py
```

または v1_55 フォルダへ移動して実行:

```bash
cd v1_55
pip install -r requirements.txt
streamlit run app.py
```

## ✨ 主な新機能

### 1. 🍿 Dynamic Containers
- `st.tabs`, `st.popover`, `st.expander` に `on_change` パラメータが追加
- コンテナの開閉時にアプリを再実行可能
- `key` を設定することでプログラムから開閉を制御可能
- `.open` プロパティで現在の開閉状態を取得

### 2. 🖇️ Widget Binding
- ほとんどのウィジェットに `bind` パラメータが追加
- `bind="query-params"` でウィジェットとクエリパラメータを自動同期
- URL を共有することで同じ状態を再現可能

### 3. 🔗 クリック可能な画像
- `st.image` に `link` パラメータが追加
- 画像をクリック可能なリンクにできる

### 4. 🥷 隠しページ
- `st.Page` に `visibility` パラメータが追加
- `visibility="hidden"` でナビゲーションに表示せずにルーティング可能

### 5. 🎨 Markdown CSS カラー
- Markdown で任意の CSS カラーをサポート
- 文字色と背景色の両方が使用可能

### 6. 📐 Metric 説明文
- `st.metric` に `delta_description` パラメータが追加
- デルタ値に説明文を追加可能

### 7. 🏓 Table サイズ指定
- `st.table` に `height` と `width` パラメータが追加
- テーブルのサイズを明示的に指定可能

### 8. 🏄‍♂️ Multiselect 全選択
- `st.multiselect` でワンクリックでの全選択・全解除が可能

## 📄 ページ構成

- **概要 (overview.py)**: 1.55.0 の主要機能を 1 ページで確認
- **Dynamic Containers**: expander と popover の開閉状態と再実行を体験
- **Widget Binding**: ウィジェットとクエリパラメータの自動同期を体験
- **その他の新機能**: 画像リンク、Metric説明、Table サイズなどを体験
- **隠しページ**: ナビゲーションに表示されないページへのアクセス

## 🔧 必要要件

- Python 3.12 以降
- Streamlit 1.55.0

## 📚 参考リンク

- [Streamlit 1.55.0 リリースノート](https://docs.streamlit.io/develop/quick-reference/release-notes)

```text
v1_55/
|-- app.py
|-- pages/
|   |-- overview.py
|   |-- dynamic_containers.py
|   `-- hidden_route.py
`-- requirements.txt
```

## Notes

- このデモは Streamlit 1.55.0 固有の API を使っています。
- 1.54.x 以前では visibility、bind、link などの引数が使えず、起動時エラーになります。