test = [2, 5, 9, 6]
ntest = []
buy = min(test)
for i in range(test.index(buy), len(test)):
    ntest.append(test[i])
sell = max(ntest)
prof = sell - buy
print(prof)
