lines = open('input', 'r').read().split('\n')
lines = [ x for x in lines if x ]
parsed = [ x.split(' ') for x in lines ]

correct = 0

for reps, letter, pw in parsed:
    i,j = (int(x) - 1 for x in reps.split('-'))
    letter = letter[0]
    
    correct += (pw[i] == letter) ^ (pw[j] == letter)

print(correct)
