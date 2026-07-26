import math

def ab(d, i, m, a, b):
    if d == 3:
        return s[i]

    if m:
        v = -math.inf
        for j in range(2):
            v = max(v, ab(d+1, i*2+j, 0, a, b))
            a = max(a, v)
            if a >= b:
                break
        return v
    else:
        v = math.inf
        for j in range(2):
            v = min(v, ab(d+1, i*2+j, 1, a, b))
            b = min(b, v)
            if a >= b:
                break
        return v

s = [3, 5, 6, 9, 1, 2, 0, -1]

print("Best Move =", ab(0, 0, 1, -math.inf, math.inf))
