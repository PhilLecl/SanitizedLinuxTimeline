#! /usr/bin/python3

import sys, csv, json


def argparse():
    try:
        global listfile
        listfile = sys.argv[1]
        global csvfile
        csvfile = sys.argv[2]
        global rulefile
        rulefile = sys.argv[3]
    except:
        print("Usage: ./make_replacement_json.py LISTFILE CSVFILE OUTPUTFILE")
        sys.exit(1)


def check_existence():
    d = {}
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
            d[distro] = ""
    with open(rulefile, "w") as f:
        f.write(json.dumps(d, sort_keys=True, indent=4))


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
