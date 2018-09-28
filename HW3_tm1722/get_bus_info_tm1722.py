# Import modules needed
from __future__ import print_function
import json
import pylab as pl
import os
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# Access API with parameters given by the user when running the file
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+sys.argv[1]+"&VehicleMonitoringDetailLevel=calls&LineRef="+sys.argv[2]

#Loading in as data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Zoom in on data we need
bus_app2 = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

# Get data for Latitude, Longitude, Stop Name ("StopPointName"), Stop Status ("PresentableDistance")  
s="Latitude,Longitude,Stop Name,Stop Status\n"
for i in bus_app2:    
    i =i['MonitoredVehicleJourney']
    printout = str(i['VehicleLocation']['Latitude'])+','+\
    str(i['VehicleLocation']['Longitude'])+','
    if len(i['OnwardCalls']) < 1:
        s = s +str(printout)
        s =s +'N/A \n'
        continue   
    printout = printout +str(i['OnwardCalls']['OnwardCall'][0]['StopPointName'])+','\
    +str(i['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    s = s +str(printout) +'\n'
print(s)

# Save to csv
f = open(sys.argv[3],'w')
f.write(s) # Python will convert \n to os.linesep
f.close()
