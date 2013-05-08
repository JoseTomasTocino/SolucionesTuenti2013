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
import re
from pprint import pprint

DEBUG = 0

def debug(*args):
    if DEBUG:
        print(*args)

def main():
    num_scripts = int(sys.stdin.readline())

    split_re = re.compile(r'([\.<>])')

    for current_script_number in range(num_scripts):

        current_script = sys.stdin.readline().strip()
        scenes = filter(None, split_re.split(current_script))

        debug()
        debug('###################################################################')
        debug("Current script: %s" % current_script)
        debug()

        scene_dict = {}
        scene_counter = 1
        last_scene_index = 0
        invalid = False

        for i in range(0, len(scenes), 2):
            scene_type = scenes[i]
            scene_text = scenes[i + 1]

            debug('Scene counter: %i' % scene_counter)
            debug('Scene type: %s' % scene_type)
            debug('Scene text: %s' % scene_text)
            debug()

            if scene_text not in scene_dict:
                # El primer elemento indica antes de qué punto debe aparecer la escena
                # El tercer elemento indica después de qué punto debe aparecer la escena
                scene_dict[scene_text] = [0, None, None]

            if scene_type == '.':
                if scene_dict[scene_text][0] is not None and scene_dict[scene_text][0] >= scene_counter:
                    invalid = True
                    break

                if scene_dict[scene_text][2] is not None and scene_dict[scene_text][2] <= scene_counter:
                    invalid = True
                    break

                scene_dict[scene_text] = [scene_counter, scene_counter, scene_counter]
                last_scene_index = scene_counter

            elif scene_type == '<':
                # La escena debe aparecer antes de scene_counter - 1
                scene_dict[scene_text][2] = scene_counter - 2

            elif scene_type == '>':
                # La escena debe aparecer después de scene_counter - 1
                scene_dict[scene_text][0] = scene_counter

            scene_counter += 1

        # Nos deshacemos de los None en los laterales
        for d in scene_dict:
            if scene_dict[d][0] is not None and scene_dict[d][2] is None:
                scene_dict[d][2] = scene_counter + 1

        if invalid:
            print('invalid')
            continue

        if DEBUG:
            pprint(scene_dict)

        final_script = []
        multiple = False
        invalid = False

        first_scene_is_checked = False

        for i in range(last_scene_index + 1):
            s_prev = [(x, scene_dict[x]) for x in scene_dict if scene_dict[x][1] is None and scene_dict[x][2] is not None and scene_dict[x][0] <= i and scene_dict[x][2] >= i]
            s_curr = [(x, scene_dict[x]) for x in scene_dict if scene_dict[x][1] is not None and scene_dict[x][1] == i]

            # One list is empty and the other is filled
            if bool(s_prev) != bool(s_curr):
                final_script += [x[0] for x in s_prev + s_curr]

                if not first_scene_is_checked:
                    first_scene_is_checked = True

            # Both empty
            elif not s_prev and not s_curr:

                pass

            # Both filled
            elif s_prev and s_curr:
                if not first_scene_is_checked:
                    invalid = True
                    debug('Inválido, no hay inicio exacto')

                elif i == last_scene_index:
                    invalid = True
                    debug('Inválido, no hay final exacto')

                elif bool(s_prev):
                    multiple = True

            debug('i: %i %s' % (i, '(Multiple)' if multiple else ''))
            debug(s_prev)
            debug(s_curr)
            debug()

        debug()

        if invalid:
            print('invalid')
        elif multiple:
            print('valid')
        else:
            print(','. join(final_script))

if __name__ == '__main__':
    main()
