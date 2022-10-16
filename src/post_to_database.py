from requests.auth import HTTPBasicAuth
import requests


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
    api_url = "https://natanielfarzan.wixsite.com/guardsman/_functions/scans"
    response = requests.get(api_url, headers=headers)
    print(response.json())
    

def post_to_database(parsedDict, args):
    api_url = "https://natanielfarzan.wixsite.com/guardsman/_functions/addScanResult"
    
    if(hasattr(args, "driveName")):
        parsedDict["driveName"] = args.driveName[0]
    
    if(hasattr(args, "driveSignature")):
        parsedDict["driveSignature"] = args.driveSignature[0]
    #scan_data = {"driveSignature": drive_signature, "driveName": drive_name, "date": date,"numInfectedFiles": num_infected_files, "filePaths": file_paths, "threatType": threat_type}
    
    # Get secret api key
    with open('scanner.secret') as f:
        lines = f.readlines()
    secret_key = lines[0]

    # auth = HTTPBasicAuth('auth', secret_key)
    
    headers = {
    'auth': secret_key
    }
        
    response = requests.post(api_url, headers=headers, json=parsedDict)
    print(response.json())
    print("Response Status code:", response.status_code)
    


def input_dictionary(input_dict):
    # Change the inputted string dictionary into a dictionary
    
    drive_signature = input_dict[drive_signature]
    drive_name = input_dict[drive_name]
    date = input_dict[date]
    num_infected_files = input_dict[num_infected_files]
    file_paths = input_dict[file_paths]
    threat_type = input_dict[threat_type]
    
    print("Posting to database...")
    post_to_database(drive_signature, drive_name, date, num_infected_files, file_paths, threat_type)



# Getting pipped data
# data = sys.stdin.read()
# print("Printing from pipe:", data)

# echo "Output from program" | python3 post-to-database.py