#!/usr/bin/python

import os
import sys

usuario=sys.argv[1]
password=sys.argv[2]
basedatos=sys.argv[3]

os.system('mysql -u' + usuario + ' -p' + password + ' ' + basedatos)

