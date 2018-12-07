from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import os

"""Read HTML data from website specified by url.
The url needs to be https://www.bobdylan.com/on-tour/.
Return the BeautifulSoup object.
"""
def readWebsite(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    return BeautifulSoup(webpage, features="html.parser")

"""Read HTML data from file for offline testing.
Url needs to be on the form "file://" + dir_path + "/file.html.
Return the BeautifulSoup object.
"""
def readFile(url):
    webpage = urlopen(url).read()
    return BeautifulSoup(webpage, features="html.parser")

"""Take an HTML attribute and format it to a JSON-like format.
"""
def sift(atr):
    field_type = atr.get("class")[0]
    if field_type == "tickets" and atr.get("data-url") != "None" and atr.getText() == "Tickets":
        return {"href": atr.get("data-url").replace(" ", "")}
    elif field_type == "venue" and atr.get("href") != "None":
        return {field_type: atr.getText(), "href": atr.get("href")}
    elif field_type == "city" and atr.get("href") != "None":
        return {field_type: atr.getText(), "href": atr.get("href")}
    elif field_type == "date" and atr.get("href") != "None":
        return {field_type: atr.getText(), "href": atr.get("href")}
    return None

"""Scrape the relevant info from the website: date, location, venue and ticket-link.
website is a boolean that indicates if data should be retreived from website (True) or file (False). 
website default value is True.
Return concerts in JSON-like format.
"""
def scrape(url, website = True):
    # Read from website or file.
    if website:
        soup = readWebsite(url)
    else:
        soup = readFile(url)
    # Insert relevant attributes in a dict.
    concerts = [attribute for attribute in (concert.findAll(True, 
    {"class": ["date", "city", "venue", "tickets"]}) for concert in soup.findAll("div", {"class": "line"}))]

    # Sift attributes of each concert.
    res = []
    for concert in concerts:
        crt = {}
        for atr in concert:
            if sift(atr) != None:
                crt[atr.get("class")[0]] = sift(atr)
        res.append(crt)
    return res[1:]
