lines = open('input', 'r').read().split('\n')
lines = [ x for x in lines if x ]
parsed = [ x.split(' ') for x in lines ]

correct = 0

for reps, letter, pw in parsed:
    minr,maxr = (int(x) for x in reps.split('-'))
    letter = letter[0]
    
    reps = 0
    for c in pw:
        reps += c == letter

    correct += reps >= minr and reps <= maxr

print(correct)
