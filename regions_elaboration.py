import glob
import numpy as np
import pandas as pd

PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'
DEST_PATH_REGIONS = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni/'

COL = ['Regioni', 'Somministrazioni', 'Dosi Consegnate', 'Percentuale', 'Popolazione', 'Copertura',
       'Copertura Teorica', 'Data']


def regionsElaborations(path, dest_path):
    all_files = glob.glob(path + "/2020*.csv")

    df = pd.read_csv(all_files[0],
                     usecols=['Regioni'], header=0)

    regions = df.Regioni

    for x in range(0, len(regions)):
        current_region = []
        current_region.insert(0, np.array(COL))
        for filename in all_files:
            region = regions[x]
            df = pd.read_csv(filename,
                             usecols=COL, header=0)

            current_region = np.concatenate([current_region, df.loc[df['Regioni'] == region].to_numpy()])

        print(current_region)

        np.savetxt(dest_path + region + '.csv', np.array(current_region),
                   delimiter=',', fmt='%s')


regionsElaborations(PATH, DEST_PATH_REGIONS)
