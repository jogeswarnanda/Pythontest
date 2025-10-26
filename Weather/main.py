# with open ("weather_data.csv", "r") as data_file:
#     content = data_file.readlines()

# for name in content:
#     stripped_name = name.strip()
#     print(stripped_name)

# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas
data1 = pandas.read_csv("weather_data.csv")
print(data1)
print(data1["temp"])
data_dict = data1.to_dict()
print(data_dict)
temp_list = data1["temp"].to_list()
print(temp_list)

# sum_temp = sum(temp_list)
# print(sum_temp / len(temp_list))

print(data1["temp"].mean())
print(data1["temp"].max())

#data in row
row1 = data1[data1.day == "Monday"]
print(row1)

maxt = data1[data1.temp == data1["temp"].max()]

monday = data1[data1.day == "Monday"]
monday_temp = monday.temp[0]
monday_temo_f = (monday_temp * 9/5) + 32
print(monday_temp)
print(monday_temo_f)