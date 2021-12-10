import csv
data1=[]
data2=[]

with open("bright_stars.csv","r")as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data1.append(i)
headers1=data1[0]
starsdata1=data1[1:]
for i in starsdata1:
    i[2]=i[2].lower()        
starsdata1.sort(key=lambda planetdata:planetdata[2])
with open ("datasorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers1)
    csvwriter.writerows(starsdata1)




with open("datasorted.csv","r")as f:
    csvreader=csv.reader(f)
    for i in csvreader:
        data2.append(i)

headers2=data2[0]
starsdata2=data2[1:]
headers=headers1+headers2
starsdata=[]
for index,i in enumerate(starsdata1):
    starsdata.append(starsdata1[index]+starsdata2[index])    
with open ("final.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(starsdata) 