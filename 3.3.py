#lst = [1, 2, 3, 4, 5, 6] #=> [[1, 2, 3], [4, 5, 6]]
lst = [1, 2, 3] #=> [[1, 2], [3]]
#lst = [1, 2, 3, 4, 5] #=> [[1, 2, 3], [4, 5]]
#lst = [1] #=> [[1], []]
#lst = [] #=> [[], []]
lstvol = len(lst)
if lstvol == 0:
    print([[], []])
else:
    mid = (lstvol + 1) // 2
    print([lst[:mid], lst[mid:]])

