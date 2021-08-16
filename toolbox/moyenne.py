def moyenne (arg):
    mean = 0
    for i in arg:
        mean += i
    mean = mean/len(arg)
    return mean
