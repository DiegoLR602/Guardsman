import secrets
from requests.auth import HTTPBasicAuth
import requests
import time
import sys


def get_from_database():
    # Get secret api key
    with open('src/scanner.secret') as f:
        lines = f.readlines()
    secret_key = lines[0]

    auth = HTTPBasicAuth('auth', secret_key)
    
    headers = {
    'auth': secret_key
    }
    
    # Get from database
    api_url = "https://natanielfarzan.wixsite.com/scanner-database/_functions/scans"
    response = requests.get(api_url, headers=headers)
    print(response.json())


# Get the current date and time in unix
def get_current_date_time():
    return time.time()


def post_to_database(drive_signature, drive_name, date, num_infected_files, file_paths, threat_type):
    api_url = "https://natanielfarzan.wixsite.com/scanner-database/_functions/addScanResult"
    
    scan_data = {"driveSignature": drive_signature, "driveName": drive_name, "date": date,"numInfectedFiles": num_infected_files, "filePaths": file_paths, "threatType": threat_type}
    
    # Get secret api key
    with open('src/scanner.secret') as f:
        lines = f.readlines()
    secret_key = lines[0]

    auth = HTTPBasicAuth('auth', secret_key)
    
    headers = {
    'auth': secret_key
    }
        
    response = requests.post(api_url, headers=headers, json=scan_data)
    print(response.json())
    print("Response Status code:", response.status_code)
    


def main():
    # drive_signature = sys.argv[1]
    # drive_name = sys.argv[2]
    # date = get_current_date_time()
    # num_infected_files = sys.argv[3]
    # file_paths = sys.argv[4]
    # threat_type = sys.argv[5]
    
    drive_signature = "test_drive_signature6"
    drive_name = "test_drive_name"
    date = get_current_date_time()
    num_infected_files = 5
    file_paths = ["test_file_paths"]
    threat_type = ["test_threat_type"]
    
    print("Posting to database...")
    # post_to_database(get_current_date_time(), sys.argv[1], sys.argv[2])
    post_to_database(drive_signature, drive_name, date, num_infected_files, file_paths, threat_type)


if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Invalid number of arguments")
    # else:
    # main()
    
    



    
    # Getting pipped data
    # data = sys.stdin.read()
    # print("Printing from pipe:", data)
    
# echo "Output from program" | python3 post-to-database.py
