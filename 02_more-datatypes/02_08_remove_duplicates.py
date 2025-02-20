# Write code that removes all duplicates from a list.
# Solve this challenge in two ways:
# 1. Convert to a different data type
# 2. Use a loop and a second list to solve it more manually

list_ = [1, 2, 3, 4, 3, 4, 5]

res1 = list(set(list_))

res2 = []
for x in list_:
    if x not in res2:
        res2.append(x)

print(res1)
print(res2)
