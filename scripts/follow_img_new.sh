#!/bin/sh

config=$1;
shift
pid=$1;
shift
xid=$1;
shift
fifo=$1;
shift
socket=$1;
shift
url=$1;
shift
title=$1;
shift

output=`echo "script @scripts_dir/follow_img_new.js \'$*\'" | socat - unix-connect:$socket`

case $output in
   *XXXEMIT_FORM_ACTIVEXXX*) echo 'event FORM_ACTIVE' | socat - unix-connect:$socket ;;
   *NEW_WINDOW*) echo 'event ESCAPE' | socat - unix-connect:$socket ;;
esac

echo "$output" | grep 'http://' | socat - unix-connect:$socket

