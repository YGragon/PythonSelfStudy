import json
from urllib.request import urlopen

def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/"+ipAddress).read().decode('utf-8')
    responseJson = json.loads(response)
    return responseJson.get("country_code")

def getGankInfo():
    filename = 'gank_android.json'
    with open(filename) as f:
        gank_info = json.load(f)

    for gank_data in gank_info:
        who = gank_data['who']
        used = gank_data['used']
        print("who: "+who+"----used: "+used)


getGankInfo()

print(getCountry("50.78.253.58"))


