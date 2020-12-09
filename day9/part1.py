seq = [ int(x) for x in open(r'input').readlines() ]

def is_sum(x, trail):
    diffs = {}

    for y in trail:
        if y in diffs:
            return(True)
        diffs[x - y] = y

    return(False)

for i in range(25, len(seq)):
    if not is_sum(seq[i], seq[i-25:i]):
        print(seq[i])
        break

