#!/bin/sh

FILE=/scans/reportfile.txt

if test -f "$FILE"; then
	echo "Report file exists, cp,learing content."
	> $FILE
else
	install -m 755 /home/pi/Documents/WashUHackathon/Reports/reportfile.txt
	echo "$FILE was cerated."
fi

echo -e "\nScanning drive...\n"

echo -e "**************USB GUARDSMAN REPORT***************\n" >> $FILE

clamscan -r /media/Tim_s_Storage_USB/info.txt | tee -a /home/pi/Documents/WashUHackathon/Reports/reportfile.txt
