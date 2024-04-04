def wordBreak(self, s, words):
    ok = [True]  # Initialize a list to store boolean values indicating if a substring can be broken into words
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]
