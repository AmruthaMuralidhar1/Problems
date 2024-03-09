test = [1, 2, 3, 0]
test.sort()
for i in range (0, len(test)):
    if test[i] == test[i+1]:
        print("true")
        break
# time for sort is O(nlogn) + time for for loop is O(n)  = O(nlogn)

#USING HASHMAPS
test = [1, 2, 3, 0, 4, 2, 2]
h = {}
for i, v in enumerate(test):
    if v in h.values():
        print("true")
        break
    h[i] = v
    
