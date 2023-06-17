#!/usr/bin/env python3

# Parse website and create sitemap in csv format

import requests
from bs4 import BeautifulSoup
import csv

def __parseUrl(url):
      try:
        return requests.get(url).content
      except:
        print("invalid url")

def __fetchElementsBySelector(html, selector):
    soup = BeautifulSoup(html, "html.parser")
    return soup.find_all(selector)

def createSiteMap(url):
    html = __parseUrl(url)
    links = __fetchElementsBySelector(html,"a")
    siteMap = []

    for link in links:
        href = link.get("href")
        if href is not None:
            siteMap.append(href)

    return siteMap

def writeToCsv(fileName, siteMap):
    with open(fileName, mode='w') as file:
        writer = csv.writer(file)

        writer.writerow(["Link"])

        for link in siteMap:
            writer.writerow([link])


siteMap = createSiteMap("https://jabko.ua")

writeToCsv("sitemap.csv", siteMap)

