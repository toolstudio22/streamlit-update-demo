# Streamlit 1.55.0 Demo App

Streamlit 1.55.0 の新機能を体感できるサンプルアプリです。

リリースノートで追加された機能のうち、UI 上で変化が分かりやすく、共有デモに向いているものをまとめています。

## What this app demonstrates

- Dynamic containers
  - st.expander と st.popover で open/close を state として扱い、on_change で rerun できます。
- Widget binding
  - bind="query-params" により、widget の値を URL と双方向同期できます。
- Clickable images
  - st.image(..., link=...) で画像全体をリンクにできます。
- Hidden pages
  - st.Page(..., visibility="hidden") でナビゲーションに出さずにルーティングできます。
- UI updates
  - st.metric(..., delta_description=...)
  - st.table(..., width=..., height=...)

## Pages

- Overview
  - 1.55.0 の主要機能を 1 ページで確認できます。
- Dynamic Containers
  - expander と popover の open/close state と rerun を体験できます。
- Hidden Route
  - navigation には表示されない page へ直接アクセスできます。

## Requirements

- Python 3.12 以降
- Streamlit 1.55.0

## Local setup

```bash
pip install -r v1_55/requirements.txt
streamlit run v1_55/app.py
```

または v1_55 フォルダへ移動して実行します。

```bash
cd v1_55
pip install -r requirements.txt
streamlit run app.py
```

## Project structure

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