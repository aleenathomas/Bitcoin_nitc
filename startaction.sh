#!/bin/bash

#start gnunet
./start.sh

#create node
python createnode.py

#listening for transactions in background
./search.sh "signedtrans.txt" &
#listening for proposed block in background
./search.sh "block.txt"	&

#ask the user for his choice
PS3='Please enter your choice: '
options=("1" "2" "3" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "1")
            python createtransaction.py
            ./publish "signedtrans.txt"	
            ;;
        "2")
            echo "you chose choice 2"
            ;;
        "3")
            echo "you chose choice 3"
            ;;
        "Quit")
            break
            ;;
        *) echo invalid option;;
    esac
done
