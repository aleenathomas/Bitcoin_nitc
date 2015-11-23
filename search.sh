#!/bin/bash

gnunet-search "$1" > filestodownload.sh
grep -v '^#' filestodownload.sh > download.sh
rm filestodownload.sh
chmod +x download.sh
./download.sh


