f = open('input', 'r')
nums = [ int(i) for i in f.read().split('\n') if i ]

diffs = {}

for i in nums:
    if i in diffs:
        print(i * diffs[i])
        exit()

    diffs[2020 - i] = i
