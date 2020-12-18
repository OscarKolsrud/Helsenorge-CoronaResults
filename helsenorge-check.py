import sched, time, requests, sys, argparse, os
from twilio.rest import Client

s = sched.scheduler(time.time, time.sleep)

#Parse auto
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--delay", help="Delay between each query in seconds", default=45, type=int)
parser.add_argument("-p", "--phone", help="Delay between each query in seconds", default=None, type=str)
args = parser.parse_args()

# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure. These lines may be commented out to disable phone notification.
# do not pass a --phone param if this is commented out
account_sid = "Put your twilio SID here"
auth_token = "Put your twilio auth token here"
client = Client(account_sid, auth_token)

url = "https://tjenester.helsenorge.no/proxy/Provesvar/api/v1/GetProvesvar"

payload={}

headers = {
    'hnauthenticatedhash': 'hash here, fetch it from network tab in a browser. Look for the API call to https://tjenester.helsenorge.no/proxy/Provesvar/api/v1/GetProvesvar',
    'hnanonymoushash': 'hash here, fetch it from network tab in a browser Look for the API call to https://tjenester.helsenorge.no/proxy/Provesvar/api/v1/GetProvesvar',
    'Cookie': 'cookies here, fetch it from network tab in a browser. Just copy paste all the values inside here Look for the API call to https://tjenester.helsenorge.no/proxy/Provesvar/api/v1/GetProvesvar'
}

delay = args.delay

def ask_helsenorge(sc):
    print("Checking helsenorge...")

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    if (response.text != '{"Provesvar":[]}') & (args.phone is not None):
        message = client.messages.create(body="Results are in: ' " + response.text + " ' Probaly more details at helsenorge.no", from_='CoronaWarn', to=args.phone)

        print("Results ready, sent in SMS to " + args.phone)
        sys.exit()
    elif response.text != '{"Provesvar":[]}':
        print("Results are in!")
        print(response.text)
        print(json.dumps(response.text, indent=1))

    s.enter(delay, 1, ask_helsenorge, (sc,))

print("Script starting with " + str(delay) + " seconds delay between each query.")
if args.phone is not None:
    message = client.messages.create(body="Checking started, we will send a warning when the response from Helsenorge changes", from_='CoronaWarn', to=args.phone)
s.enter(delay, 1, ask_helsenorge, (s,))
s.run()
