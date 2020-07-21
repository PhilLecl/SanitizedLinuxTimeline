#! /usr/bin/python3

from sys import argv
import requests
from bs4 import BeautifulSoup


def parse_args():
    try:
        global number
        number = int(argv[1])
        global listfile
        listfile = argv[2]
        global timeframe
        timeframe = argv[3] if len(argv) > 3 else 1
    except:
        print(
            "Usage: ./scrape_distrowatch.py NUMBER_OF_DISTROS OUTPUT_FILE [TIMEFRAME]")


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
    parse_args()
    scrape()
