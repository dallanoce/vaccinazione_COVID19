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

        date = df['Data'].copy()

        for k in range(0,len(date)):
            date[x] = date[k].strip("2020-")

        ax = df.plot(x='Data', y=['Somministrazioni', 'Dosi Consegnate'], kind='line', title=filename, grid=True,
                xticks=np.arange(len(df['Data'])),  lw = 2, rot = 90,
                legend=True, style='.-')
        ax.set_xlabel("Data")
        ax.set_ylabel("Dosi")

        for i, txt in enumerate(df['Somministrazioni']):
            plt.text(i - 0.3, txt, txt)

        for i, txt in enumerate(df['Dosi Consegnate']):
            plt.text(i - 0.3, txt, txt)

        plt.fill_between(np.arange(len(df['Data'])), df['Somministrazioni'], alpha=0.4)

        plt.savefig(fname=dest_path + filename + '.png',pad_inches = 0.3,bbox_inches= 'tight')
        #plt.show()

        print(x)


"""
DEST_PATH_REGIONS = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni/'
DEST_PATH_GRAFICI = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni_grafici/'

plotRegions(DEST_PATH_REGIONS, DEST_PATH_GRAFICI)
"""
