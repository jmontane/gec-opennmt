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


import os


def split_in_two_files():

    lines = 0
    match = 0
    equal = 0
    changed = 0
        
    with open("data/src-test.500", "r") as source,\
        open("data/tgt-test.500", "r") as reference,\
        open("data/translated.txt", "r") as target:

        while True:

            src = source.readline()
            ref = reference.readline()
            trg = target.readline()

            if not src or not trg or not ref:
                break

            lines = lines + 1

            if ref == trg:
                match = match + 1

            elif src == target:
                equal = equal + 1

            else:
                changed = changed + 1

    pmatch = match * 100 / lines
    pequal = equal * 100 / lines
    pchanged = changed * 100 / lines
    print(f"Total strings {lines}, matched {match} ({pmatch:.2f}%), equal {equal} ({pequal:.2f}%), changed {changed} ({pchanged:.2f}%)")

def main():

    print("Evaluates reference corpus against translation")
    split_in_two_files()

if __name__ == "__main__":
    main()
