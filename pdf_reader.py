import os
import sys
import datetime
import c_logger
from pypdf import PdfReader

def read(target_path, window=None, output=None):
  """PDFファイルのテキストをファイルに抽出する

  Args:
      targetpath (str): 出力対象となるPDFファイルのパス
      window (_type_, optional): TkEasyGUIのWindowオブジェクト. Defaults to None.
      output (_type_, optional): TkEasyGUIのOutputオブジェクト. Defaults to None.

  Returns:
      str: 終了告知ダイアログに表示する文字列
  Exports:
      target_filename.txt:  テキストのみ抽出したテキストファイル
  """

  # ロガー準備
  str_dt = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
  log_file_path = f"./log/log_pdf_reader_{str_dt}.txt"
  logger = c_logger.logger()
  logger.start(log_file_path, window, output)

  logger.print(f"target_path:{target_path}")

  # ファイル存在確認
  if not os.path.isfile(target_path):
    logger.print(f"targetpath {target_path} is not Exists.")
    sys.exit()
  
  # 入力ファイルパスから出力ファイルパスを生成する
  export_dir = os.path.dirname(target_path)
  export_file_name = os.path.splitext(os.path.basename(target_path))[0] + ".txt"
  export_path = os.path.join(export_dir,export_file_name)
  logger.print(f"export_path:{export_path}")

  # 出力先ファイルをwriteで開く
  with open(export_path, "w", encoding="utf-8") as ex:
    # pdfファイル読み込み
    reader = PdfReader(target_path)

    # ページ数
    number_of_pages = len(reader.pages)
    logger.print(f"number of pages:{number_of_pages}")
    logger.print("-----")

    # pdfのページを1枚ずつ処理
    for i,page in enumerate(reader.pages):
      # ページ数
      text = f"page:{i+1}/{number_of_pages}"
      print(text, file=ex)
      logger.print(text)
      # PDF本文
      document = page.extract_text()
      print(document, file=ex)
      logger.print(document)
      # ページ区切り改行
      print("\n", file=ex)
      logger.print("\n")
  
  return f"PDFファイルのテキストを抽出しました\n{export_path}"

# コマンドライン実行
if __name__ == "__main__":
  if (len(sys.argv)) == 2:
    read(sys.argv[1])
  else:
    print("python pdf_reader.py [target_path]")
    sys.exit()