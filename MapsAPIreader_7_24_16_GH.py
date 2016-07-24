import googlemaps
import re
import csv

test1 = open('INSERT YOUR SOURCE PATH')
test2 = csv.reader(test1, quotechar='"',quoting=csv.QUOTE_ALL,skipinitialspace=True)
addresses1 = []
addresses2 = []
addresses3 = []
addresses4 = []
providernum = []

for row in test2:
    addresses1.append(row[2])
    addresses2.append(row[3])
    addresses3.append(row[4])
    addresses4.append(row[5])
    providernum.append(row[0])    
test1.close()

#print(len(addresses1))
#print(addresses1)
#print(addresses1[1])
#print(addresses1[len(addresses1)-1])
gmaps = googlemaps.Client('INSERT YOUR KEY HERE')

latitude = []
longitude = []
j = 1
resultFile = open('INSERT YOUR DESTINATION PATH','a')
resultFile.write("Provider_Number,Latitude,Longitude" + '\n')  #Write your own results headers

for i in range(1,len(addresses1)):
    print(i)
    #if j == 1000:
        #j = 1
        #print(i)
        
    geocode_result = str(gmaps.geocode(addresses1[i]+", "+ addresses2[i] +", " + addresses3[i] + " " + addresses4[i]))

    regex = re.compile("'location': \{u'lat':\s\d+\.\d+, u'lng': -\d+\.\d+")
    var1 = str(regex.findall(geocode_result))
    
    regex2 = re.compile("u'lng'")
    lngloc = re.search(regex2, var1).start()
    lngloc = lngloc - 2
    
    
    regex3 = re.compile("u'lat'")
    latloc = re.search(regex3,var1).start()
    latloc = latloc + 8
    
    latitude.append(var1[latloc:lngloc])
    
    lngloc = lngloc + 10
    longitude.append(var1[lngloc:(len(var1)-2)])
    resultFile.write(str(providernum[i]) + "," + str(latitude[i-1]) + "," + str(longitude[i-1]) + '\n')  
    j = j + 1
    
resultFile.close()