def birthdayCakeCandles(candles):
    # Write your code here
    t = max(candles)
    count = 0
    for i in range(len(candles)):
        if candles[i] == t:
            count += 1
    return count

#time complixity = O(n) 

#Julia Language
function birthdayCakeCandles(candles)
    # Write your code here
    t = maximum(candles)
    count = 0
    for i in 1:length(candles)
        if candles[i] == t
            count += 1
        end
    end
    return count
end
