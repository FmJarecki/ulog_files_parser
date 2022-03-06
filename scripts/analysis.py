import matplotlib.pyplot as plt
import pandas as pd


class Analyzer:
    def __init__(self):
        fig = plt.figure()
        fig.suptitle("Drone's trajectory")
        self._ax = fig.add_subplot(111, projection='3d')
        self._ax.set_xlabel('x[m]')
        self._ax.set_ylabel('y[m]')
        self._ax.set_zlabel('z[m]')

    def add_scatter(self, df: pd.DataFrame, label: str):
        self._ax.scatter(df.x, df.y, df.z, label=label)

    def show(self):
        self._ax.legend()
        plt.show()
