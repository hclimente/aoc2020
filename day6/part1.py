forms = open(r'input').read().split('\n\n')
n_yes = [ len(set(x.replace('\n',''))) for x in forms ]
print(sum(n_yes))

