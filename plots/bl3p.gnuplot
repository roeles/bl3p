set multiplot layout 1,2

epoch_diff=946684800
t0e = t0 - epoch_diff
t1e = t1 - epoch_diff

set palette rgb 33,13,10
set key left top

set title "BL3P"
set ylabel "Time (UTC)"
set xlabel "Price (Euro)"
set cblabel "Amount"
#set xtics 50
set yrange [t1e - (1*60*60):t1e]
set ydata time
set timefmt "%s"
set format y "%H:%M"

splot \
"/home/archive/data/bl3p/ask.csv" using 2:1:4 with lines notitle,\
"/home/archive/data/bl3p/sell.csv" using 2:1:4 with lines notitle
#"/home/archive/data/bl3p/trades.csv" using 3:2:4 with points lt 1 pt 7 ps variable title "Trades"

