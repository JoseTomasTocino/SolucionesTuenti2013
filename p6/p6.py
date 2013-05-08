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
from itertools import product

DEBUG = 0

def debug(*args):
    if DEBUG:
        print(*args)

class Node(object):

    def __init__(self, x, y, parent = None):
        self.x = x
        self.y = y
        self.parent = parent
        self.visited = False
        self.cost_to_here = None

    def __str__(self):
        return '(%i, %i)' % (self.x, self.y)

    def __repr__(self):
        return '(%i, %i)' % (self.x, self.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x * 1000 + self.y

def main():
    num_cases = int(sys.stdin.readline())
    debug('Num cases: %i' % num_cases)

    for current_case in range(num_cases):
        map_width, map_height, speed, speedup_cost = map(int, filter(None, sys.stdin.readline().strip().split()))

        debug()
        debug('Map: %i x %i' % (map_width, map_height))
        debug('Speed: %i' % speed)
        debug('speedup time: %i' % speedup_cost)

        # Build the matrix of nodes
        nodes = [[Node(x, y) for y in range(map_height)] for x in range(map_width)]

        # Reset start and end positions
        startX = startY = endX = endY = 0

        # Read the map definition
        for row in range(map_height):
            row_elem = list(sys.stdin.readline().strip())
            row_elem = filter(lambda x: x != '\xb7', row_elem)
            row_elem = ['.' if x == '\xc2' else x for x in row_elem]

            debug(row_elem)

            for col, elem_type in enumerate(row_elem):
                if elem_type == '#':
                    nodes[col][row] = None
                elif elem_type == 'X':
                    startX, startY = col, row
                elif elem_type == 'O':
                    endX, endY = col, row

        for row in nodes:
            debug(row)

        debug('Start:', nodes[startX][startY])
        debug('End:  ', nodes[endX][endY])
        debug()
        compute_path(nodes, startX, startY, endX, endY, map_width, map_height, 0, speedup_cost, speed, 0)

        print (int(round(nodes[endX][endY].cost_to_here)))

def compute_path(nodes, x, y, endX, endY, map_width, map_height, value_so_far, speedup_cost, speed, r):

    q = r * '  '

    debug()
    debug(q, 'I\'m at (%i,%i)' % (x, y))

    value_so_far += speedup_cost

    sub_paths = []

    # Compute possible directions
    for dx, dy in product([-1, 0, 1], [-1, 0, 1]):

        # Check bounds
        if not (0 <= x + dx < map_width):
            continue

        if not (0 <= y + dy < map_height):
            continue

        # Ignore diagonals
        if abs(dx) + abs(dy) > 1:
            continue

        # Ignore self position
        if dx == 0 and dy == 0:
            continue

        # Ignore non-existant nodes
        if nodes[x+dx][y+dy] is None:
            continue

        debug(q, '  Computing for direction dx=%i, dy=%i' % (dx, dy))

        newX, newY = x, y
        oldX, oldY = x, y

        while(True):
            oldX += dx
            oldY += dy
            if oldX == map_width or oldX == 0 or oldY == 0 or oldY == map_height or nodes[oldX][oldY] is None:
                break

            newX, newY = oldX, oldY

        steps = abs(newX - x) + abs(newY - y)
        debug('DIVISION TEST', steps, speed, steps/speed)
        local_cost = value_so_far + float(steps) / float(speed)

        debug(q, '  New pos: (%i, %i)' % (newX, newY))
        debug(q, '  Steps: %i' % steps)

        if not nodes[newX][newY].visited or (nodes[newX][newY].visited and nodes[newX][newY].cost_to_here > local_cost):
            debug(q, '  This node should be revisited')

            nodes[newX][newY].visited = True
            nodes[newX][newY].cost_to_here = local_cost
            nodes[newX][newY].parent = nodes[x][y]

            if newX == endX and newY == endY:
                debug('\t' * 10, 'OMG THE ENDING!! Cost:', local_cost)
                sub_paths.append(True)
            else:
                sub_paths += compute_path(nodes, newX, newY, endX, endY, map_width, map_height, local_cost, speedup_cost, speed, r + 1)

        else:
            debug(q, '  I\'ve been here in better times...')

        debug()

    debug(q, 'Returning...')
    return sub_paths

if __name__ == '__main__':
    main()
