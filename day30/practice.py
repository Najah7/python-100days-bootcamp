"""
This lecture is for Exceptions and json
"""

"""
代表的なExceptions
・KeyError：辞書型のkeyがない
・IndexError：イテレータの指定したインデックスのデータが存在しない
・TypeError：型が違う
・FileNotFound：ファイルが見つからない
・
・
・
・
"""

"""
Catching Exceptions
・try：エラーが起こる可能性がある処理を
・except：Exceptionがあった場合の処理
・else：Exceptionが起こらなかった場合の処理を
・finally：Exceptionが起きても、起きなくても行う処理
"""

"""
if/elseとtry/exceptの使い分け
・if/else：処理を分岐させたいときに使うもの。なので、基本的な分岐を考える場面ではifを使う
・try/except：例外を表すもの。なので、たまに起こるような例外的なものにtryを使う
※まとめ
頻繁に起こるようなエラーハンドルは基本的にif文。
例外的なレアケースにはtry文。

※ほかにも、ifで書くには難しい場合に、tryだと簡単に表せるので、しょうがなくtryを使う場面もある。
"""

try:
    file = open('a_file.txt')
    a_dict = {'key': 'value'}
    # print(a_dict['worng_key'])
except FileNotFoundError: # catchするエラーを指定できる
    file = open('a_file.txt', 'w')
    file.write('There was an error on using file')
except KeyError as error_message:
    # NOTE:keyが格納されている。
    print(f'{error_message} does not exist.')
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed")
    
"""
Rasing Exception
・raise <Exception>
"""

# height = float(input('Height: '))
# weight = int(input("Weight: "))

# if height > 3:
#     raise ValueError("Human height should not be over 3 meters.")

# bmi = weight / height ** 2
# print(bmi)

"""
JSON(JavaScript Object Notation)
Write：json.dump(data, file, indent=0)
Read：json.load(file)
Update(append)：json.update(data)
"""
import json

dict_for_json = {
    'test1': 1,
    'test2': 2,
}

# Write
with open('practice.json', 'w') as json_file:
    json.dump(dict_for_json, json_file, indent=4)

# Read
with open('practice.json', 'r') as json_file:
    json_data = json.load(json_file)
    print(json_data)
    
new_data_for_json = {
    'test3': 3,
}

# Update
with open('practice.json', 'r') as json_file:
    data = json.load(json_file)
    data.update(new_data_for_json)
    
with open('practice.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)
    