import numpy as np

LINE = 4

INPUT_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_immagine/'
DEST_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'


def convertion(input_path, date, dest_path):
    regions = []
    somministrations = []
    available = []
    percentage = []

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

    result = [list(zipped) for zipped in zip(regions,somministrations,available, percentage)]
    print(result)

    np.savetxt(DEST_PATH + date + '.csv', result,
               delimiter=',', fmt='%s')


convertion(INPUT_PATH, '01_01', DEST_PATH)
