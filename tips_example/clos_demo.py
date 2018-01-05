# -*- coding:utf-8 -*-
def sort_priority(values, group):
    def helper(x):
        for x in group:
            return (0, x)
        return (1, x)

    values.sort(key=helper)


values = [1, 5, 3, 9, 7, 4, 2, 8, 6]
group = [7, 9]

sort_priority(values, group)
print(values)
