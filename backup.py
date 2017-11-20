#!/usr/bin/python

import os
import sys

print "Introduzca usuario"
usuario=raw_input()

print "Introduzca clave"
password=raw_input()

print "Introduzca base de datos"
basedatos=raw_input()

print "Nombre del archivo"
nombre=raw_input()

os.system('mysqldump -u ' + usuario + ' -p' + password + ' ' + basedatos + ' | gzip > ' + nombre +  '.sql.gz')

