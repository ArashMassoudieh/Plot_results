import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class TimeSeries:
    time = np.array([], dtype=float)
    value = np.array([], dtype=float)

    def plot(self, filename, xtitle="", ytitle=""):
        plt.plot(self.time, self.value)
        plt.xlabel(xtitle)
        plt.ylabel(ytitle)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()

    def readfromfile(self, filename):
        import csv
        with open(filename, 'rt') as csvfile:
            raw_data = pd.read_csv(csvfile,delimiter="\t")
            print(raw_data.iloc[:,:])
            self.time = raw_data.iloc[1:,0]
            self.value = raw_data.iloc[1:,1]
            print(self.time)
            print(self.value)