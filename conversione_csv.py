import numpy as np
import datetime
from scraping import scraping, scrapingGroup, scrapingCategory

DATE = '03_01'

LINE = 4

INPUT_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_immagine/'
DEST_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'
DEST_PATH_GROUP = 'E:/vaccinazione_COVID19/andamento_giornaliero_gruppi/'
DEST_PATH_CATEGORY = 'E:/vaccinazione_COVID19/andamento_giornaliero_categorie/'

POPOLAZIONE = ['Popolazione', '1305770', '556934', '1924701', '5785861', '4467118', '1211357', '5865544', '1543127',
               '10103969', '1518400', '302265', '520891', '538223', '4341375', '4008296', '1630474', '4968410',
               '3722729', '880285', '125501', '4907704']  # dati ISTAT 12/2019
FASCE_ETA = ['Fasce Età', '16-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']

CATEGORIE = ['Categorie', 'Operatori Sanitari', 'Personale non Sanitario', 'Ospiti RSA']

PERSONALE_SANITARIO = ['Personale Sanitario', '10296', '4695', '13183', '31503', '40502', '11905', '30589', '10752',
                       '59164', '13019', '2105', '5530', '5226', '36596', '25601', '15403', '30801', '35651', '8164',
                       '1364', '39443']  # dati ISTAT 2017

LINK = "https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9"


def convertion(date, dest_path, latest=False):
    total_somministrations = 0
    total_available = 0
    total_population = 0
    total_health = 0

    day, month = date.split(sep="_")

    data = [str(datetime.date(2020, int(month), int(day)))] * (len(POPOLAZIONE))
    data.insert(0, "Data")

    regions, somministrations, available, percentage = scraping(LINK)

    copertura = []
    copertura.append('Copertura')

    copertura_dosi = []
    copertura_dosi.append(('Copertura Teorica'))

    for x in range(1, len(POPOLAZIONE)):
        copertura.append(str(round(int(somministrations[x].replace('.', '')) / int(POPOLAZIONE[x]) * 100, 3)) + '%')
        copertura_dosi.append(str(round(int(available[x].replace('.', '')) / int(POPOLAZIONE[x]) * 100, 3)) + '%')

        total_somministrations += int(somministrations[x].replace('.', ''))
        total_available += int(available[x].replace('.', ''))
        total_population += int(POPOLAZIONE[x])
        total_health += int(PERSONALE_SANITARIO[x])
    print(copertura)
    print(copertura_dosi)

    regions.append("Totale")
    somministrations.append(total_somministrations)
    available.append(total_available)
    percentage.append(str(round(total_somministrations / total_available * 100, 3)) + '%')
    POPOLAZIONE.append(total_population)
    PERSONALE_SANITARIO.append(total_health)
    copertura.append(str(round(total_somministrations / total_population * 100, 3)) + '%')
    copertura_dosi.append(str(round(total_available / total_population * 100, 3)) + '%')

    print("\n")
    result = [list(zipped) for zipped in
              zip(regions, somministrations, available, percentage, POPOLAZIONE, PERSONALE_SANITARIO, copertura,
                  copertura_dosi, data)]
    print(result)

    np.savetxt(dest_path + str(datetime.date(2020, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')

    if latest:
        np.savetxt(dest_path + 'latest' + '.csv', result,
                   delimiter=',', fmt='%s')


def convertionGroup(date, dest_path, latest=False):
    day, month = date.split(sep="_")
    data = scrapingGroup(LINK)

    date = [str(datetime.date(2020, int(month), int(day)))] * (len(POPOLAZIONE))
    date.insert(0, "Data")

    result = [list(zipped) for zipped in
              zip(np.array(FASCE_ETA), np.array(data), np.array(date))]

    print(result)

    np.savetxt(dest_path + str(datetime.date(2020, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')

    if latest:
        np.savetxt(dest_path + 'latest' + '.csv', result,
                   delimiter=',', fmt='%s')


def convertionCategory(date, dest_path, latest=False):
    day, month = date.split(sep="_")
    data = scrapingCategory(LINK)

    date = [str(datetime.date(2020, int(month), int(day)))] * (len(POPOLAZIONE))
    date.insert(0, "Data")

    result = [list(zipped) for zipped in
              zip(np.array(CATEGORIE), np.array(data), np.array(date))]

    print(result)

    np.savetxt(dest_path + str(datetime.date(2020, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')

    if latest:
        np.savetxt(dest_path + 'latest' + '.csv', result,
                   delimiter=',', fmt='%s')


convertion(DATE, DEST_PATH, latest=True)

convertionGroup(DATE, DEST_PATH_GROUP, latest=True)

convertionCategory(DATE, DEST_PATH_CATEGORY, latest=True)
