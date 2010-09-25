#!/bin/sh
# b23.sh -- created 2010-09-24, Viator, viator@via-net.org
# License: GPL (see http://www.gnu.org/licenses/gpl.txt)

uri="$6"

wget --post-data="l=$uri" --load-cookies=$XDG_DATA_HOME/uzbl/cookies.txt 'http://b23.ru' -O /tmp/b23.html

echo "uri /tmp/b23.html" | socat - unix-connect:$5

# vi: ts=4
