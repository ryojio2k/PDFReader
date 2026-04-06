# PDF Reader
PDFファイルを読み込んでテキストのみをテキストファイルに出力するサービス

# ファイル内訳
- pdf_reader.py : pdfからテキストを抽出する処理の本体

- pdf_to_csv.py : pdfから抽出したテキストをcsv形式で出力する処理の本体

- gui_pdf_reader.py : 上記2処理をGUIアプリケーション化するためのソースコード

# 環境設定

(Windows準拠 別OSの場合は適宜読み替えてください)

## 仮想環境の作成と起動

  ルートディレクトリで下記を実施し仮想環境を作成し、仮想環境を起動してください。

  (VSCodeで.venvをrequirements.txt指定で作成したほうが手っ取り早いです)
  
  `python -m venv .venv`
  
  ### Windows
  `./.venv/Scripts/activate`

  ### Mac OS
  `source ./.venv/Scripts/activate`

  ### Linux
  `source ./.venv/bin/activate`
  
## モジュールのインストール
  下記を実施し必要なモジュールをインストールしてください。
  
  `pip install -U pip`
  
  `pip install -r requirements.txt`

  VirtualBoxなどのLinux仮想環境の場合は以下を追加で実行ください。
  (tkinterがnot foundになる場合)

  `sudo apt-get install python3-tk`

# 実行

## コマンドラインでの実行
  コマンドラインから下記を実行すると、テキストの抽出を行うことが可能です。
  
  出力ディレクトリおよびファイル名は「PDFファイルのディレクトリ/PDFファイル名称.txt」になります。
  
  `python pdf_reader.py {PDFファイルのパス}`

  また、下記を実行すると、pdfから抽出したテキストをcsv形式で出力することが可能です。

  ただし、半角スペースを区切りとしてカンマで分割しただけなので整合性等は考えていません。

  `python pdf_to_csv.py {PDFファイルのパス}`


# GUIアプリケーション

## 実行
  コマンドラインから下記を実行すると、開発環境上でGUIアプリが開きます。

  `python gui_pdf_reader.py`

## 作成
  コマンドラインから下記を実行することでGUIアプリケーションのexeを作成することが可能です。
  
  `pyinstaller -wF ./gui_pdf_reader.py`
