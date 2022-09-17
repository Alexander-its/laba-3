for i in range(105, 701, 7):
    d, u = divmod(i, 10)
    h, d = divmod(d, 10)
    if h + d + u == 7:
        print(i)
