#!/bin/sh
# just an example of how you could handle your downloads
# try some pattern matching on the uri to determine what we should do

# Some sites block the default wget --user-agent..
#GET="wget --user-agent=Firefox --content-disposition --load-cookies=$XDG_DATA_HOME/uzbl/cookies.txt"

#dest="$HOME/download"
#url="$8"

#http_proxy="$9"
#export http_proxy

#filename="$10"
#export filename

#terminal -e = $XDG_DATA_HOME/uzbl/scripts/downloader.sh $url $http_proxy

URL="$6"
PROXY="$8"
SAVE="Save file"
CANCEL="Cancel saving"
UP=".."
#If you modify the above 3 variables, make sure you name them in such a manner that you will never have a folder with that same name

url=$URL
dest="$HOME/download"

# only changes the dir for the $get sub process
if echo "$url" | grep -E '.*\.torrent' >/dev/null;
then
    dest="$dest/torrent"
fi
if echo "$url" | grep -E '.*\.avi' >/dev/null;
then
    dest="$dest/avi"
fi
if echo "$url" | grep -E '.*\.bz2' >/dev/null;
then
    dest="$dest/bz2"
fi
if echo "$url" | grep -E '.*\.deb' >/dev/null;
then
    dest="$dest/deb"
fi
if echo "$url" | grep -E '.*\.flv' >/dev/null;
then
    dest="$dest/flv"
fi
if echo "$url" | grep -E '.*\.gif' >/dev/null;
then
    dest="$dest/gif"
fi
if echo "$url" | grep -E '.*\.gz' >/dev/null;
then
    dest="$dest/gz"
fi
if echo "$url" | grep -E '.*\.jpg' >/dev/null;
then
    dest="$dest/jpg"
fi
if echo "$url" | grep -E '.*\.mp3' >/dev/null;
then
    dest="$dest/mp3"
fi
if echo "$url" | grep -E '.*\.ogg' >/dev/null;
then
    dest="$dest/ogg"
fi
if echo "$url" | grep -E '.*\.pdf' >/dev/null;
then
    dest="$dest/pdf"
fi
if echo "$url" | grep -E '.*\.png' >/dev/null;
then
    dest="$dest/png"
fi
if echo "$url" | grep -E '.*\.rar' >/dev/null;
then
    dest="$dest/rar"
fi
if echo "$url" | grep -E '.*\.txt' >/dev/null;
then
    dest="$dest/txt"
fi
if echo "$url" | grep -E '.*\.zip' >/dev/null;
then
    dest="$dest/zip"
fi
if echo "$url" | grep -E '.*\.jpeg' >/dev/null;
then
    dest="$dest/jpg"
fi
if echo "$url" | grep -E '.*\.ogv' >/dev/null;
then
    dest="$dest/ogv"
fi
if echo "$url" | grep -E '.*\.exe' >/dev/null;
then
    dest="$dest/exe"
fi
if echo "$url" | grep -E '.*\.htm*' >/dev/null;
then
    dest="$dest/html"
fi
if echo "$url" | grep -E '.*\.php' >/dev/null;
then
    dest="$dest/html"
fi
if echo "$url" | grep -E '.*\.xls' >/dev/null;
then
    dest="$dest/xls"
fi
if echo "$url" | grep -E '.*\.doc' >/dev/null;
then
    dest="$dest/doc"
fi

 
TARGET=$dest
FGCOLOR="#B8DDEA"
BGCOLOR="#222222"
SELCOLOR="#B8DDEA"
 
#could have "hardcoded" these or course but this is easier in case you want to modify something :)
 
while (true); do
DIRLIST=`ls -l $TARGET | grep ^d | awk '{print $8}'`
if dmenu --help 2>&1 | grep -q '\[-rs\] \[-ni\] \[-nl\] \[-xs\]'
then
    SELECTION=`echo "$SAVE\n$CANCEL\n$UP\n$DIRLIST" | dmenu -nb "$BGCOLOR" -nf "$FGCOLOR" -sb "$SELCOLOR" -sf "$BGCOLOR" -p "$TARGET" -xs -rs -l 20`
else
    SELECTION=`echo "$SAVE\n$CANCEL\n$UP\n$DIRLIST" | dmenu -nb "$BGCOLOR" -nf "$FGCOLOR" -sb "$SELCOLOR" -sf "$BGCOLOR" -p "$TARGET"`
fi
if [ "$SELECTION" = "$SAVE" ]; then 
    break
fi
if [ "$SELECTION" = "$CANCEL" ]; then 
        exit
fi
if [ -z "$SELECTION" ]; then 
        exit
fi
if [ "$SELECTION" = "$UP" ]; then 
        TARGET=$(dirname $TARGET)
else
    TARGET="$TARGET/$SELECTION"
fi
done
 
cd "$TARGET"
terminal -e $XDG_DATA_HOME/uzbl/scripts/downloader.sh $URL $PROXY
#terminal -e "echo \"Target: $TARGET/\" && $DOWNLOADER $URL && echo \"Download complete. Press any key to close\" && read lol"
