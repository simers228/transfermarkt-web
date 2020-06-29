import os, random, sys, time
from urllib.parse import urlparse
from selenium import webdriver
import selenium
from bs4 import BeautifulSoup
import requests
import pandas
import time
import operator
from selenium.webdriver.common.keys import Keys

chromedriver = "/Users/simer/Downloads/chromedriver 2"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("https://www.transfermarkt.us")
search_bar = driver.find_element_by_name('query')
search_bar.send_keys(input("Enter Name of any Soccer Player"))
search_bar.send_keys(Keys.RETURN)
elems = driver.find_elements_by_class_name("spielprofil_tooltip")
search_prof = []
truenam = ''
trueval = ''

total_dict = {}
for elem in elems:
        search_prof.append(elem.get_attribute("href"))

for links in search_prof:
        driver.get(search_prof[0])
        break

current_player_name = driver.find_elements_by_xpath("//*[@id='spieler_select_breadcrumb_chzn']/a/span")
for values in current_player_name:
    truenam = str(values.text)
truenam = truenam.split()
new_c = truenam[1:]
listToStr = ' '.join(map(str, new_c))
print(listToStr)

for i in range(5):
    page = driver.current_url
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    pageTree = requests.get(page, headers = headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')

    next_player = pageSoup.find_all("span", {"class": "spieler-name"})
    next_player_value = pageSoup.find_all("td", {"class": "rechts mw-gesamt"})

    player_values = {}
    player_values[next_player[-1].text] = next_player_value[-1].text.strip("\n")

    elems = driver.find_elements_by_class_name("spielprofil_tooltip")
    all_profiles = []

    time.sleep(3)

    for elem in elems:
        all_profiles.append(elem.get_attribute("href"))

    for links in all_profiles:
        driver.get(all_profiles[-1])
        total_dict.update(player_values)
        all_profiles.clear()
        print(total_dict)

print(max(total_dict, key=total_dict.get),max(total_dict.values()))





