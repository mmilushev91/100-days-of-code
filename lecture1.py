#csv file = comma separated values
with open(file="./weather_data.csv", mode="r") as data:
  #create a list of data from the file content separated by new line
  data_list = data.readlines()
  
import csv
with open(file="./weather_data.csv", mode="r") as weather_data_file:
  #returns csv.reader object, which can be iterated over
  data = csv.reader(weather_data_file)
  temperatures = []
  
  for row in data:
    #row is list of data from each row in the file
    if row[1] == "temp":
      continue
    
    temperatures.append(row[1])
  print(temperatures)
    

