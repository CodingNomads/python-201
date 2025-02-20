# Write a script that "flattens" a shallow list. For example:
#
# starter_list = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
# flattened_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# Note that your input list only contains one level of nested lists.
# This is called a "shallow list".
#
# CHALLENGE: Do some research online and find a solution that works
# to flatten a list of any depth. Can you understand the code used?

starter_list = [[1, 2, [3], 4], [5, 6], [7, 8, 9]]


def flatten(l):
    if type(l) != type([]):
        return l
    res = []
    for x in l:
        if type(x) != type(l):
            res.append(x)
        else:
            res.extend(flatten(x))
    return res


print(flatten(starter_list))
