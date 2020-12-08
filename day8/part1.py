commands = open(r'input').read().strip('\n').split('\n')
commands = [ (x.split(' ')[0], int(x.split(' ')[1])) for x in commands ]

i = acc = 0
visited = set()
while i not in visited:
    visited.add(i)
    cmd,inc = commands[i]
    i += 1 if cmd in ['acc','nop'] else inc
    acc += inc if cmd == 'acc' else 0

print(acc)
