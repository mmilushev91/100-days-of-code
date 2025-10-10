import pandas 

squirrel_data_frame = pandas.read_csv("./squirrel_data.csv")
color_squirrel_list = squirrel_data_frame["Primary Fur Color"].to_list()

gray_color_count = color_squirrel_list.count("Gray")
black_color_count = color_squirrel_list.count("Black")
cinnamon_color_count = color_squirrel_list.count("Cinnamon")

data_dict = {
  "Fur color count": ["Gray", "Black", "Cinnamon"],
  "Count": [gray_color_count, black_color_count, cinnamon_color_count]
}

filtered_data = pandas.DataFrame(data_dict)
print(filtered_data)
filtered_data.to_csv("suirrel_count.csv")
