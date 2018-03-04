from TimeSeries import TimeSeries
from typing import List
import matplotlib.pyplot


class TimeSeriesSet:
    Time_series = List[TimeSeries]

    def plot(self):
        for ts in self.Time_series:
            matplotlib.pyplot.plot(ts.time, ts.value)
