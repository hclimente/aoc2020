f = open('input', 'r')
nums = [ int(i) for i in f.read().split('\n') if i ]

diffs = {}

for i in nums:
    for j in nums:
        if j in diffs:
            print(j * diffs[j][0] * diffs[j][1])
            exit()
        diffs[2020 - i - j] = (i,j) 
