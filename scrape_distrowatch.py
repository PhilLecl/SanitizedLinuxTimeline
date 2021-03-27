#! /usr/bin/python3

# SanitizedLinuxTimeline: Reduce the Linux Distribution Timeline to the most popular distributions.
# Copyright (C) 2020-2021  Philipp Leclercq
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

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
