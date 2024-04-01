def breakingRecords(scores):
    minc = maxc = 0
    mn = mx = scores[0]
    for i in scores:
        if mn > i:
            minc += 1
            mn = i
        if mx < i:
            maxc +=1
            mx = i
    return [maxc, minc]
#Julia
function breakingRecords(scores)
    minc = maxc = 0
    mn = mx = scores[1]
    for i in scores
        if i > mx
            mx = i
            maxc = maxc + 1
        end
        if i < mn
            mn = i
            minc +=1
        end
    end
    return [maxc, minc]        
end
