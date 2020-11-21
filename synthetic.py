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

def _replace(sentence, src, trg, changes):

    replaced = sentence.replace(src, trg)
    if replaced != sentence:
        key = f"{src}->{trg}"
        if key not in changes: 
            value = 0
        else:
            value = changes[key]

        value = value + 1
        changes[key] = value
    
    return replaced

def apply_rules(sentence, changes):

    # Dicritic "què"
    sentence = _replace(sentence, " què ", " que ", changes)

    return sentence

