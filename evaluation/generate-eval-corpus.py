#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import sys
sys.path.append('../')

import os
import operator
from synthetic import apply_rules


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def split_in_two_files(src_filename):

    strings = 0
    total_lines = file_len(src_filename)
    total_lines = 3000000 # Fix lines to 12 million

    changes = {}
    with open("data/src-test.txt", "w") as source,\
        open("data/tgt-test.txt", "w") as target,\
        open(src_filename, "r") as read_source:


        lines = 0
        while True:

            src_org = read_source.readline()
            lines = lines + 1

            if not src_org or lines > total_lines:
                break

            trg = src_org
            src = apply_rules(src_org, changes)

            if src == src_org:
                continue

            source.write(src)
            target.write(trg)
            strings = strings + 1

    print(f"Total strings {lines}, selected {strings}")
    print_changes(changes)

def print_changes(changes):
    sorted_dict = sorted(changes.items(), key=operator.itemgetter(1), reverse=True)
    for change in sorted_dict:
        key, value = change
        print(f"{key}: {value}")


def append_lines_from_file(src_filename, trg_file):
    lines = 0
    with open(src_filename, 'r') as tf:
        line = tf.readline()
        while line:
            lines += 1
            trg_file.write(line)
            line = tf.readline()

    print("Appended {0} lines from {1}".format(lines, src_filename))
    return lines



def main():

    print("Takes a Catalan corpus and generates a validation corpus by introducing errors in source")
    split_in_two_files("data/catalan.txt")

if __name__ == "__main__":
    main()
