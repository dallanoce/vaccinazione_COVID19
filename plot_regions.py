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

        plt.savefig(fname=dest_path+filename+'.png')

        print(x)


PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni/'
DEST_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni_grafici/'

plotRegions(PATH, DEST_PATH)
