#! /usr/bin/python3

import sys, csv, json
from _sanitizedlinuxtimeline import read_distros, check_existence, apply_rules

def argparse():
    try:
        global listfile
        listfile = sys.argv[1]
        global csvfile
        csvfile = sys.argv[2]
        global rulefile
        rulefile = sys.argv[3]
    except:
        print("Usage: ./check_replacement_json.py LISTFILE CSVFILE OUTPUTFILE")
        sys.exit(1)

if __name__ == "__main__":
    argparse()
    distros = read_distros(listfile)
    distros = apply_rules(distros, rulefile)
    ne = check_existence(distros, csvfile)
    print(ne)
