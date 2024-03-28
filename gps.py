import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(37.428, -122.145, 16)

gmap.coloricon = "http://www.googlemapsmarkers.com/v1/%s/" # color of the marker

with open("route.csv","r") as f:
    reader = csv.reader(f)
    k = 0

    for row in reader:
        lat = float(row[0])
        lon = float(row[1])
        if k == 0:
            gmap.marker(lat, lon, 'yellow')
            k = 1
        else:
            gmap.marker(lat, lon, 'red')

gmap.marker(lat, lon, 'green')

gmap.draw("mymap.html")