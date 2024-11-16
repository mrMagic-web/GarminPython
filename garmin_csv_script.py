import csv
import arcpy
import csv
from datetime import datetime

arcpy.CreateFeatureClass_management("", "garmin_shapefile_.shp", "POINT")

# Open the CSV file in read mode
with open('B21C0631.csv', mode='r', newline='') as file:
    reader = csv.reader(file, delimiter=',')

    cords_list = []
    for row in reader:
        if row[1] == '7':
            position_lat_degrees = int(row[7]) * (100 / 2 ** 31)
            position_long_degrees =  int(row[10]) * (100 / 2 ** 31)
            dt = datetime.fromtimestamp(int(row[4]))

            cords_list.append((position_lat_degrees,position_long_degrees, (dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)))

    print(cords_list)