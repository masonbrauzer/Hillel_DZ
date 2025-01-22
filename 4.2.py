lst = [1, 3, 5] #=> 30
#lst = [6] #=> 36
#lst = [] #=> 0
if len(lst) == 0:
    print(0)
else:
    summa = 0
    for a in range(0, len(lst), 2):
        summa += lst[a]
    result = summa * lst[-1]
    print(result)





