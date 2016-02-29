#!/usr/bin/env python
#
# (C) 2016 Ed Bueler
#
# This script puts only the "meat" of codes into new files in cstrip/, for
# inclusion into the book.
#
# We remove entire lines with either "PetscErrorCode ierr" or "//STRIP" lines.
# We strings "ierr = " and "CHKERRQ(ierr);" from any line.

import os
import re

# filenames should be distinct
files = { 2 : "vecmatksp.c tri.c",
          3 : "poisson.c",
          4 : "expcircle.c ecjacobian.c reaction.c",
          5 : "plap.c",
          6 : "ode.c heat.c pattern.c",
          7 : "ad3.c",
          8 : "readmesh.c poissontools.c poissonfem.c",
         12 : "obstacle.c"}

if not os.path.exists("cstrip/"):
    os.makedirs("cstrip/")

for chapt, filesstr in files.items():
    flist = filesstr.split()
    for fname in flist:
        sf = open('../c/ch' + str(chapt) + '/' + fname,'r')  # source
        df = open('cstrip/' + fname,'w')                     # destination
        for line in sf:
            if re.search('\/\/STRIP',line) or re.search('PetscErrorCode ierr',line):
                continue
            line = re.sub('ierr = ','', line).rstrip()
            line = re.sub('CHKERRQ\(ierr\);','', line).rstrip()
            df.write(line + '\n')
        sf.close()
        df.close()

