
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import requests
import json
import time
import simplejson
from time import gmtime, strftime
from datetime import datetime, timedelta
from cassandra.cluster import Cluster

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

base_url = "https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson"


def writeFile(fileName, data):
    """Write the information to a file"""
    print("###Writing file")
    with open("./"+fileName, 'w') as outfile:
        json.dump(data, outfile, indent=0, sort_keys=True)


def printLog(msg):
    print(strftime("%d-%m-%Y %H:%M:%S", gmtime()), "->", msg)

def getX(longitude):
    x = 0

    if 0 <= longitude < 30:
        x = 1
    elif 30 <= longitude < 60:
        x = 2
    elif 60 <= longitude < 90:
        x = 3
    elif 90 <= longitude < 120:
        x = 4
    elif 120 <= longitude < 150:
        x = 5
    elif 150 <= longitude <= 180:
        x = 6
    elif -180 <= longitude < -150:
        x = 7
    elif -150 <= longitude < -120:
        x = 8
    elif -120 <= longitude < -90:
        x = 9
    elif -90 <= longitude < -60:
        x = 10
    elif -60 <= longitude < -30:
        x = 11
    elif -30 <= longitude < 0:
        x = 12
    return x


def getY(latitude):
    y = 0

    if 60 <= latitude < 80:
        y = 1
    elif 40 <= latitude < 60:
        y = 2
    elif 20 <= latitude < 40:
        y = 3
    elif 0 <= latitude < 20:
        y = 4
    elif -20 <= latitude < 0:
        y = 5
    elif -40 <= latitude < -20:
        y = 6
    elif -60 <= latitude < -40:
        y = 7
    elif -80 <= latitude < -60:
        y = 8
    elif latitude < -80:
        y = 8
    elif 80 <= latitude:
        y = 1
  
    return y



def insertIntoDB(data):
    eventId = data.get("id")
    properties = data.get("properties")
    location = data.get("geometry")
    latitude = location.get("coordinates")[1]
    longitude = location.get("coordinates")[0]
    depth = location.get("coordinates")[2]
    magnitude = properties["mag"]
    time = properties["time"]
    place = properties["place"]
    fecha = datetime.fromtimestamp(float(properties["time"])/1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    geoJson = str(data)
    quadrantX = getX(float(longitude))
    quadrantY = getY(float(latitude))
    quadrantXY = str(quadrantX)+","+str(quadrantY)

    magnitude = float(str(magnitude).replace(",", ".")) if not (magnitude is None) else None
    depth = float(str(depth).replace(",", ".")) if not (depth is None) else None

    if str(place) and str(time):
        session.execute("INSERT INTO Earthquake (\"eventId\",\"place\",\"time\",\"fecha\",\"magnitude\",\"depth\",\"longitude\",\"latitude\",\"geojson\",\"quadrant\",\"quadrantX\", \"quadrantY\") \
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)",
        [str(eventId), str(place), str(time), fecha, magnitude, depth, longitude, latitude, geoJson,quadrantXY,int(quadrantX),int(quadrantY)])


def getEarthQuakesWorld(yearFrom):

    now = datetime.now()
    while yearFrom <= now.year:
        startDateStr = str(yearFrom)+"-01-01"
        endDateStr = str(yearFrom)+"-12-31"

        try:
            getData(startDateStr,endDateStr)
        except simplejson.scanner.JSONDecodeError:
            printLog("####ERROR!!!"+str(yearFrom))
            getDataMonthly(yearFrom)
        finally:
            yearFrom = yearFrom+1


def getDataMonthly(yearFrom):
    for i in range(1, 12):
        startDateStr = str(yearFrom)+"-"+str(i)+"-01"
        endDateStr = str(yearFrom)+"-"+str((i+1)%13)+"-01"
        getData(startDateStr, endDateStr)
        time.sleep(10)


def getData(fromDate, toDate):
    url = "&starttime="+fromDate+"&endtime="+toDate
    printLog("Calculating from "+str(fromDate)+" to " + str(toDate))
  
    response = requests.get(base_url+url)
    jsonData = response.json()
    for feature in jsonData.get("features"):
        properties = feature.get("properties")
        dateTime =  datetime.fromtimestamp(float(properties["time"])/1000).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        try:
            printLog("Processing :" + str(properties["place"])+" for: " + str(dateTime))
            insertIntoDB(feature)
        except UnicodeEncodeError:
            printLog("Bad encoding")



# Main Function #
if __name__ == "__main__":
    cluster = Cluster(['192.168.246.236'])
    session = cluster.connect("dev")
    getEarthQuakesWorld(2017)
    printLog("END")
