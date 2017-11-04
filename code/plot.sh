#!/bin/bash
END=`date "+%s"`
BEGIN=`date "+%s" -d '3 days ago -1 hour'`
#BEGIN=`date "+%s" -d '-1 hour'`
TEMPFILE=`mktemp`
cd /home/archive/data/bl3p
gnuplot -e "set datafile separator \",\"; set grid; set terminal png size 1920,1080; set output \"$TEMPFILE\"; t0=$BEGIN; t1=$END" bl3p.gnuplot
mv $TEMPFILE $1
chmod a+rx $1
