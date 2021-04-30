# SanitizedLinuxTimeline

This project contains python scripts for reducing the [Linux Distribution Timeline](https://github.com/FabioLolix/linuxtimeline) to the most popular distributions (according to [Distrowatch](https://distrowatch.com/)) and their ancestors.

## Dependencies
- git
- gnuclad
- Python3
- BeautifulSoup4

## Setup
    git clone --recursive https://github.com/PhilLecl/SanitizedLinuxTimeline

## Usage
Generate a list containing the top NUM distros on Distrowatch and write it to LISTFILE:

    ./scrape_distrowatch.py NUM LISTFILE [TIMEFRAME]

Possible timeframes are:
- 0: last 12 months
- 1: last 6 months
- 2: last 3 months
- 3: last month

Generate a csv for gnuclad using LISTFILE and write it to CSVFILE (in linuxtimeline/):

    ./sanitize_csv LISTFILE linuxtimeline/ldt.csv replacements.json linuxtimeline/CSVFILE

Generate the image using gnuclad and write it to SVGFILE:

    cd linuxtimeline
    gnuclad CSVFILE SVGFILE ldt.conf
