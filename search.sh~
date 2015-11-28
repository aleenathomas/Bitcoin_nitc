#!/bin/bash

timeout 10s gnunet-search "$1" > filestodownload.sh
grep -v '^#' filestodownload.sh > download.sh
#rm filestodownload.sh
chmod +x download.sh
./download.sh

#validating the transaction received
python validatetrans.py
