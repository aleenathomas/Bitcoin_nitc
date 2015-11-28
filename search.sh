#!/bin/bash

#while :
#do
#timeout gnunet-search -N 1 "$1" > filestodownload.sh
timeout 100s gnunet-search "$1" > filestodownload.sh
gnunet-search "$1" > filestodownload.sh
grep -v '^#' filestodownload.sh > download.sh
rm filestodownload.sh
chmod +x download.sh
./download.sh
#mv $1 $i
#let i=i+1
#done

