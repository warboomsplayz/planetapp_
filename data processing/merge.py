import csv

with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  data1 = list(reader)
 
with open('data2final.csv', newline="") as g:
  reader = csv.reader(g)
  data2 = list(reader)
 

headers1=data1[0]
planet_data1=data1[1:]

headers2=data2[0]
planet_data2=data2[1:]

headers=headers1+headers2
planet_data=[]
a=1
for i in planet_data1:
  planet_data.append(i+planet_data2[a])
  a=a+2
  
print(planet_data[0])
with open("final.csv", "w") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)