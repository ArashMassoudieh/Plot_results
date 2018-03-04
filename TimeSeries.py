import matplotlib.pyplot as plt


class TimeSeries:
    time = []
    value = []

    def plot(self):
        plt.plot(self.time, self.value)

    def readfromfile(self, filename):
        import csv
        with open(filename, 'rt') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                print(row)
                print(type(row))
                print(row[0])
                print(type(row[0]))
                if len(row) == 2:
                    self.time.append(float(row[0]))
                    self.value.append(float(row[1]))
