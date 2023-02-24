"""
This lesson is for CSV(Comma Separated Values) file and Pandas
"""

# import csv

# with open('weather_data.csv', 'r') as csv_file:
#     # NOTE:readerの場合はrowごとのリストのリストのcsvオブジェクトが返される
#     data = csv.reader(csv_file)
#     print(data)
#     for row in data:
#         if not row[1] == 'temp':
#             row[1] = int(row[1])
#         print(row)

# # NOTE：一行目にカラム名がある場合がほとんどなので、その場合はDictReaderが適している
# with open('weather_data.csv', 'r') as csv_file:
#     data = csv.DictReader(csv_file)
#     print(data)
#     for row in data:
#         print(row)
        
import pandas
from pprint import pprint

# NOTE: pandas:データ解析を支援する機能を提供するライブラリ

# NOTE:pandasで提供される２種類のデータタイプ
# 1.Series：一元データ用の型。イメージは１つのカラム。
# 2.DataFrame：２元データ用の型。Seriesが複数集まったもの。

data = pandas.read_csv('input/weather_data.csv')
# print(data['temp'])
# print(data.temp)

# data_dict = data.to_dict()
# pprint(data_dict)

# data_list = data['temp'].to_list()
# print(data_list)

# print(data['temp'].mean())
# print(data['temp'].max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == 'Monday']
# print(monday.condition)

# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# DataFrameの作成方法
# data_dict = {
#     "student" : ['Amy', 'James', 'Angela'],
#     "score": [76, 56, 65],
# }

# df = pandas.DataFrame(data_dict)
# print(df)

# df.to_csv('output/new_data.csv')

df = pandas.read_csv('input/2018_Central_Park_Squirrel_Census_Squirrel_Data.csv')
gray_squirrels = df[df['Primary Fur Color'] == 'Gray']
red_squirrels = df[df['Primary Fur Color'] == 'Cinnamon']
black_squirrels = df[df['Primary Fur Color'] == 'Black']
num_gray_squirrels = len(gray_squirrels)
num_red_squirrels = len(red_squirrels)
num_black_squirrels = len(black_squirrels)

data_dict = {
    'Fur Color': [
        'Gray',
        'Cinnamon',
        'Black'
    ],
    'Count': [
        num_gray_squirrels,
        num_red_squirrels,
        num_black_squirrels
    ]
}

output_df = pandas.DataFrame(data_dict)
output_df.to_csv("output/squirrels_count.csv")