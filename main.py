import conversione_csv
import regions_elaboration
import plot_regions
import config


def main():
    print("CSV loading...")
    conversione_csv.convertion(config.DATE, config.LINK, config.DEST_PATH, latest=True)

    conversione_csv.convertionGroup(config.DATE, config.LINK, config.DEST_PATH_GROUP, latest=True)

    conversione_csv.convertionCategory(config.DATE, config.LINK, config.DEST_PATH_CATEGORY, latest=True)
    print("Done.")

    print("Regions creation..")
    regions_elaboration.regionsElaborations(config.PATH, config.DEST_PATH_REGIONS)
    print("Done.")

    print("Plotting regions..")
    plot_regions.plotRegions(config.DEST_PATH_REGIONS, config.DEST_PATH_GRAFICI)
    print("Done.")


if __name__ == "__main__":
    main()
