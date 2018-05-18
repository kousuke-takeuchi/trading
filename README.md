システムトレーディング
==================

## Data Tools API

【未完成】FXヒストリカルデータのローカルダウンロード/ロード

```python
from datatools import historical

# ダウンロード
historical.download_local(path='.data')
# ローカルデータの読み込み
data = historical.load_local(path='.data')
```

みん株の指標取得

```python
from datatools import minkabu

calendar = minkabu.fetch()
for item in calendar:
  print(item)

#  日付: 2018-05-18
#  指標一覧:
#    発表時間: 08:30
#    指標: 日本・消費者物価指数(前年比/前年比)
#    重要度: 3
#    前回変動幅: +1.5pips
#
#    発表時間: 15:00
#    指標: ドイツ・生産者物価指数(前月比/前年比)
#    重要度: 2
#    前回変動幅: -2.4pips
#
#    発表時間: 15:00
#    指標: ドイツ・卸売物価指数(前月比/前年比)
#    重要度: 2
#    前回変動幅: -1.9pips
#
#    発表時間: 17:00
#    指標: ユーロ・経常収支(季調前/季調済)
#    重要度: 2
#    前回変動幅: +1.7pips
#
#    発表時間: 18:00
#    指標: ユーロ・貿易収支(季調前/季調済)
#    重要度: 2
#    前回変動幅: -2.9pips
#
#    発表時間: 21:30
#    指標: カナダ・小売売上高(前月比/前月比)
#    重要度: 3
#    前回変動幅: -0.9pips
#
#    発表時間: 21:30
#    指標: カナダ・消費者物価指数(前月比/前年比)
#    重要度: 3
#    前回変動幅: -0.9pips
```
