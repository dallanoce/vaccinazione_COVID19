import numpy as np
import datetime

LINE = 4

INPUT_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_immagine/'
DEST_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'

POPOLAZIONE = ['Popolazione','1305770', '556934', '1924701', '5785861', '4467118', '1211357', '5865544', '1543127', '10103969', '1518400', '302265', '520891', '538223', '4341375', '4008296', '1630474', '4968410', '3722729', '880285', '125501','4907704']


def convertion(input_path, date, dest_path):
    regions = []
    somministrations = []
    available = []
    percentage = []

    day , month = date.split(sep="_")

    data = [str(datetime.date(2020, int(month), int(day)))] * (len(POPOLAZIONE)-1)
    data.insert(0,"Data")

    with open(input_path + date + '.txt') as fp:
        line = fp.readline()
        cnt = 0
        while line:
            if cnt == 0:
                regions.append(line.rstrip())
                cnt += 1
            elif cnt == 1:
                somministrations.append(line.rstrip())
                cnt += 1
            elif cnt == 2:
                available.append(line.rstrip())
                cnt += 1
            elif cnt == 3:
                percentage.append(line.rstrip())
                cnt = 0
            line = fp.readline()

    print(regions)
    print(somministrations)
    print(available)
    print(percentage)

    copertura = []
    copertura.append('Copertura')

    for x in range(1,len(POPOLAZIONE)):
        copertura.append( str(round(int(somministrations[x].replace('.',''))/int(POPOLAZIONE[x])*100,3))+'%')

    print(copertura)

    print("\n")
    result = [list(zipped) for zipped in zip(regions, somministrations, available, percentage,POPOLAZIONE,copertura,data)]
    print(result)

    np.savetxt(DEST_PATH + str(datetime.date(2020, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')


convertion(INPUT_PATH, '01_01', DEST_PATH)
