#! /usr/bin/python3

# SanitizedLinuxTimeline: Reduce the Linux Distribution Timeline to the most popular distributions.
# Copyright (C) 2020-2021  Philipp Leclercq
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import sys
import csv
from _sanitizedlinuxtimeline import read_distros, add_ancestors, apply_rules, remove_comments, write_csv, remove_unneeded_distros


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


if __name__ == "__main__":
    argparse()

    distros = read_distros(listfile)
    distros = apply_rules(distros, rulefile)
    csvdata = remove_comments(inputcsv)

    for distro in distros.copy():
        distros = add_ancestors(distro, distros, csvdata)

    print(len(distros))
    print(distros)
    csvdata = remove_unneeded_distros(csvdata, distros)

    write_csv(outputcsv, csvdata)
