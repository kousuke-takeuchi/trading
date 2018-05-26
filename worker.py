from datatools import historical
from datatools.chart import double_linechart
from analytics.functions import fabx, predict

# 1. 過去データを取得
data = historical.load_local('USDJPY', '2017', tf='D')
close = data['Close']

# 2. 指標を作成
indices = fabx(close, 2, 2)
predicts = predict(close, indices, 1.0)

# 3. データと指標をグラフに表示
double_linechart(data.index, close, predicts, label1='Close', label2='FA_BX')
