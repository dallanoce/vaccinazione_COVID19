import matplotlib.pyplot as plt
import glob
import pandas as pd
import os
import numpy as np

COL = ['Somministrazioni', 'Dosi Consegnate', 'Data']


def plotRegions(path, dest_path):
    all_files = glob.glob(path + "/*.csv")

    for x in all_files:
        df = pd.read_csv(x,
                         usecols=COL, header=0)
        filename_w_ext = os.path.basename(x)
        filename, file_extension = os.path.splitext(filename_w_ext)

        df.plot(x='Data', y=['Somministrazioni', 'Dosi Consegnate'], kind='line', title=filename, grid=True,
                xticks=np.arange(len(df['Data'])),
                legend=True, style='.-')
        plt.fill_between(np.arange(len(df['Data'])),df['Somministrazioni'],alpha=0.4)
        plt.savefig(fname=dest_path + filename + '.png')
        #plt.show()

        print(x)