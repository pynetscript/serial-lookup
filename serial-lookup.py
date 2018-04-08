#!/usr/bin/python

###############################################################################
# Written by:           Aleks Lambreca
# Creation date:        08/04/2018
# Last modified date:   08/04/2018
# Version:              v1.1
#
# Script use:           Parses a Cisco serial number into an approximate manufacture date.
#                       The script needs 2 arguments to run:
#                       - 1st argument: serial-number.py
#                       - 2nd argument: SERIALNUMBER
#                       Valid command looks like:
#                       ./serial-number.py SAD08300D4W
#
# Script input:         Cisco serial number
#
# Script output:        Approximate manufacture date
#                       Travis CI build notification to Slack private channel
###############################################################################


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import re
import sys
import string
from pprint import pprint as pp
from collections import Counter


# If arguments not equal to 2 we get an error.
if len(sys.argv) != 2:
    print('\n>> Usage: ./serial-lookup.py SERIALNUMBER \n')
    exit()


serial = sys.argv[1]

def count_letters(serial):
    counter = Counter()
    for word in serial.split():
        counter.update(word)
    return sum(counter.values())

serial_counter = count_letters(serial)

if serial_counter < 11:
    print('\n'
          '>> Error: Serial Number must be 11 characters. \n'
          '          The Serial Number you specified was', serial_counter, 'characters. \n')
    sys.exit()
else:
    pass


REGEX = r'\w\w\w(\d\d)(\d\d)'

m = re.match(REGEX, serial)

year_code = int(m.group(1))
week_code = int(m.group(2))


manuf_years = []
for x in range(1996, 2100):
    manuf_years.append(x)


numbers_manuf_years = {}
for i in range(0, 100):
        numbers_manuf_years[i] = manuf_years[i]

numbers_manuf_week = {
    1: 'January',
    2: 'January',
    3: 'January',
    4: 'January',
    5: 'January',
    6: 'February',
    7: 'February',
    8: 'February',
    9: 'February',
    10: 'March',
    11: 'March',
    12: 'March', 
    13: 'March',
    14: 'March',
    15: 'April',
    16: 'April',
    17: 'April',
    18: 'April',
    19: 'May',
    20: 'May',
    21: 'May',
    22: 'May',
    23: 'June',
    24: 'June',
    25: 'June',
    26: 'June',
    27: 'June',
    28: 'July',
    29: 'July',
    30: 'July',
    31: 'July',
    32: 'August',
    33: 'August',
    34: 'August',
    35: 'August',
    36: 'September',
    37: 'September',
    38: 'September',
    39: 'September',
    40: 'September',
    41: 'October',
    42: 'October',
    43: 'October',
    44: 'October',
    45: 'November',
    46: 'November',
    47: 'November',
    48: 'November',
    49: 'February',
    50: 'December',
    51: 'December',
    52: 'December',
}
    

print('\n>> Serial Number:', serial)


if year_code in numbers_manuf_years:
    year = (numbers_manuf_years[year_code])
else:
    year = ''
    print('>> Error: Could not match year code!')

if week_code in numbers_manuf_week:
    week = (numbers_manuf_week[week_code])
else:
    week = ''
    print('>> Error: Could not match week code!')


print('>> Approximate manufacture date:', week, year,'\n')
