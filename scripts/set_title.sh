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

test "x$title" = "x" && { 
    title='\ ';
}

echo "set cool_title=`cutstr $title 15`" | socat - unix-connect:$socket


