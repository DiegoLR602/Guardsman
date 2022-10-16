from parser import parseLog
from send_sms import send_sms
from post_to_database import post_to_database
import argparse

def main():
    parser = argparse.ArgumentParser(description="Arguemnts for GuardsMan")
    parser.add_argument("filePath", metavar="FP", type=str, nargs=1, help="The path to the log file")
    parser.add_argument('-n', '--drive-name', dest="driveName", metavar="DN", type=str, nargs=1, help="The name of the drive", required=False, default="")
    parser.add_argument('-s', '--drive-signature', dest="driveSignature", metavar="DS", type=str, nargs=1, help="The signature of the drive", required=False, default="")
    args = parser.parse_args()
    
    post_to_database(parseLog(args.filePath[0]), args)
    send_sms(parseLog(args.filePath[0]), args)

if(__name__ == "__main__"):
    main()
