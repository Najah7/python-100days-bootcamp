with open('file1.txt', 'r') as file1:
    with open('file2.txt', 'r') as file2:
        file1_nums = [int(num) for num in file1.readlines()]
        file2_nums = [int(num) for num in file2.readlines()]

# my answer
# file1_nums_set = set(file1_nums)
# file2_nums_set = set(file2_nums)

# intersection = file1_nums_set.intersection(file2_nums_set)
# intersection_list = list(intersection)
# intersection_list.sort()        

# answer
result = [int(num) for num in file1_nums if num in file2_nums]
result.sort()

print(result)