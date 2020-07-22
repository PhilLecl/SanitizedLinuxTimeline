#! /usr/bin/python3

from sys import argv
import csv


def argparse():
    global listfile
    listfile = argv[1]
    global csvfile
    csvfile = argv[2]


def read_distros():
    l = set()
    with open(listfile) as f:
        for line in f:
            if line[0] != "#":
                l.add(line.replace("\n", ""))
    return l


def add_ancestors(distro):
    global distros
    for row in csvdata:
        if row[0] == "N" and row[1] == distro:
            if row[3] and row[3] not in distros:
                distros.add(row[3])
                add_ancestors(row[3])
            break


def remove_comments():
    global csvdata
    csvdata = [row for row in csvdata if row[0]
               and not row[0].startswith("//") and not row[0].startswith("#")]


def remove_unneeded_distros():
    global csvdata
    for row in csvdata.copy():
        if row[0] == "N" and row[1] not in distros and row[8] not in distros:
            csvdata.remove(row)
        elif row[0] != "N":
            csvdata.remove(row)


def print_csv():
    for row in csvdata:
        print(row)


if __name__ == "__main__":
    argparse()

    distros = read_distros()

    with open(csvfile) as f:
        csvdata = list(csv.reader(f, delimiter=',', quotechar='"'))
    remove_comments()

    for distro in distros.copy():
        add_ancestors(distro)

    remove_unneeded_distros()
