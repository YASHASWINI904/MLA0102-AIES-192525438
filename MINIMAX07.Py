def minimax(d, i, m):
    if d == 3:
        return a[i]
    if m:
        return max(minimax(d+1, i*2, 0), minimax(d+1, i*2+1, 0))
    return min(minimax(d+1, i*2, 1), minimax(d+1, i*2+1, 1))

a = [3, 5, 2, 9, 12, 5, 23, 23]

print("Best Move =", minimax(0, 0, 1))
