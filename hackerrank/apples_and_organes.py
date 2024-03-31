def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_apples = sum(s <= a + d <= t for d in apples)
    count_oranges = sum(s <= b + d <= t for d in oranges)
    print(count_apples)
    print(count_oranges)

#julia
function countApplesAndOranges(s, t, a, b, apples, oranges)
    counta = sum(s<=i+a<=t for i in apples)
    counto = sum(s<=j+b<=t for j in oranges)
    println(counta)
    println(counto)
end

def countApplesAndOranges(s, t, a, b, apples, oranges):
    counta = counto = 0 
    for i in range(len(apples)):
        apples[i] += a
        if s <= apples[i] <= t:
            counta += 1
    for j in range(len(oranges)):
        oranges[j] += b
        if s <= oranges[j] <= t:
            counto += 1
    print(counta)
    print(counto)

#what i first types and got correct
def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    counta = counto = 0 
    for i in range (len(apples)):
        apples[i] = a + apples[i]
    for j in range (len(oranges)):
        oranges[j] = b + oranges[j]
    for i in range (len(apples)):
        if (apples[i] >= s and apples[i] <= t):
            counta = counta + 1
    for j in range (len(oranges)):
        if (oranges[j] >= s and oranges[j] <= t):
            counto = counto + 1
    print(counta)
    print(counto)
