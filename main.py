import time

import pandas
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# specify the url of the webpage
urls = [
    "www.facebook.com",
    "www.twitter.com",
    "www.linkedin.com",
    "www.abc.com",
    "www.cnn.com",
    "www.nbc.com",
    "www.bbc.com",
    "www.foxnews.com",
    "www.abcnews.com",
    "www.espn.com",
    "www.fox.com",
    "www.hulu.com",
    "www.netflix.com",
    "www.amazon.com",
    "www.chase.com",
    "www.bankofamerica.com",
    "www.wellsfargo.com",
    "www.google.com",
    "www.yahoo.com",
    "www.bing.com"
]

# initialize the web driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222")
chrome_options.add_argument("--disable-cache")
chrome_options.add_argument("--disable-application-cache")
chrome_options.add_argument("--disable-offline-load-stale-cache")
chrome_options.add_argument("--disk-cache-size=0")

iterations = input("Set Nuber of Iteration (Whole number only): ")
Name = input("Set .CSV file save name: ")

LoadTime_DFs = []

for iteration in range(int(iterations)):
    df = pandas.DataFrame()
    for url in urls:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # navigate to the webpage
        start_time = time.time()
        driver.get('https://' + url)
        # wait for the page to fully load
        wait = WebDriverWait(driver, 60)
        wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "body")))
        end_time = time.time()
        # calculate the load time in seconds
        load_time = end_time - start_time
        # print the load time
        df[url] = [round(load_time, 2)]
        print("Page load time: {:.2f} seconds".format(load_time))
        # close the driver
        driver.quit()
    LoadTime_DFs.append(df)
    Main_DF = pd.concat(LoadTime_DFs)
    Main_DF.to_csv("Temp_Save.csv")

Main_DF = pd.concat(LoadTime_DFs)
Main_DF.to_csv(str(Name) + ".csv")
