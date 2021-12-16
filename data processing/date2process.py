import pandas as pd
import csv
data=[]


with open("data2.csv", "r") as f:
    csvreader = csv.reader(f)
    for row in csvreader: 
        data.append(row)

headers=data[0]
planet_data=data[1:]
for i in planet_data:
    i[2]=i[2].lower()
#Sorting planet names in alphabetical order
planet_data.sort(key=lambda planet_data: planet_data[2])
with open("data2final.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)