import matplotlib.pyplot as plt
import numpy as np

from tkinter import filedialog
from tkinter import *
import os

from TimeSeries import TimeSeries
from TimeSeriesSet import TimeSeriesSet
os.chdir("/home/arash/Projects/Upscaling_outputs")
root = Tk()
root.filename = filedialog.askopenfilename(initialdir="/home/arash/Projects/Upscaling_outputs", title="Select file",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))
print(root.filename)

T = TimeSeriesSet()
#T.time = np.arange(0.0, 2.0, 0.01)
#T.value = 1 + np.sin(2*np.pi*T.time)


T.readfromfile(root.filename)

T.plot("output.png")
