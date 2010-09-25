#!/bin/bash

#NOTE: it's the job of the script that inserts bookmarks to make sure there are no dupes.

file=$XDG_DATA_HOME/uzbl/history_html.html

echo '<HTML>' > $file
echo '<head>' >> $file
echo '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">' >> $file
echo '<title>History</title>' >> $file
echo '</head>' >> $file
echo '<body>' >> $file
hist2html >> $file
echo '</body>' >> $file
echo '</HTML>' >> $file

echo "uri $file" | socat - unix-connect:$5
