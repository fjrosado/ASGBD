#!/usr/bin/python

import os
import sys

print "Introduzca usuario"
usuario=raw_input()

print "Introduzca clave"
password=raw_input()

print "Introduzca base de datos"
basedatos=raw_input()

os.system('mysql -u' + usuario + ' -p' + password + ' ' + basedatos)
