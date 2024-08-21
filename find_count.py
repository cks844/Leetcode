"""Input ='SSSSGGrr', Output = 4S2G2r """
def find_count(inp):
    counts = dict()
    word = inp
    for i in word:
        if i in counts:
            counts[i] += 1
        else:
            counts[i] = 1
    res = ''.join([str(counts[i])+i for i in counts])
    return print(res)
inp ='SSSSGGrr'
find_count(inp)