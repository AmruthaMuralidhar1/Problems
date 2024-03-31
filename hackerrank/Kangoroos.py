def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        if x1 == x2:
            return "YES"
        else:
            return "NO"
    else:
        # Time taken for the kangaroos to meet
        t = (x2 - x1) / (v1 - v2)
        # Checking if time is non-negative integer, if they meet at some integer time
        if t >= 0 and t.is_integer():
            return "YES"
        else:
            return "NO"
