import conversione_csv
import regions_elaboration
import plot_regions

DATE = '04_01'

INPUT_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero_immagine/'
DEST_PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'
DEST_PATH_GROUP = 'E:/vaccinazione_COVID19/andamento_giornaliero_gruppi/'
DEST_PATH_CATEGORY = 'E:/vaccinazione_COVID19/andamento_giornaliero_categorie/'

PATH = 'E:/vaccinazione_COVID19/andamento_giornaliero/'
DEST_PATH_REGIONS = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni/'
DEST_PATH_GRAFICI = 'E:/vaccinazione_COVID19/andamento_giornaliero_regioni_grafici/'

LINK = "https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9"


def main():
    print("CSV loading...")
    conversione_csv.convertion(DATE, LINK, DEST_PATH, latest=True)

    conversione_csv.convertionGroup(DATE, LINK, DEST_PATH_GROUP, latest=True)

    conversione_csv.convertionCategory(DATE, LINK, DEST_PATH_CATEGORY, latest=True)
    print("Done.")

    print("Regions creation..")
    regions_elaboration.regionsElaborations(PATH, DEST_PATH_REGIONS)
    print("Done.")

    print("Plotting regions..")
    plot_regions.plotRegions(DEST_PATH_REGIONS, DEST_PATH_GRAFICI)
    print("Done.")


if __name__ == "__main__":
    main()
