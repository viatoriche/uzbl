#!/usr/bin/env python
#Vincent Kriek <vincent at vincentkriek dot nl>
#
#Dependencies:
#  dmenu with vertical patch and the ability to define position I used http://aur.archlinux.org/packages.php?ID=27334
#  xwininfo

import os
import subprocess
import sys

### Config settings, remember, everything must be a string!!!
y                       = "0" #This is the y-pos of dzen
x                       = "0" #This is the x-pos of dzen
width               = "1000" #Dzen's width
lines               = "10" #Number of vertical lines in dzen
bg                      = "darkgrey" #Dzen's background color
fg                      = "darkgreen" #Dzen's foreground
sb                      = "black"
sf                      = "red"
font                    = "monospace"
bookmarkfile    = os.path.join(os.environ['XDG_DATA_HOME'],'uzbl/keywordBookmarks.txt')
historyfile     = os.path.join(os.environ['XDG_DATA_HOME'],'uzbl/history')

xwin = subprocess.Popen(["xwininfo", "-id", sys.argv[3]], stdout=subprocess.PIPE)
xwininfo = xwin.communicate()[0]
xwinArray = xwininfo.split("\n")
print len(xwinArray)
for line in xwinArray:
    if line.find("Absolute upper-left X") != -1:
        print line
        x = line.split(":")[1]
        x = x.strip(" ");
        print x
    if line.find("Absolute upper-left Y") != -1:
        y = line.split(":")[1]
        y = y.strip(" ")
    if line.find("Width") != -1:
        width = line.split(":")[1]
        width = width.strip(" ")
cat = subprocess.Popen(["cat", bookmarkfile, historyfile], stdout=subprocess.PIPE)
dmenu = subprocess.Popen(["dmenu", "-xs", "-fn", font, "-l", lines, "-x", x, "-y", y, "-w", width, "-sb", sb, "-sf", sf, "-nb", bg, "-nf", fg], stdin=cat.stdout, stdout=subprocess.PIPE)
output = dmenu.communicate()[0]
output = output.split(" ")

for i in output:
    if i.startswith("http://"):
        if sys.argv[8] == "tab":
                os.system("uzbl \"%s\"" % i)
        elif sys.argv[8] == "open":
            os.system("uzblctrl -s %s -c \"uri %s\"" % (sys.argv[5], i))
