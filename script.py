import os
import sys

if len(sys.argv) != 2:
    raise ValueError('Need exactly one argument: Day number')

day = sys.argv[1]

os.system('git add .')
os.system('git commit -m "Added solution for Day {0}"'.format(day))

print('Committed solution for Day {0}'.format(day))
