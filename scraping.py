from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def scraping(link):
    """
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    """
    driver = webdriver.Chrome(executable_path=r'C:\WebDrivers\chromedriver.exe')
    driver.get(link)
    # parent = driver.find_element_by_xpath(
    #    "/html/body/div[1]/root/div/div/div[1]/div/div/div/exploration-container/exploration-container-modern/div/div/div/exploration-host/div/div/exploration/div/explore-canvas-modern/div/div[2]/div/div[2]/div[2]/visual-container-repeat/visual-container-modern[32]/transform/div/div[3]/div/visual-modern/div/div")
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "rowHeaders")))
    regions_parent = driver.find_element_by_class_name("rowHeaders")
    # print(regions_parent)
    regions_children = regions_parent.find_elements_by_xpath('.//*')
    regions = [child.get_attribute('title') for child in regions_children]

    while '' in regions:
        regions.remove('')

    WebDriverWait(driver, 20).until(
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
        somministrations.append(data[x])
    somministrations.append(data[-3])
    for x in range(ln, 2 * ln):
        available.append(data[x])
    available.append(data[-2])
    for x in range(2 * ln, 3 * ln):
        percentage.append(data[x].replace(",","."))
    percentage.append(data[-1])

    regions.insert(0, "Regioni")
    somministrations.insert(0, "Somministrazioni")
    available.insert(0, "Dosi Consegnate")
    percentage.insert(0, "Percentuale")
    print(regions)
    print(somministrations)
    print(available)
    print(percentage)

    return regions, somministrations, available, percentage
