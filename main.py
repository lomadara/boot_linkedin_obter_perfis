from bs4 import BeautifulSoup
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request as ur
import os
import random

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)

email = ''
password = ''
perfis = []
def obterperfis(page):
    driver.get("https://www.linkedin.com/search/results/people/?facetGeoRegion=%5B%22br%3A6045%22%5D&facetIndustry=%5B%22137%22%2C%2296%22%2C%224%22%5D&origin=FACETED_SEARCH&page="+str(page))
    if page == 0 :
        driver.find_element_by_xpath("//p//a[@class='main__sign-in-link']").click()
        time.sleep(3)
        driver.find_element_by_xpath("//form//input[@id='username']").send_keys(email)
        driver.find_element_by_xpath("//form//input[@id='password']").send_keys(password)
        driver.find_element_by_xpath("//button[@class='btn__primary--large from__button--floating']").click()
        time.sleep(3)
    search = driver.find_element_by_xpath("//div//ul[@class='search-results__list list-style-none ']")
    html = search.get_attribute('outerHTML')
    soup = BeautifulSoup(html, 'html.parser')
    mydivs = soup.find_all("a", {"class": "search-result__result-link ember-view"})
    lastperfil = ''
    for a in mydivs:
        if a['href'] != lastperfil:
            perfis.append("https://www.linkedin.com"+str(a['href']))
            lastperfil = a['href']

for x in range(0,3):
    obterperfis(x)

for perfil in perfis:
    driver.get(perfil)
    time.sleep(3)
    driver.find_element_by_xpath("//button[@class='ml2 pv-s-profile-actions__overflow-toggle artdeco-button artdeco-button--muted artdeco-button--2 artdeco-button--secondary ember-view']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//artdeco-dropdown-item[@class='pv-s-profile-actions pv-s-profile-actions--save-to-pdf pv-s-profile-actions__overflow-button full-width text-align-left ember-view']").click()
    time.sleep(3)
