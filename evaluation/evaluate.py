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

    strings = 0

    with open("data/tgt-test.500", "r") as source,\
        open("data/translated.500", "r") as target

        lines = 0
        match = 0
        while True:

            src = source.readline()
            trg = target.readline()

            if not src or not trg:
                break

            lines = lines + 1

            if src == trg:
                match = match + 1

    pmatch = match * 100 / strings
    print(f"Total strings {lines}, matched {match} ({pmatch:.2f}%)")

def main():

    print("Evaluates reference corpus against translation")
    split_in_two_files()

if __name__ == "__main__":
    main()
