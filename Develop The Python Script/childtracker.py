from http import client
import json
import wiotp.sdk.device
import time
myConfig = {
    "identify":{
        "orgId":"hj5fmy",
        "typeId":"NodeMCU",
        "deviceId":"12345678"
    },
    "auth":{
        "token":"12345678"
    }
}
client = wiotp.sdk.device.DeviceClient(config=myConfig, logHandlers=None)
client.connect()
while True:
    name= "Smartbridge"
    #in area location
    #latitude=17.4225176
    #longitude 78.5458842
    #out area location
    latitude=17.4219272
    longitude=78.5488783
    myData={'name': name, 'lat': latitude, 'lon': longitude}
    client.publishEvent(eventId="status", msgFormat="json", data=myData, qos-0, onPublish=None)
    print("Data published to IBM IOT platfrom: ",myData)
    time.sleep(5)

client.disconnect()