# Helsenorge-CoronaResults
### A tool that notifies you automatically regardless of the test result of a Coronavirus test in Helsenorge via Twilio SMS.
This tool was made because i got tired of refreshing Helsenorge waiting for my results after having been exposed to the virus.
Feel free to fork and use for your own purposes.

Apparently Helsenorge has since i wrote this code implemented it themself.


## Known issues
This tool only works if you do not have a previous test result (aka. the array returned from Helsenorge is empty. I may improve it in the future once i know how the response from the API looks.
The process of authentication could also be improved greatly.

## Usage
Stuff to change in code:
You need to update the headers variable with your own vars that you can get from inspecting the network requests when signed in to Helsenorge in order to authenticate to Helsenorge

### CLI Parameters
```
Usage: helsenorge-check.py [-d DELAY] [-d DELAY] session

Arguments:
  -d, --delay            
    (Integer) The delay in seconds between each query, keep this under 300 seconds so you keep the session alive
  -p, --phone (OPTIONAL)          
    (String) The phone number including country code (F.ex. +4712345678). If not passed no SMS will be sent. Twilio is initialized regardless

```

## Requirements (PIP available)
```
twilio
requests
argparse
```
