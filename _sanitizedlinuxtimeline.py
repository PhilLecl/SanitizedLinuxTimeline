import json
import csv


def check_existence(distros, csvfile):
    """check_existence(distros, csvfile)
    Return a set of all distributions that are in distros but not in csvfile

    Arguments:
    distros - a set of distributions
    csvfile - csv file 
    """

    with open(csvfile) as f:
        csvdata = list(csv.reader(f, delimiter=',', quotechar='"'))

    s = set()
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
            s.add(distro)
    return s


def read_distros(listfile):
    """read_distros(listfile)
    Return a set of all distributions contained in listfile
    with each line being treated as one distribution.
    Lines with a leading '#' are ignored
    """

    s = set()
    with open(listfile) as f:
        for line in f:
            if line[0] != "#":
                s.add(line.replace("\n", ""))
    return s


def apply_rules(distros, rulefile):
    d = distros.copy()
    with open(rulefile) as f:
        rules = json.loads(f.read())
    for distro in distros.copy():
        if distro in rules.keys():
            d.remove(distro)
            if rules[distro] and rules[distro][0] != "#":
                d.add(rules[distro])
    return d


def add_ancestors(distro, distros, csvdata):
    d = distros.copy()
    for row in csvdata:
        if row[0] == "N":
            add = (row[1] == distro)
            i = 8
            while i < len(row) and not add:
                add = (row[i] == distro)
                i += 3
            if add and row[3] and row[3] not in d:
                d.add(row[3])
                d = add_ancestors(row[3], d, csvdata)
                break
    return d
