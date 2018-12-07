URL = "https://www.bobdylan.com/on-tour/"

"""Format the concert data to fit subreddit sidebar. 
Example one line of the output: * 21 Jun [Bergen, Norway](https://www.ticketmaster.no/event/593577) - Koengen
returns all concerts formatted in one string.
"""
def format(concerts):
    lines = ""
    for concert in concerts:
        if not concert["tickets"]["href"]: # Replace empty links with official on-tour link.
            concert["tickets"]["href"] = URL

        line = "* "
        line += concert["date"]["date"][:-5]
        line += " ["
        line += concert["city"]["city"]
        line += "]("
        line += concert["tickets"]["href"]
        line += ")"
        line += " - "
        line += concert["venue"]["venue"]

        lines += line + "\n"
    return lines