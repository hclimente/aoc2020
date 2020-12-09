seq = [ int(x) for x in open(r'input').readlines() ]

def overflow(seq, i):
    goal = 1212510616
    addition = 0
    for j in range(i, len(seq)):
        addition += seq[j]
        if addition > goal:
            return(False)
        elif addition == goal:
            print(min(seq[i:j+1]) + max(seq[i:j+1]))
            return(True)

    return(False)

for i in range(len(seq)):
    if overflow(seq, i):
        break

