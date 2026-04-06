import os
import json
import TkEasyGUI as teg
import pdf_reader

# 入力フレーム
frame1 = teg.Frame('設定',
  [
    [
      teg.Text('対象PDF')
    ],
    [
      teg.InputText(key='-TARGETPATH-', size=(100, 1)),
      teg.FileBrowse(target_key='-TARGETPATH-', file_types=(("PDF File",".pdf"),))
    ],
    [
      teg.Submit(button_text='実行', key='button_execute')
    ]
  ]
)

# 出力フレーム
frame2 = teg.Frame('ログ出力',
  [
    [
      teg.Output(key='-OUTPUT-', size=(100, 20), autoscroll=True, disabled=True),
    ],
  ]
)

# レイアウト
layout = [
  [
    frame1
  ],
  [
    frame2
  ],
]

# Window生成
window = teg.Window('PDF Reader', layout)

# GUI表示実行部分
while window.is_alive():
  # ウインドウ表示
  event, values = window.read()

  # クローズボタン
  if event is None:
    print('exit')
    break

  # ボタンが押された場合
  if event == 'button_execute':
    target_path = str(values['-TARGETPATH-'])
    output = window['-OUTPUT-']

    str_finished = pdf_reader.read(target_path, window, output)

    teg.popup_info(str_finished, "PDF Reader")

window.close()
