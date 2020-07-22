#! /usr/bin/python3

import sys
import csv
from _sanitizedlinuxtimeline import read_distros, add_ancestors, apply_rules


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


def remove_comments(inputcsv):
    with open(inputcsv) as f:
        _csvdata = list(csv.reader(f, delimiter=',', quotechar='"'))
    csvdata = [row for row in _csvdata if row[0]
               and not row[0].startswith("//") and not row[0].startswith("#")]
    return csvdata


def remove_unneeded_distros(_csvdata):
    csvdata = _csvdata.copy()
    for row in _csvdata:
        if row[0] == "N" and row[1] not in distros:
            needed = False
            i = 8
            while i < len(row) and not needed:
                if row[i] in distros:
                    needed = True
                i += 3
            if not needed:
                csvdata.remove(row)
        elif row[0] == "C" and (row[2] not in distros or row[4] not in distros):
            csvdata.remove(row)
        elif row[0] == "D" and row[1] not in distros:
            csvdata.remove(row)
    return csvdata


def write_csv(filename, csvdata):
    with open(filename, "w") as f:
        csvwriter = csv.writer(
            f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in csvdata:
            csvwriter.writerow(row)


if __name__ == "__main__":
    argparse()

    distros = read_distros(listfile)
    distros = apply_rules(distros, rulefile)
    csvdata = remove_comments(inputcsv)

    for distro in distros.copy():
        distros = add_ancestors(distro, distros, csvdata)

    csvdata = remove_unneeded_distros(csvdata)

    write_csv(outputcsv, csvdata)
