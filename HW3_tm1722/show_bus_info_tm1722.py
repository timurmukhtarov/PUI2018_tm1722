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
print(url)

#Loading in as data
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)

# Isolate only data we need
bus_app = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
bus_number = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']\
    [0]['MonitoredVehicleJourney']['PublishedLineName']

# Print the number of the bus route chosen by the user
print('Bus Line :', bus_number)

# Print the number of active buses
total_count = 0
for i in bus_app:
    total_count+=1
print('Number of Active Buses :', total_count)

# Print the latitude and longitude for every bus of the bus route
counter = 0
for i in bus_app:
    counter += 1
    print('Bus', str(counter), 'is at latitude:', i['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], \
          'Longitude', i['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
