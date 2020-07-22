#! /usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup


def argparse():
    try:
        global number
        number = int(sys.argv[1])
        global listfile
        listfile = sys.argv[2]
        global timeframe
        timeframe = int(sys.argv[3]) if len(sys.argv) > 3 else 1
    except:
        print(
            "Usage: ./scrape_distrowatch.py NUMBER_OF_DISTROS OUTPUT_FILE [TIMEFRAME]")
        print("""TIMEFRAMES:
        0 - last year
        1 - last 6 months
        2 - last 3 months
        3 - last mont""")
        sys.exit(1)


def scrape():
    URL = "https://distrowatch.com/dwres.php?resource=popularity"
    soup = BeautifulSoup(requests.get(URL).content, "html.parser")
    table = soup.find_all(
        "table", style="width: 100%; table-layout: auto")[timeframe]
    rows = table.find_all("tr")[1:]

    distros = set()
    for i in range(int(number)):
        row = rows[i]
        distros.add(row.td.text)

    with open(listfile, "w") as f:
        for line in distros:
            f.write(line+"\n")


if __name__ == "__main__":
    argparse()
    scrape()
