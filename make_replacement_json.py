#! /usr/bin/python3

import sys, csv, json
from _sanitizedlinuxtimeline import read_distros, check_existence

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

if __name__ == "__main__":
    argparse()
    distros = read_distros(listfile)
    with open(csvfile) as f:
        csvdata = list(csv.reader(f, delimiter=',', quotechar='"'))
    nonexistent = check_existence(distros, csvdata)
    ne_dict = {}
    for distro in nonexistent:
        ne_dict[distro] = ""
    with open(rulefile, "w") as f:
        f.write(json.dumps(ne_dict, sort_keys=True, indent=4))
