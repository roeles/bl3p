set multiplot layout 2,1

epoch_diff=946684800
t0e = t0 - epoch_diff
t1e = t1 - epoch_diff

set palette rgb 33,13,10
set key left top

set title "BL3P"
set xlabel "Time (UTC)"
set ylabel "Price (Euro)"
set cblabel "Amount"
set xrange [t1e - (24*60*60):t1e]
set xdata time
set timefmt "%s"
set format x "%H:%M"
set pm3d 
set view map

splot \
"/home/archive/data/bl3p/ask.csv" using 1:2:4 with pm3d notitle,\
"/home/archive/data/bl3p/sell.csv" using 1:2:4 with pm3d notitle,\
"/home/archive/data/bl3p/trades.csv" using 2:3:4:4 with points lt 1 pt 7 ps variable title "Trades"

set xrange [t1e - (1*60*60):t1e]
replot
