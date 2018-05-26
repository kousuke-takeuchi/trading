import numpy as np
import pandas
import matplotlib.pyplot as plt
# from mpl_finance import candlestick2_ohlc, volume_overlay
import matplotlib.cm as cm
# %matplotlib inline


def convert_time64(data):
    data_frame = data[["Open","Close","High","Low"]]
    times = pandas.DataFrame(np.array(data.index.to_pydatetime(), dtype=np.datetime64))
    data_frame["Time"] = times.values.astype("float")
    return data_frame

def preview_candlestick(data):
    fig = plt.figure(figsize=(9, 6))
    ax = plt.subplot(1, 1, 1)
    candlestick2_ohlc(ax, data["Open"], data["High"], data["Low"], data["Close"], width=0.5, colorup="b", colordown="r")

    ax.set_xticklabels(data.index.date)
    ax.set_xlim([0, data.shape[0]])
    ax.set_ylabel("Price")

    plt.show()

def double_linechart(x, y1, y2, label1='', label2=''):
    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ln1 = ax1.plot(x, y1, 'C0', label=label1)

    ax2 = ax1.twinx()
    ln2 = ax2.plot(x, y2, 'C1', label=label2)

    h1, l1 = ax1.get_legend_handles_labels()
    h2, l2 = ax2.get_legend_handles_labels()
    ax1.legend(h1+h2, l1+l2, loc='lower right')

    ax1.set_xlabel('t')
    ax1.set_ylabel(label1)
    ax1.grid(True)
    ax2.set_ylabel(label2)

    plt.show()

if __name__ == '__main__':
    from historical import load_local
    data = load_local('EURUSD', '2017', tf='D')
    preview_candlestick(data[:50])
