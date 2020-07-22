#! /usr/bin/python3

import sys, csv


def argparse():
    global listfile
    listfile = sys.argv[1]
    global csvfile
    csvfile = sys.argv[2]


def check_existence():
    for distro in distros:
        found = False
        for row in csvdata:
            if row[0] == "N":
                if row[1] == distro:
                    found = True
                    break
                i = 8
                while i < len(row):
                    if row[i] == distro:
                        found = True
                        break
                    i += 3
        if not found:
            print(distro + " not found in csv.")


def read_distros():
    l = set()
    with open(listfile) as f:
        for line in f:
            if line[0] != "#":
                l.add(line.replace("\n", ""))
    return l


if __name__ == "__main__":
    argparse()
    distros = read_distros()
    with open(csvfile) as f:
        csvdata = list(csv.reader(f, delimiter=',', quotechar='"'))
    check_existence()
