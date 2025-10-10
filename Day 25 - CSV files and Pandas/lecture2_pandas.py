import pandas 

#creates table from csv file
weather_data = pandas.read_csv(filepath_or_buffer="./weather_data.csv")
#getting column from table using header name
print(weather_data["temp"])
#alternatively you can use dot notaition with the name of the column after the dot
print(weather_data.temp)
#pandas use two types of data structures: series and dataframes
#series is a column in a table, and it is one dimensional
#dataframe is a table in a table - two dimensional. It is a collection of series

#converting dataframe to dictionary
data_dict = weather_data.to_dict()
print(data_dict)

#converts data series to a list
temp_list = weather_data["temp"].to_list()

print(temp_list)

# average_temp = sum(temp_list) / len(temp_list)
average_temp = weather_data["temp"].mean()
print(f"Average temp is: {average_temp:.2f}")

#getting row
first_row = weather_data[weather_data.day == "Monday"]
print(first_row)

#getting row with highest temp
max_temp = weather_data["temp"].max()
print(max_temp)
print("----------------------")
highest_temp_row = weather_data[weather_data.temp == max_temp]
print("----------------------")
print(f"Highest temp row: {highest_temp_row}")
print("----------------------")
print()
temperatureInFar = (highest_temp_row.temp.values[0]* 1.8) + 32
print(f"Temp in farenheit: {temperatureInFar}")

data_dict = {
  "students": ["Marian", "Monika", "Martin"],
  "scores": [95, 93, 92]
}

#create new dataframe
dict_data = pandas.DataFrame(data_dict)
dict_data.to_csv("dict_data.csv")
print(dict_data)
