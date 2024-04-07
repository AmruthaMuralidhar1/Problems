        out = []
        t = 0
        cs = ''
        
        for i in s:
            if i.isdigit():
                t = t * 10 + int(i)
            elif i == '[':
                out.append((cs, t))
                cs = ''
                t = 0
            elif i == ']':
                prev_string, prev_number = out.pop()
                cs = prev_string + cs * prev_number
            else:
                cs += i
        
        return cs
