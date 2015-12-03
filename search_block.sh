#!/bin/bash

timeout 10s gnunet-search "$1" > filestodownload_block.sh
grep -v '^#' filestodownload_block.sh > download_block.sh
#rm filestodownload.sh
chmod +x download_block.sh
./download_block.sh
