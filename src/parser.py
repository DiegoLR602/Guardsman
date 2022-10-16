import sys
import time
import datetime

def parseLog(logPath="ex.txt"):
    output = {
        "driveSignature": "",
        "driveName": "",
        "date": 0,
        "numInfectedFiles": 0,
        "filePaths": [],
        "threatType": []
    }

    with open(logPath, 'r') as f:
        next(f)
        lines = (line.strip() for line in f.readlines())
        lines = (line for line in lines if line)

        for line in lines:
            if(line == "-----SCAN SUMMARY-----"):
                break

            virPath, threatType = line.split(":", 1)
            output["filePaths"].append(virPath)
            output["threatType"].append(threatType.strip())

        for line in f:
            lineID, lineValue = line.split(":", 1)

            if(lineID == "Infected files"):
                output["numInfectedFiles"] = lineValue
                #extend for more options
            elif(lineID == "Start Date"):
                output["date"] = time.mktime(datetime.strptime(lineValue, "%Y:%m:%d %H:%M:%S"))

    return output