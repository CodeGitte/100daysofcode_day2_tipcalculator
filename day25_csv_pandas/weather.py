#import libaries
import csv

#open the csv file and declare to a new variable 
file = open("weather_data.csv", "r") 
data = list(csv.reader(file, delimiter=","))
file.close()
print(data)

#making a list with just the temperatures as new entry
temperatures = []
for row in data[1:]: 
    temp = int(row[1])
    temperatures.append(temp)
    
print(temperatures)

####

#column is a series (equivalent to list)
#whole table is dataframe 

import pandas
data = pandas.read_csv("weather_data.csv")
print(data["temp"])

#trying out some methods
data["temp"].astype(int)
average_temp = data["temp"].mean()
print(round(average_temp,2))
max_temp = data["temp"].max()
print(max_temp)

#get data in columns
print(data["condition"])
print(data.condition) #both the same, spelling is important

#get data in row 
print(data[data.day == "Monday"]) #first look for the column, then for the specific row 

#get data row with the highest temperature
print(data[data.temp == data.temp.max()]) #or
print(data[data["temp"] == data["temp"].max()])