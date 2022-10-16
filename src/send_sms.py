from json import load
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()

def send_sms(message):
    # Your Account SID from twilio.com/console
    account_sid = os.environ['ACCOUNT_SID']
    # Your Auth Token from twilio.com/console
    auth_token  = os.environ['AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    print(os.environ['PHONE_NUMBER'])
    m = client.messages.create(
        to=os.environ['PHONE_NUMBER'], 
        from_="+12059648542",
        body=("Drive signature: " + message["driveSignature"] + "\n"+
        "Drive name: " + message["driveName"] + "\n" +
        "Scan date:" + str(message["date"]) + "\n" +
        "Number of infected files: " + str(message["numInfectedFiles"]) + "\n" +
        "File paths: " + str(message["filePaths"]) + "\n" +
        "Threat type: " + str(message["threatType"])
        ))

    print(m.sid)