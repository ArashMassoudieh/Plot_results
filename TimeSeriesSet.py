from TimeSeries import TimeSeries
from typing import List
import matplotlib.pyplot as plt
import pandas as pd


class TimeSeriesSet:
    Time_series = []

    def plot(self, filename, xtitle="", ytitle=""):
        plt.plot(self.Time_series[0].time, self.Time_series[0].value)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()

    def readfromfile(self, filename):
        with open(filename, 'rt') as csvfile:
            raw_data = pd.read_csv(csvfile, delimiter='\t')
            s = raw_data.iloc[1:, :]
            print(s.shape)
            print(s.shape[0])
            print(s.shape[1])
            print(s)
            for i in range(0, int(s.shape[1] / 2)):
                print(i)
                TS = TimeSeries();
                TS.time = raw_data.iloc[1:, i * 2]
                TS.values = raw_data.iloc[1:, i * 2 + 1]
                self.Time_series.append(TS)
