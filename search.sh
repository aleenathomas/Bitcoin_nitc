#!/bin/bash

<<<<<<< HEAD
#while :
#do
#timeout gnunet-search -N 1 "$1" > filestodownload.sh
timeout 10s gnunet-search "$1" > filestodownload.sh
=======
gnunet-search "$1" > filestodownload.sh
>>>>>>> 9f1f19c63030d2c3c4f0b0bebfd8174c6d790abc
grep -v '^#' filestodownload.sh > download.sh
rm filestodownload.sh
chmod +x download.sh
./download.sh
<<<<<<< HEAD
#mv $1 $i
#let i=i+1
#done
=======

>>>>>>> 9f1f19c63030d2c3c4f0b0bebfd8174c6d790abc

