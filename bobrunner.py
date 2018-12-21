from bobparser import scrape
from bobformatter import format



"""The driver for the Dylan tour scraper.
Print the formatted concerts.
"""

URL = 'http://www.bobdylan.com/on-tour/'
#URL = "file:/" + dir_path + "/ontour.html"
concerts = scrape(URL, True)
lines = format(concerts)

print(lines)
