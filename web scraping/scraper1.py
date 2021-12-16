from selenium import webdriver 
from bs4 import BeautifulSoup 
import time 
import csv


START_URL = "https://exoplanets.nasa.gov/exoplanet-catalog/" 
browser = webdriver.Chrome("/Users/Planet/Desktop/all files/whj files/python/web scraping/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

def scrape():
    headers=["name","distance from eath(ly)","mass(jupiter for scale)","stellar magnitute","discovy date"]
    planet_data=[]
    for a in range(0,4):
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ut in soup.find_all("ul",attrs={"class","exoplanet"}):
            lt=ut.find_all("li")
            
            temp_list=[]
            for s,i in enumerate(lt):
                if s==0:
                     temp_list.append(i.find_all("a")[0].contents[0])
                     
                else:
                    temp_list.append(i.contents[0])
            planet_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)



scrape()
