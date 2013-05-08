#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

# Copyright (C) 2013 José Tomás Tocino García <theom3ga@gmail.com>

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
import math
import time

DEBUG = 0
SHOULD_BUY = 0
SHOULD_SELL = 1

def debug(*args):
    if DEBUG:
        print(*args)

def getMax(l):
    return getWhat(l, lambda x, y: x >= y)

def getMin(l):
    return getWhat(l, lambda x, y: x <= y)

def getWhat(l, fun):
    mI = 0
    mV = l[0]

    for i, v in enumerate(l):
        if fun(v, mV):
            mV = v
            mI = i

    return (mI, mV)

def main():
    numCases = int(sys.stdin.readline())

    for currentCase in range(numCases):
        initialBudget = int(sys.stdin.readline())
        rates = map(int, filter(None, sys.stdin.readline().strip().split()))

        debug()
        debug('######################################################################')
        debug('Case %i' % currentCase)
        debug('initialBudget = %i' % initialBudget)
        debug('rates =', rates)
        debug()

        currentBudget = initialBudget
        currentCoins = 0

        while len(rates) > 1:

            debug('-------')
            debug('Budget: %i \nCoins: %i' % (currentBudget, currentCoins))
            debug('Rates:', rates)

            # I look for the moment the prices starts to rise
            v0 = rates[0]
            limDer = len(rates) - 1

            for j, v in enumerate(rates[1:]):
                if v > v0:
                    limDer = j + 1
                    break
                else:
                    v0 = v

            localMinPos, localMin = getMin(rates[:limDer])

            # Update the rates list
            rates = rates[localMinPos + 1:]

            localMax = rates[0]
            localMaxPos = 0

            for j, v in enumerate(rates):
                if v < localMax:
                    break

                localMax = v
                localMaxPos = j

            rates = rates[localMaxPos + 1:]

            if localMin > localMax:
                break

            # Do them ops
            currentCoins += math.floor(currentBudget / localMin)
            currentBudget -= currentCoins * localMin
            currentBudget += currentCoins * localMax
            currentCoins = 0

            debug('I buy at %i' % (localMin,))
            debug('I sell at %i' % (localMax, ))

            if DEBUG:
                time.sleep(0.4)

        print(int(currentBudget))

if __name__ == '__main__':
    main()
