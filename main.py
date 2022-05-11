from selenium import webdriver
import time
import random
import shell
import os
import sys
from configparser import ConfigParser
from selenium.webdriver.common.keys import Keys


def resource_path(relative_path: str) -> str:
    '''
    Get absolute path to resource, works for dev and for PyInstaller
    '''
    try:
        base_path = sys._MEIPASS

    except Exception:
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)


def main():

    for i in range(0,10):   

        config = ConfigParser()
        config.read("example.ini")


        CHROME_DRIVER_PATH = config.get("chromedriver", "path")
        DURATION = config.getint("delay", "seconds")

        driver = webdriver.Chrome(resource_path(CHROME_DRIVER_PATH))

        URL = config.get("website", "url")
        driver.get(URL)

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/fieldset/div/div/div[2]/div/div/div/div/div[11]/div').click()

        time.sleep(DURATION)
        motivo = driver.find_element_by_xpath('/html/body/div[1]/div/form/div/div[2]/div[2]/fieldset/div[2]/div/div/textarea')

        lista = ['excelente servicio', 'buen servicio', 'muy buena comida', 'personal atento']
        x = lista[random.choice([0,1,2,3])]
        motivo.send_keys(x)

        driver.find_element_by_xpath('/html/body/div[1]/div/form/div/nav/div/div/button').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/div[2]/fieldset/div/div/div[2]/div/div/div/div/div[10]/div').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/nav/div/div[1]/button').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/div[2]/div[1]/fieldset/div/div/ul/li[1]/div/div').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/div[2]/div[3]/fieldset/div/div/ul/li[1]/div/div').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/nav/div/div[1]/button').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/div[2]/div[1]/fieldset/div/div/ul/li[2]/div/div/div/div[1]/input').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/div[2]/fieldset/div/div/div[2]/div/div/div/div/div[10]/div').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/div[2]/div[8]/fieldset/div/div/ul/li[2]/div/div/div/div[1]/input').click()

        time.sleep(DURATION)
        driver.find_element_by_xpath('/html/body/div/div/form/div/nav/div/div[1]/button').click()

        driver.close()

        time.sleep(30)



if __name__ == "__main__":
    main()
