#!/bin/sh

# It is expected that this file is located in /usr/local/bin/

DIR=$1
FILE=/scans/reportfile.txt

if test -f "$FILE"; then
	echo "Report file exists, clearing content."
	> $FILE
else
	mkdir -p /scans
	install -m 755 ./reportfile.txt
	echo "$FILE was created."
fi

echo -e "\nScanning drive...\n"

echo -e "**************USB GUARDSMAN REPORT***************\n" >> $FILE

clamscan -r $DIR | tee -a /scans/reportfile.txt
