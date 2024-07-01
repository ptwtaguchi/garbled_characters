# Webサイトの文字化けテスト
このプロジェクトは、Python、Pytest、およびPlaywrightを使用してWebサイトのテストを行い、AzureのAIを利用して文字化けを検出するためのツールです。

## 概要
１． Playwrightを使用してWebサイトのスクリーンショットを取得します。  
２． Azure Computer Vision APIを使用してスクリーンショットからテキストを抽出します。  
３． 抽出したテキストに文字化けがないかを確認します。  

## ディレクトリ構造

```
project_root/
│  
├── src/  
│　　├── init.py  
│　　├── take_screenshot.py  
│　　└── azure_ocr.py  
│  
├── tests/  
│　　├── init.py  
│　　└── test_website.py  
│  
├── screenshots/  
│　　└── screenshot.png  
│  
├── requirements.txt  
└── README.md  
```

## セットアップ
### １． リポジトリのクローン
ターミナルで以下のコマンドを実行してリポジトリをクローンし、ディレクトリを移動します。

```
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

### ２． 必要なライブラリのインストール
ターミナルで以下のコマンドを実行して必要なライブラリをインストールします。

```
pip install -r requirements.txt
playwright install
```

### ３． Azure Cognitive Servicesのセットアップ
プロジェクトのルートディレクトリに.envファイルを作成し、以下の内容を記述します。

```
AZURE_SUBSCRIPTION_KEY=your_azure_subscription_key
AZURE_ENDPOINT=your_azure_endpoint
```

## 使用方法
### １． スクリーンショットの取得
以下のコマンドを実行して、指定したURLのスクリーンショットを取得します。

```
python src/take_screenshot.py
```

### ２． 文字化けの検出
以下のコマンドを実行して、取得したスクリーンショットを元に文字化けがないかを確認します。

```
python src/azure_ocr.py
```

### ３． テストの実行
Pytestを使用して自動化されたテストを実行します。以下のコマンドを実行します。

```
pytest
```
