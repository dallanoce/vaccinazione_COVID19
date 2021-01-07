import glob
import numpy as np
import pandas as pd

COL = ['Regioni', 'Somministrazioni', 'Dosi Consegnate', 'Percentuale', 'Popolazione', 'Copertura',
       'Copertura Teorica', 'Data']

LINK = "https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9"


def regionsElaborations(path, dest_path):
    all_files = glob.glob(path + "/2021*.csv")

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
