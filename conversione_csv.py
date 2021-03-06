import numpy as np
import datetime
from scraping import scraping, scrapingGroup, scrapingCategory

POPOLAZIONE = ['Popolazione', '1305770', '556934', '1924701', '5785861', '4467118', '1211357', '5865544', '1543127',
               '10103969', '1518400', '302265', '520891', '538223', '4341375', '4008296', '1630474', '4968410',
               '3722729', '880285', '125501', '4907704']  # dati ISTAT 12/2019
FASCE_ETA = ['Fasce Età', '16-19', '20-29', '30-39', '40-49', '50-59', '60-69', '70-79', '80-89', '90+']

CATEGORIE = ['Categorie', 'Operatori Sanitari', 'Personale non Sanitario', 'Ospiti RSA']

PERSONALE_SANITARIO = ['Personale Sanitario', '10296', '4695', '13183', '31503', '40502', '11905', '30589', '10752',
                       '59164', '13019', '2105', '5530', '5226', '36596', '25601', '15403', '30801', '35651', '8164',
                       '1364', '39443']  # dati ISTAT 2017


def convertion(date, link, dest_path, latest=False):
    total_somministrations = 0
    total_available = 0
    total_population = 0
    total_health = 0

    day, month = date.split(sep="_")

    data = [str(datetime.date(2021, int(month), int(day)))] * (len(POPOLAZIONE))
    data.insert(0, "Data")

    regions, administration, available, percentage = scraping(link)

    zipped = zip(regions, administration, available, percentage)
    sort = sorted(zipped, key = lambda x: x[0])
    regions = [regions for (regions, administration, available, percentage) in sort]
    administration = [administration for (regions, administration, available, percentage) in sort]
    available = [available for (regions, administration, available, percentage) in sort]
    percentage = [percentage for (regions, administration, available, percentage) in sort]

    copertura = []
    copertura.append('Copertura')

    copertura_dosi = []
    copertura_dosi.append(('Copertura Teorica'))

    for x in range(1, len(POPOLAZIONE)):
        copertura.append(str(round(int(administration[x].replace('.', '')) / int(POPOLAZIONE[x]) * 100, 3)) + '%')
        copertura_dosi.append(str(round(int(available[x].replace('.', '')) / int(POPOLAZIONE[x]) * 100, 3)) + '%')

        total_somministrations += int(administration[x].replace('.', ''))
        total_available += int(available[x].replace('.', ''))
        total_population += int(POPOLAZIONE[x])
        total_health += int(PERSONALE_SANITARIO[x])
    print(copertura)
    print(copertura_dosi)

    regions.append("Totale")
    administration.append(total_somministrations)
    available.append(total_available)
    percentage.append(str(round(total_somministrations / total_available * 100, 3)) + '%')
    POPOLAZIONE.append(total_population)
    PERSONALE_SANITARIO.append(total_health)
    copertura.append(str(round(total_somministrations / total_population * 100, 3)) + '%')
    copertura_dosi.append(str(round(total_available / total_population * 100, 3)) + '%')

    print("\n")
    result = [list(zipped) for zipped in
              zip(regions, administration, available, percentage, POPOLAZIONE, PERSONALE_SANITARIO, copertura,
                  copertura_dosi, data)]
    print(result)

    np.savetxt(dest_path + str(datetime.date(2021, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')

    if latest:
        np.savetxt(dest_path + 'latest' + '.csv', result,
                   delimiter=',', fmt='%s')


def convertionGroup(date, link, dest_path, latest=False):
    day, month = date.split(sep="_")
    data = scrapingGroup(link)

    date = [str(datetime.date(2021, int(month), int(day)))] * (len(POPOLAZIONE))
    date.insert(0, "Data")

    result = [list(zipped) for zipped in
              zip(np.array(FASCE_ETA), np.array(data), np.array(date))]

    print(result)

    np.savetxt(dest_path + str(datetime.date(2021, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')

    if latest:
        np.savetxt(dest_path + 'latest' + '.csv', result,
                   delimiter=',', fmt='%s')


def convertionCategory(date, link, dest_path, latest=False):
    day, month = date.split(sep="_")
    data = scrapingCategory(link)

    date = [str(datetime.date(2021, int(month), int(day)))] * (len(POPOLAZIONE))
    date.insert(0, "Data")

    result = [list(zipped) for zipped in
              zip(np.array(CATEGORIE), np.array(data), np.array(date))]

    print(result)

    np.savetxt(dest_path + str(datetime.date(2021, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')

    if latest:
        np.savetxt(dest_path + 'latest' + '.csv', result,
                   delimiter=',', fmt='%s')
