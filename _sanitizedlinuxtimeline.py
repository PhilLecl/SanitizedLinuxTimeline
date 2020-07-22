def check_existence(distros, csvdata):
    """check_existence(distros, csvdata)
    Return a set of all distributions that are in distros but not in csvfile
    
    Arguments:
    distros - a set of distributions
    csvdata - csv data as a list
    """
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


read_distros("list_100")
