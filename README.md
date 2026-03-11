# streamlit-update-demo

Streamlit のアップデート検証デモを、バージョンごとのフォルダで管理するリポジトリです。

note 記事や検証メモと対応づけやすく、読者が迷いにくく、Git に不慣れでも扱いやすい構成にしています。

## Structure

```text
streamlit-update-demo/
|-- v1_55/
|-- v1_56/
`-- v1_57/
```

## Versions

- [v1_55/README.md](v1_55/README.md)
  - Streamlit 1.55.0 の新機能デモ
- [v1_56/README.md](v1_56/README.md)
  - 追加予定
- [v1_57/README.md](v1_57/README.md)
  - 追加予定

## How to run

まずはルートから最新デモを起動できます。

```bash
pip install -r v1_55/requirements.txt
streamlit run app.py
```

特定バージョンだけ直接動かしたいときは、そのフォルダの app.py を指定します。

```bash
pip install -r v1_55/requirements.txt
streamlit run v1_55/app.py
```

## Why this layout

- note 記事やリリース記事と対応づけやすい
- バージョン差分をフォルダ単位で追いやすい
- 読者が今どの版を見ているか分かりやすい
- 将来の v1_56 や v1_57 を追加しやすい