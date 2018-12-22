
# The Bob Dylan Tour Scraper
### Description
The purpose of the program is to scrape the tour date, location, venue and ticket link off the [official Bob Dylan website](https://www.bobdylan.com/on-tour/).
Then format the information to a subreddit sidebar in a markdown format.

### How to Run the Scraper
Simply run bobrunner.py with Python2.x and [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) and [requests](http://docs.python-requests.org/en/master/) installed. The output will then be printed to the console.

### Example Output
* 31 Mar - Dusseldorf, Germany - [Mitsubishi Electric Halle](https://www.ticketmaster.de/artist/bob-dylan-tickets/1607?cities=60055)

* 4 May - Malaga, Spain - [Marenostrum Castle Park](https://www.bobdylan.com/on-tour/)
* 5 May - Murcia, Spain - [Plaza de Toros](https://www.bobdylan.com/on-tour/)
* 7 May - Valencia, Spain - [Plaza de Toros de Valencia](https://www.bobdylan.com/on-tour/)
* 21 Jun - Bergen, Norway - [Koengen](https://www.ticketmaster.no/event/593577)
* 24 Jun - Helsinki, Finland - [Hartwall Arena](https://www.ticketmaster.fi/event/244861)
* 26 Jun - Stockholm, Sweden - [Ericsson Globe](http://axs.com/se/events/365878/bob-dylan-tickets?skin=livenationse)
* 28 Jun - Gothenberg, Sweden - [Scandinavium](https://www.ticketmaster.se/event/bob-dylan-biljetter/532495)
* 29 Jun - Oslo, Norway - [Spektrum](https://www.ticketmaster.no/event/593503)
* 5 Jul - Hamburg, Germany - [Barclaycard Arena](https://www.ticketmaster.de/artist/bob-dylan-tickets/1607?cities=60075)
* 6 Jul - Braunschweig, Germany - [Volkswagen Halle](https://www.ticketmaster.de/artist/bob-dylan-tickets/1607?cities=61600)
* 7 Jul - Mainz, Germany - [Volkspark](https://www.ticketmaster.de/artist/bob-dylan-tickets/1607?cities=66755)
* 9 Jul - Erfurt, Germany - [Messehalle](https://www.ticketmaster.de/event/bob-dylan-tickets/312335)
* 10 Jul - Stuttgart, Germany - [Jazzopen](https://www.bobdylan.com/on-tour/)
* 12 Jul - London, England - [BST Hyde Park](https://www.axs.com/uk/events/357515/bob-dylan-and-neil-young-tickets/promop%20age/13931?skin=bst)
* 14 Jul - Kilkenny, Ireland - [Nowlan Park](https://www.ticketmaster.ie/promo/gxllqn)

Notice that sometimes the official sites have not provided any link to a concert. In that case, the official tour website link is inserted instead.
