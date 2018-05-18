import numpy as np
import pandas
import matplotlib.pyplot as plt
from mpl_finance import candlestick2_ohlc, volume_overlay

from historical import load_local


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

if __name__ == '__main__':
    data = load_local('EURUSD', '2017', tf='D')
    preview_candlestick(data[:50])
