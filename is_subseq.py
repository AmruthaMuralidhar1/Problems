        if len(s) == 0:
            return True
        c = 0
        for i in range(len(t)):
            if t[i] == s[c]:
                c += 1
            if len(s) == c:
                return True
        return False
