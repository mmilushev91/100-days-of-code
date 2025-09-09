#Python Dictionary consist of key: value pairs

programming_dictionary = {
    "Bug": "A bug in programming refers to an error, flaw, or fault in a computer program that causes it to produce incorrect or unexpected results or to behave in unintended ways.",
    "Function": "A function is a reusable block of code designed to perform a specific task.",
}

#Retrieving a value from Dictionary

print(programming_dictionary["Bug"])

#you can reassign values or create new key value pair
programming_dictionary["Loop"] =  "A loop is a fundamental programming construct designed to executea block of code repeatedly, based on a specified condition."
print(programming_dictionary["Loop"])

#creating new Dictionary
empty_dictionary = {}
empty_dictionary = {"key": "value"}
print(empty_dictionary)

#cleaning key/value pairs from a Dictionary
empty_dictionary = {}
print(empty_dictionary)

#Looping through Dictionary

for key in programming_dictionary:
    print(key) # print keys
    print(programming_dictionary[key]) #print values
    
#-----------------

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested list in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Shtuttgard", "Berlin"],
}

#challenge: print Lille from travel_log

print(travel_log["France"][1])

#Nested lists

nested_list = ["A", "B", ["C", "D"]]

#challenge: letter D 
print(nested_list[2][1])

nested_travel_log = {
    "France": {
        "cities_visited" : ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    
    "Germany": {
        "cities_visited": ["Shtuttgard", "Berlin"],
        "total_visits": 5,
    }
}

#challenge: print Shtuttgard from nested_travel_log
print(nested_travel_log["Germany"]["cities_visited"][0])
