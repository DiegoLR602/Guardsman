import secrets
from requests.auth import HTTPBasicAuth
import requests
import datetime
import sys
# api_url = "https://natanielfarzan.wixsite.com/scanner-database/_functions/scans"
# response = requests.get(api_url)
# print(response.json())

# Get the current date and time
def get_current_date_time():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


def post_to_database(date, drive_name, num_infected_files):
    api_url = "https://natanielfarzan.wixsite.com/scanner-database/_functions/addScanResult"
    scan_data = {"date": date,"driveName": drive_name,"numInfectedFiles": num_infected_files}
    with open('src/scanner.secret') as f:
        lines = f.readlines()
    secret_key = lines[0]
    # secret_key = HTTPBasicAuth('apikey', '')
    response = requests.post(api_url, secret=secret_key, json=scan_data)
    print(response.json())
    print("Response Status code:", response.status_code)


def main():
    print("Posting to database...")
    post_to_database(get_current_date_time(), sys.argv[1], sys.argv[2])


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Invalid number of arguments")
    else:
        main()
