# git-sample2022
勉強会用のリポジトリ
# クローラーもどき

## 概要
Playwrightを使ったクローラーもどきです。

## 必要要件
- Python3.7以上

## 環境構築
1. 仮想環境構築
```[bash]
python -m venv [venv-name]
```
1. パッケージの導入
```[bash]
pip install -r requirements.txt
```
1. Playwrightのインストール
```[bash]
playwright install
playwright install-deps
```

## 実行方法
```
python crawl.py
```