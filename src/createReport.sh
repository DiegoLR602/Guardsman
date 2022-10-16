#!/bin/sh

FILE=./reportfile.txt

if test -f "$FILE"; then
	echo "Report file exists, cp,learing content."
	> $FILE
else
	install -m 755 ./reportfile.txt
	echo "$FILE was cerated."
fi

echo -e "\nScanning drive...\n"

echo -e "**************USB GUARDSMAN REPORT***************\n" >> $FILE

clamscan -r / /Users/diegolopezramos/Documents/CPSC_Courses/CS408 | tee -a ./reportfile.txt
