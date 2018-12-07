from bobparser import scrape
from bobformatter import format

"""The driver for the Dylan tour scraper.
Print the formatted concerts.
"""

URL = 'http://www.bobdylan.com/on-tour/'
concerts = scrape(URL)
lines = format(concerts)
print(lines)