import csv
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
#
#     for row in data:
#         # print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
#
# print(data["temp"].mean())
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp])
#
# monday = data[data.day == "Monday"]
#
# temp = int(monday.temp)
# F = temp * 9/5 + 32
# print(F)
#
# data_dict = {
#     "students": ["Munib", "Mawadda", "Yumna"],
#     "scores": [76, 86, 90]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

import csv
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_s_count = len(data[data["Primary Fur Color"] == "Gray"])
black_s_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
cinnamon_s_count = len(data[data["Primary Fur Color"] == "Black"])


data_dict = {
    "Fur color": ["gray", "Cinnamon", "Black"],
    "count": [gray_s_count, cinnamon_s_count, black_s_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")







