import json
import csv


def check_existence(distros, csvfile):
    """check_existence(distros, csvfile)
    Return a set of all distributions that are in distros but not in csvfile

    :param set distros: a set of distributions
    :param str csvfile: filename of the csv file

    :return: set containing all distributions that are in distros but don't appear in csvfile
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

    :param str listfile: filename of the file containing the list
    """

    s = set()
    with open(listfile) as f:
        for line in f:
            if line[0] != "#":
                s.add(line.replace("\n", ""))
    return s


def apply_rules(distros, rulefile):
    """apply_rules(distros, rulefile)
    Use the rules contained in rulefile to match the spelling of the distributions in distros to the spelling in the csv.

    :param set distros: a set of distribution names

    :return: a set with the rules applied
    """
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
    """Add the ancestors of distro to distros.

    :param str distro: the distribution whose acestors to add
    :param set distros: a set of distribution names
    :param list csvdata: csv data in list format for finding the ancestors

    :returns: A set containing the original distributions as well as the ancestors of distro.
    """
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
