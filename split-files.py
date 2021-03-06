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
import operator
from synthetic import apply_rules

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def split_in_two_files(src_filename):

    pairs = set()
    number_validation = 3000
    number_test = 3007 # number_test != number_validation

    strings = 0
    duplicated = 0

    print("Split src and tgt files in 6 files for training, text and validation")

    total_lines = file_len(src_filename)
    total_lines = 3000000 # Fix lines to 12 million
    changed = 0

    validation_each = round(total_lines / number_validation)
    test_each = round(total_lines / number_test)

    if test_each == validation_each:
        print("test_each ({0}) and validation_each ({0}) cannot be equal".format(test_each, validation_each))
        return
        
    with open("data/src-val.txt", "w") as source_val,\
        open("data/src-test.txt", "w") as source_test,\
        open("data/src-train.txt", "w") as source_train,\
        open("data/tgt-val.txt", "w") as target_val,\
        open("data/tgt-test.txt", "w") as target_test,\
        open("data/tgt-train.txt", "w") as target_train,\
        open(src_filename, "r") as read_source:

        print("total_lines {0}".format(total_lines))
        print("number_validation {0}".format(number_validation))
        print("number_test {0}".format(number_test))
        print("validation_each {0}".format(validation_each))
        print("test_each {0}".format(test_each))

        clean = 0
        lines = 0
        added = 0
        changes = {}
        while True:

            src = read_source.readline()
            lines = lines + 1

            if not src or lines > total_lines:
                break

            trg = src
            src = apply_rules(src, changes)

# Assume no duplications since we use dedup Oscar corpus
#            pair = src
#            if pair in pairs:
#                duplicated = duplicated + 1
#                continue
#            else:
#                pairs.add(pair)

            if strings % validation_each == 0:
                source = source_val
                target = target_val
            elif strings % test_each == 0:
                source = source_test
                target = target_test
            else:
                source = source_train
                target = target_train

            if src != trg:
                changed = changed + 1
                added = added + 1                
                # For every changed pair we add the original correct as reference too
                source.write(trg)
                target.write(trg)

            source.write(src)
            target.write(trg)
            strings = strings + 1

    pclean = clean * 100 / strings
    pduplicated = duplicated * 100 / strings
    pchanged = changed * 100 / strings
    padded = added * 100 / strings
    total_strings = strings + added
    print(f"Strings: {strings}, total strings {total_strings}, duplicated {duplicated} ({pduplicated:.2f}%)")
    print(f"Changed {changed} ({pchanged:.2f}%), added {added} ({padded:.2f}%)")
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

    print("Joins several corpus and creates a final train, validation and test dataset")

    split_in_two_files("corpus/ca_dedup.txt")

if __name__ == "__main__":
    main()
