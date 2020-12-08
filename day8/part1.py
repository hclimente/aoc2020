commands = [ x.split() for x in open(r'input').readlines() ]
commands = [ (cmd, int(inc)) for cmd,inc in commands ]

i = acc = 0
visited = set()
while i not in visited:
    visited.add(i)
    cmd,inc = commands[i]
    i += 1 if cmd in ['acc','nop'] else inc
    acc += inc if cmd == 'acc' else 0

print(acc)
