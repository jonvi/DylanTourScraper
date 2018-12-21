from bs4 import BeautifulSoup
import requests

URL = "https://www.bobdylan.com/on-tour/"

"""Read HTML data from website specified by url.
The url needs to be https://www.bobdylan.com/on-tour/.
Return the BeautifulSoup object.
"""
def readWebsite(url):
    webpage = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    return BeautifulSoup(webpage, features="html.parser")

"""Read HTML data from file for offline testing.
Url needs to be on the form "file://" + dir_path + "/file.html.
Return the BeautifulSoup object.
"""
def readFile(url):
    webpage = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}).text
    return BeautifulSoup(webpage, features="html.parser")

"""Take an HTML attribute and format it to a JSON-like format.
"""
def sift(atr):
    field_type = atr.get("class")[0]
    if field_type == "tickets" and atr.get("data-url") is not "None" and atr.getText() == "Tickets":
        return {"href": atr.get("data-url").replace(" ", "")}
    elif field_type == "venue" and atr.get("href") is not "None":
        return {field_type: atr.getText(), "href": atr.get("href")}
    elif field_type == "city" and atr.get("href") is not "None":
        return {field_type: atr.getText(), "href": atr.get("href")}
    elif field_type == "date" and atr.get("href") is not "None":
        return {field_type: atr.getText(), "href": atr.get("href")}
    return None

"""Scrape the relevant info from the website: date, location, venue and ticket-link.
website is a boolean that indicates if data should be retreived from website (True) or file (False). 
website default value is True.
Return concerts in JSON-like format.
"""
def scrape(url, website):
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
        cnrt = {}
        for atr in concert:
            sifted = sift(atr)
            if sifted is not None:
                cnrt[atr.get("class")[0]] = sifted
        res.append(cnrt)
    return res[1:]
