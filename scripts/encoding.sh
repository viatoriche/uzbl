#!/bin/sh

ENCODE_LIST="UTF-8\nKOI8-R\nCP1251"
FGCOLOR="#B8DDEA"
BGCOLOR="#222222"
SELCOLOR="#B8DDEA"
 
if dmenu --help 2>&1 | grep -q '\[-rs\] \[-ni\] \[-nl\] \[-xs\]'
then
    ENC=`echo "$ENCODE_LIST" | dmenu -nb "$BGCOLOR" -nf "$FGCOLOR" -sb "$SELCOLOR" -sf "$BGCOLOR" -p "ENCODING:" -xs -rs -l 20`
else
    ENC=`echo "$ENCODE_LIST" | dmenu -nb "$BGCOLOR" -nf "$FGCOLOR" -sb "$SELCOLOR" -sf "$BGCOLOR" -p "ENCODING:"`
fi

echo 'set default_encoding = '$ENC | socat - unix-connect:$5
echo 'reload' | socat - unix-connect:$5
