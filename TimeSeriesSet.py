from TimeSeries import TimeSeries
from typing import List
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


class TimeSeriesSet:
    Time_series = []

    def plot(self, filename, xtitle="", ytitle=""):
        for TS in self.Time_series:
            if (TS.time.shape == TS.value.shape):
                plt.plot(TS.time, TS.value)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()

    def readfromfile(self, filename):
        c = []
        nvars = 0
        with open(filename, 'rt') as csvfile:
            raw_data = pd.DataFrame()
            eof = False
            s = csvfile.readline()
            s = csvfile.readline()
            i = 0
            while eof == False:
                s = csvfile.readline()
                print("s=", s)
                if s == "":
                    eof = True
                    print("eof = ", eof)
                else:
                    c = s.split('\t')
                    print("c=", c)
                if (i == 0):
                    nvars = int((len(c) - 1) / 2)
                    print("nvars = ", nvars)
                    for i in range(0, nvars):
                        self.Time_series.append(TimeSeries())
                for i in range(0, nvars):
                    self.Time_series[i].time = np.append(self.Time_series[i].time, np.array(float(c[i * 2])))
                    self.Time_series[i].value = np.append(self.Time_series[i].value, np.array(float(c[i * 2 + 1])))
                i = i + 1
