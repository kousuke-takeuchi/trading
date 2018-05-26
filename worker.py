from datatools import historical
from analytics.functions import fabx

# 1. 過去データを取得
data = historical.load_local('USDJPY', '2017', tf='D')
results = fabx(data['Close'], 4, 10)

import matplotlib.pyplot as plt
import matplotlib.cm as cm

import numpy as np
# %matplotlib inline

fig = plt.figure()
ax1 = fig.add_subplot(111)
t = data.index
ln1=ax1.plot(t, data['Close'], 'C0', label=r'Close')

ax2 = ax1.twinx()
ln2=ax2.plot(t, results, 'C1', label=r'FA_X')

h1, l1 = ax1.get_legend_handles_labels()
h2, l2 = ax2.get_legend_handles_labels()
ax1.legend(h1+h2, l1+l2, loc='lower right')

ax1.set_xlabel('t')
ax1.set_ylabel(r'Close')
ax1.grid(True)
ax2.set_ylabel(r'FA_X')

plt.show()
