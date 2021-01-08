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

        daily = []

        for j in range(1,len(df['Somministrazioni'])):
            daily.append(df.at[j,'Somministrazioni'] - df.at[j-1,'Somministrazioni'])
        print(daily)
        daily.insert(0,df.at[0,'Somministrazioni'])

        for k in range(0,len(date)):
            date[x] = date[k].strip("2020-")

        ax = df.plot(x='Data', y=['Somministrazioni', 'Dosi Consegnate'], kind='line', title=filename, grid=True,
                xticks=np.arange(len(df['Data'])),  lw = 2, rot = 90,
                 style='.-')
        ax.set_xlabel("Data (YYYY-MM-DD)")
        ax.set_ylabel("Dosi")
        plt.xlim(0,len(df['Data']))

        for i, txt in enumerate(df['Somministrazioni']):
            plt.text(i - 0.3, txt, txt)

        for i, txt in enumerate(df['Dosi Consegnate']):
            plt.text(i - 0.3, txt, txt)

        for i, txt in enumerate(daily):
            plt.text(i - 0.22, txt, txt,color='#3b4d8a')

        plt.fill_between(np.arange(len(df['Data'])), df['Somministrazioni'], alpha=0.4,label='_nolegend_')

        plt.bar(np.arange(len(df['Data'])),daily,width=0.55,color = '#3b4d8a')
        plt.legend(['Somministrazioni', 'Dosi Consegnate','Somministrazioni giornaliere'])

        plt.savefig(fname=dest_path + filename + '.png',pad_inches = 0.3,bbox_inches= 'tight')
        #plt.show()

        print(x)


"""
DEST_PATH_REGIONS = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni/'
DEST_PATH_GRAFICI = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni_grafici/'

plotRegions(DEST_PATH_REGIONS, DEST_PATH_GRAFICI)
"""
