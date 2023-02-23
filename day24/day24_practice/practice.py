# This lesson is for file oprating

# NOTE:Pathについての説明があった
# NOTE:pythonの中では、セパレータを気にする必要ない（Winでも「/」を使える）

# basic useage to read
file = open('my_file.txt', 'r')
contents = file.read()
print(contents)
file.close()

# useage to read with "with statement" 
with open('my_file.txt', 'r') as file:
    contents = file.read()
    print(contents)
    
# basic useage to write
with open('my_file.txt', 'w') as file:
    file.write('Hello Wold\nThis is new text.txt')
    
# basic useage to append
with open('my_file.txt', 'a') as file:
    file.write('\nThis is another text')