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
import json
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
