forms = open(r'input').read().split('\n\n')
forms = [ [ set(y.replace('\n','')) for y in x ] for x in forms ]
n_yes = [ len(set.intersection(*x)) for x in forms ]
print(forms)
print(n_yes)
print(sum(n_yes))

