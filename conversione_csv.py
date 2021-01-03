import numpy as np
import datetime
from PIL import Image
import pytesseract
from scraping import scraping

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'

LINE = 4

INPUT_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_immagine/'
DEST_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'

POPOLAZIONE = ['Popolazione', '1305770', '556934', '1924701', '5785861', '4467118', '1211357', '5865544', '1543127',
               '10103969', '1518400', '302265', '520891', '538223', '4341375', '4008296', '1630474', '4968410',
               '3722729', '880285', '125501', '4907704']
LINK = "https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9"


def extractText(input_path, date):
    text = pytesseract.image_to_string(Image.open(input_path + date + '.PNG'))
    print(text)


def convertion(date, dest_path):
    total_somministrations = 0
    total_available = 0
    total_population = 0

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
    print(copertura)
    print(copertura_dosi)

    regions.append("Totale")
    somministrations.append(total_somministrations)
    available.append(total_available)
    percentage.append(str(round(total_somministrations / total_available * 100, 3)) + '%')
    POPOLAZIONE.append(total_population)
    copertura.append(str(round(total_somministrations / total_population * 100, 3)) + '%')
    copertura_dosi.append(str(round(total_available / total_population * 100, 3)) + '%')

    print("\n")
    result = [list(zipped) for zipped in
              zip(regions, somministrations, available, percentage, POPOLAZIONE, copertura, copertura_dosi, data)]
    print(result)

    np.savetxt(dest_path + str(datetime.date(2020, int(month), int(day))) + '.csv', result,
               delimiter=',', fmt='%s')


convertion('03_01', DEST_PATH)

# extractText(INPUT_PATH,'01_01')
