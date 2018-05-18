## Data Tools API

FXヒストリカルデータのローカルダウンロード/ロード

ロード時のTF:TimeFrameは下記で指定可能

+ 分 - 'T'
+ 時 - 'H'
+ 日 - 'D'
+ 週 - 'W'
+ 月 - 'M'

```python
from datatools import historical

# ダウンロード
historical.download_local()

# ローカルデータの読み込み
data = historical.load_local('EURUSD', '2017', tf='W')
# > 2017年のEURUSDデータを週単位で取得
# Time        Open     High     Low      Close
# 2017-01-08  1.05155  1.06214  1.03406  1.05306
# 2017-01-15  1.05284  1.06847  1.04537  1.06425
# 2017-01-22  1.06047  1.07197  1.05793  1.06988
# 2017-01-29  1.07004  1.07747  1.06576  1.06963
# 2017-02-05  1.07204  1.08287  1.06201  1.07825
# 2017-02-12  1.07869  1.07912  1.06076  1.06386
# 2017-02-19  1.06263  1.06792  1.05213  1.06127
```

ローソク足チャートの表示

```python
from datatools import historical, chart

data = historical.load_local('EURUSD', '2017', tf='D')
chart.preview_candlestick(data)
```

![chart](http://res.cloudinary.com/selfolio/image/upload/v1526639731/fig_qrjsky.png)

みん株の指標取得

```python
from datatools import minkabu

calendar = minkabu.fetch()
for item in calendar:
  print(item)
# >
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
