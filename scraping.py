from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np


def scraping(link):
    driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver.get(link)

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rowHeaders")))
    regions_parent = driver.find_element_by_class_name("rowHeaders")
    # print(regions_parent)
    regions_children = regions_parent.find_elements_by_xpath('.//*')
    regions = [child.get_attribute('title') for child in regions_children]

    while '' in regions:
        regions.remove('')

    WebDriverWait(driver, 100).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bodyCells")))
    parent = driver.find_element_by_class_name("bodyCells")
    # print(parent)
    children = parent.find_elements_by_xpath('.//*')
    data = [child.get_attribute('title') for child in children]

    while '' in data:
        data.remove('')

    somministrations = []
    available = []
    percentage = []
    ln = len(regions) - 1

    for x in range(ln):
        somministrations.append(data[x].replace(",", "").replace(".", ""))
    somministrations.append(data[-3].replace(",", "").replace(".", ""))
    for x in range(ln, 2 * ln):
        available.append(data[x].replace(",", "").replace(".", ""))
    available.append(data[-2].replace(",", "").replace(".", ""))
    for x in range(2 * ln, 3 * ln):
        percentage.append(data[x].replace(",", "."))
    percentage.append(data[-1].replace(",", "."))

    regions.insert(0, "Regioni")
    somministrations.insert(0, "Somministrazioni")
    available.insert(0, "Dosi Consegnate")
    percentage.insert(0, "Percentuale")
    print(regions)
    print(somministrations)
    print(available)
    print(percentage)

    return regions, somministrations, available, percentage


def scrapingGroup(link):
    driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver.get(link)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "label")))
    parent = driver.find_element_by_class_name("labelGraphicsContext")
    # print(parent)
    children = parent.find_elements_by_xpath('.//*')

    data = [child.get_attribute('innerHTML') for child in children]
    data.insert(0, "Vaccinati")

    print(data)

    return data


def scrapingCategory(link):
    driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver.get(link)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "label")))
    parent = driver.find_elements_by_css_selector(
        "html body div#pbiAppPlaceHolder root div div#embedWrapperID.embedWrapper div.landingController.fillAvailableSpace div.landingContainer div#reportLandingContainer.embeddedLandingRootContent.reportContainerContent.isActive.embeddedPV.embeddedLandingRootContentLogoVisible div.embeddedPV exploration-container exploration-container-modern div.explorationContainer.explorationWithChrome.themeableElement.reading.newPaneColors div.explorationContent.fill div.explorationHost.explorationHostNoAppBar exploration-host#pvExplorationHost div.fillAvailableSpace.verticalItemsContainer div.horizontalItemsContainer exploration.exploreCanvasToBottom div.exploration explore-canvas-modern.explore-canvas-modern-style div.exploreCanvas.themeableElement.disableAnimations.stylableVisualContainerHeader.master-form-factor div.canvasFlexBox div.displayAreaContainer.droppableElement.ui-droppable div.displayArea.disableAnimations.actualSizeAlignCenter.actualSizeAlignTop.actualSizeOrigin div.visualContainerHost visual-container-repeat visual-container-modern.visual-container-component transform.bringToFront div.visualContainer.unselectable.droppableElement.ui-droppable.readMode.hideBorder.noVisualTitle.visualHeaderAbove div div.vcBody.themableBackgroundColor.themableBorderColorSolid visual-modern div.visual.visual-barChart.allow-deferred-rendering svg.cartesianChart svg.svgScrollable g.labelGraphicsContext")
    # print(parent)
    children = parent[0].find_elements_by_xpath('.//*')

    data = [child.get_attribute('innerHTML') for child in children]
    data.insert(0, "Vaccinati")

    print(data)

    return data

def scrapingSomministrationPoints(link): #WIP
    driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver.get(link)


    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "label")))

    scroll = driver.find_elements_by_css_selector('html body div#pbiAppPlaceHolder root div div#embedWrapperID.embedWrapper div.landingController.fillAvailableSpace div.landingContainer div#reportLandingContainer.embeddedLandingRootContent.reportContainerContent.isActive.embeddedPV.embeddedLandingRootContentLogoVisible div.embeddedPV exploration-container exploration-container-modern div.explorationContainer.explorationWithChrome.themeableElement.reading.newPaneColors div.explorationContent.fill div.explorationHost.explorationHostNoAppBar exploration-host#pvExplorationHost div.fillAvailableSpace.verticalItemsContainer div.horizontalItemsContainer exploration.exploreCanvasToBottom div.exploration explore-canvas-modern.explore-canvas-modern-style div.exploreCanvas.themeableElement.disableAnimations.stylableVisualContainerHeader.master-form-factor div.canvasFlexBox div.displayAreaContainer.droppableElement.ui-droppable div.displayArea.disableAnimations.actualSizeAlignCenter.actualSizeAlignTop.actualSizeOrigin div.visualContainerHost visual-container-repeat visual-container-modern.visual-container-component transform.bringToFront div.visualContainer.unselectable.readMode.hideBorder.noVisualTitle.visualHeaderAbove.droppableElement.ui-droppable div div.vcBody.themableBackgroundColor.themableBorderColorSolid visual-modern div.visual.visual-tableEx.allow-deferred-rendering div.tableExContainer div.tableEx div.scroll-bar-div')
    driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', scroll)
    print(scroll)

    parent = driver.find_elements_by_css_selector(
        "html body div#pbiAppPlaceHolder root div div#embedWrapperID.embedWrapper div.landingController.fillAvailableSpace div.landingContainer div#reportLandingContainer.embeddedLandingRootContent.reportContainerContent.isActive.embeddedPV.embeddedLandingRootContentLogoVisible div.embeddedPV exploration-container exploration-container-modern div.explorationContainer.explorationWithChrome.themeableElement.reading.newPaneColors div.explorationContent.fill div.explorationHost.explorationHostNoAppBar exploration-host#pvExplorationHost div.fillAvailableSpace.verticalItemsContainer div.horizontalItemsContainer exploration.exploreCanvasToBottom div.exploration explore-canvas-modern.explore-canvas-modern-style div.exploreCanvas.themeableElement.disableAnimations.stylableVisualContainerHeader.master-form-factor div.canvasFlexBox div.displayAreaContainer.droppableElement.ui-droppable div.displayArea.disableAnimations.actualSizeAlignCenter.actualSizeAlignTop.actualSizeOrigin div.visualContainerHost visual-container-repeat visual-container-modern.visual-container-component transform.bringToFront div.visualContainer.unselectable.readMode.hideBorder.noVisualTitle.visualHeaderAbove.droppableElement.ui-droppable div div.vcBody.themableBackgroundColor.themableBorderColorSolid visual-modern div.visual.visual-tableEx.allow-deferred-rendering div.tableExContainer div.tableEx div.innerContainer div.bodyCells")
    print(parent)




    children = parent[0].find_elements_by_xpath('.//*')

    #print(children)

    data = [child.get_attribute("title") for child in children]
    data.insert(0, "title")

    print(data)

    return data


#scrapingSomministrationPoints( "https://app.powerbi.com/view?r=eyJrIjoiMzg4YmI5NDQtZDM5ZC00ZTIyLTgxN2MtOTBkMWM4MTUyYTg0IiwidCI6ImFmZDBhNzVjLTg2NzEtNGNjZS05MDYxLTJjYTBkOTJlNDIyZiIsImMiOjh9")