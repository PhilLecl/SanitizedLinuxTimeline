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


def remove_comments(csvfile):
    """remove_comments(csvfile)
    Reads csvfile and returns a list of all lines whose first element is not empty and doesn't begin with "//" or "#"

    :param str csvfile: filename of the csv file

    :return: a list containing all non-comment lines
    """
    with open(csvfile) as f:
        _csvdata = list(csv.reader(f, delimiter=',', quotechar='"'))
    csvdata = [row for row in _csvdata if row[0]
               and not row[0].startswith("//") and not row[0].startswith("#")]
    return csvdata


def write_csv(filename, csvdata):
    """write_csv(filename, csvdata)
    Write the data in csvdata to a file called filename

    :param str filename: name of the output file
    :param list csvdata: csv data in list form
    """
    with open(filename, "w") as f:
        csvwriter = csv.writer(
            f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in csvdata:
            csvwriter.writerow(row)


def remove_unneeded_distros(_csvdata, distros):
    """remove_unneeded_distros(_csvdata)
    Return a list that only contains the elements of csvdata that are relevant to the distributions in distros

    :param list _csvdata: csv data in list format
    :param set distros: set of distribution names

    :return: the cleaned-up set
    """
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
