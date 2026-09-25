# Given a dictionary with a values list, extract the key whose value has the most unique
# values.
# Input: test_dict= {"Gfg":[5,7,7,7,7], "is":[6,7,7,7], "Best":[9,9,6,5,5]}
# Output:"Best"
# Explanation:3 (max) unique elements, 9,6,5 of "Best"
D = {"Gfg": [5, 7, 7, 7, 7], "is": [6, 7, 7, 7], "Best": [9, 9, 6, 5, 5]}
max_count = 0
max_key = ""
for key in D:
    count = len(set[int](D[key]))
    if count > max_count:
        max_count = count
        max_key = key
print(f" the dictionary who has more unique values are : {max_key}")


