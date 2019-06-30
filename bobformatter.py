URL = "https://www.bobdylan.com/on-tour/"

"""Format the concert data to fit subreddit sidebar. 
Example one line of the output: * 21 Jun [Bergen, Norway](https://www.ticketmaster.no/event/593577) - Koengen
returns all concerts formatted in one string.
"""

"""Add the ticket link. Needs to handle when link attribute isn't added, empty or provided.
"""
def addTicketLine(concert):
    line = ""
    try:
        if concert["tickets"]["href"] == "": # If the link is empty
            line += URL
        else:
            line += concert["tickets"]["href"] # Use link provided
    except KeyError as e: # # If official website haven't added link attribute
        line += URL



def format(concerts):
    lines = ""
    for concert in concerts:
        line = "* "
        line += concert["date"]["date"][:-5]
        line += " - "
        line += concert["city"]["city"]
        line += " - "
        line += "["
        line += concert["venue"]["venue"]
        line += "]("
        try:
            if concert["tickets"]["href"] == "":
                line += "https://www.bobdylan.com/on-tour/"
            else:
                line += concert["tickets"]["href"]
        except KeyError as e:
            line += "https://www.bobdylan.com/on-tour/"
        line += ")"
        lines += line + "\n"
    return lines

