#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Copyright (C) 2011 José Tomás Tocino García <theom3ga@gmail.com>

# Autor: José Tomás Tocino García

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.

import sys

DEBUG = 0

def debug(*args):
    if DEBUG:
        print(*args)

def main():
    sys.stdin.readline()
    dict_file = sys.stdin.readline().strip()
    sys.stdin.readline()
    num_words = int(sys.stdin.readline())
    sys.stdin.readline()

    word_list = []
    for line in sys.stdin:
        word_list.append(line.strip())

    debug('Dictionary file:', dict_file)
    debug('Num words:', num_words)
    debug('Word list:', word_list)

    get_word_key = lambda x: ''.join(sorted(x.strip()))

    # Get the sizes of the words
    word_lengths = set(map(len, word_list))
    word_keys = map(get_word_key, word_list)
    word_dict = {}

    debug('Word lengths:', word_lengths)
    debug('Word keys:', word_keys)
    debug()

    word_dict = {}

    f = open(dict_file)
    for w in f:
        debug('Checking %s, len %i, key %s' % (w.strip(), len(w) - 1, get_word_key(w)))

        w_t = len(w) - 1
        # If word has known length
        if w_t in word_lengths:

            # Sort the letters
            w_k = get_word_key(w)
            if w_k in word_keys:

                if w_t not in word_dict:
                    word_dict[w_t] = {}
                if w_k not in word_dict[w_t]:
                    word_dict[w_t][w_k] = []

                word_dict[w_t][w_k].append(w.strip())

    f.close()

    debug('ditto')

    for w in word_list:
        w_k = get_word_key(w)
        w_t = len(w)

        if w_k in word_dict[w_t]:
            sugg_list = filter(lambda x: x != w, word_dict[w_t][w_k])
        else:
            sugg_list = []

        sugg_list.sort()

        print ('%s ->' % w, ' '.join(sugg_list))

if __name__ == '__main__':
    main()
