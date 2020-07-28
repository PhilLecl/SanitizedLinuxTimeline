#! /usr/bin/python3

import sys
import csv
from _sanitizedlinuxtimeline import read_distros, add_ancestors, apply_rules, remove_comments, write_csv, remove_unneeded_distros


def argparse():
    try:
        global listfile
        listfile = sys.argv[1]
        global inputcsv
        inputcsv = sys.argv[2]
        global rulefile
        rulefile = sys.argv[3]
        global outputcsv
        outputcsv = sys.argv[4]
    except:
        print("Usage: ./sanitize_csv.py LISTFILE INPUTCSV RULEFILE OUTPUTCSV")
        sys.exit(1)


if __name__ == "__main__":
    argparse()

    distros = read_distros(listfile)
    distros = apply_rules(distros, rulefile)
    csvdata = remove_comments(inputcsv)

    for distro in distros.copy():
        distros = add_ancestors(distro, distros, csvdata)
    
    print(len(distros))
    print(distros)
    csvdata = remove_unneeded_distros(csvdata, distros)

    write_csv(outputcsv, csvdata)
