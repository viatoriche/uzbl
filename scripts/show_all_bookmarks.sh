#!/bin/bash

#NOTE: it's the job of the script that inserts bookmarks to make sure there are no dupes.

filebook=$XDG_DATA_HOME/uzbl/bookmarks
filechrom=$XDG_DATA_HOME/uzbl/bookmarks_with_chromium
file=$XDG_DATA_HOME/uzbl/bookmarks_html.html

cat $filebook > $filechrom
getcb >> $filechrom

echo '<HTML>' > $file
echo '<head>' >> $file
echo '<meta http-equiv="Content-Type" content="text/html; charset=utf-8">' >> $file
echo '<title>Bookmarks</title>' >> $file
echo '</head>' >> $file
echo '<body>' >> $file
book2html >> $file
echo '</body>' >> $file
echo '</HTML>' >> $file

echo "uri file:///$file" | socat - unix-connect:$5
