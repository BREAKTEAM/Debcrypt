#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from colored import fg

color = fg('#008000')

def pingo(iteration,
          total,
          prefix='',
          suffix='',
          decimals=1,
          length=100,
          fill='█'):
    """
    Print
    """
    length = length - (len(prefix) + len(suffix) + 10)
    percent = ("{0:." + str(decimals) + "f}").format(
        100 * (iteration / float(total)))
    fillLength = int(length * iteration // total)
    bar = fill * fillLength + '-' * (length - fillLength)
    print(color + '\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end='\r')
    if iteration == total:
        print()
