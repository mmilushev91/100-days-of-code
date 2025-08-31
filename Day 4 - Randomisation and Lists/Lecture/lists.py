#Lists

#lists contain related ordered values
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", 
    "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", 
    "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", 
    "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", 
    "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", 
    "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota",
    "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", 
    "Arizona", "Alaska", "Hawaii"]
#You can get an item from the list using index. Index represents the offset of the element
#in respect to the first item. That is why first item is always with index 0 and last is
#len of the list - 1
print(states_of_america[0]) #Delaware
#with negative indexes that counting starts from the end. -1 is the last item
print(states_of_america[-1]) #Hawaii
#you can change the value of the desired offset position by assigning it a new value
states_of_america[1] = "Pencilvania"
#append(item) adds the item at them of list
states_of_america.append("Marian Land")
#extend([item1, item2]) adds list items at the of the list
states_of_america.extend(["Land1", "Land2"])
