#!/bin/sh
# just an example of how you could handle your downloads
# try some pattern matching on the uri to determine what we should do

# Some sites block the default wget --user-agent..
GET="wget --user-agent=Firefox --content-disposition --load-cookies=$XDG_DATA_HOME/uzbl/cookies.txt"

#dest="$HOME/download"

url="$1"
echo "Download a file"
echo ""
echo "---------------------------------"
echo "Destination: `pwd`"
echo "URL: $url"
echo "---------------------------------"
echo ""
#echo "File list:"
#echo ""
#ls -Gh --color --group-directories-first
#echo "---------------------------------"
echo "Input filename: (Enter - none)"
read filename

test "x$filename" = "x" && { 
    $GET "$url";
}

test "x$filename" != "x" && {
    $GET "$url" -O "$filename";
}

echo "Input command (example: mc) or Enter for complete"
read cmd
$cmd
exit

