import copy

commands = open(r'input').read().strip('\n').split('\n')
commands = [ [x.split(' ')[0], int(x.split(' ')[1])] for x in commands ]
switches = {'nop': 'jmp', 'jmp': 'nop'}

def explore_tree(commands, switch, visited, i, acc):

    while True:
        if i in visited:
            return(0)
        elif i >= len(commands):
            return(acc)
        cmd,inc = commands[i] 
        
        if switch and (cmd in switches):
            commands_cpy = copy.deepcopy(commands)
            commands_cpy[i][0] = switches[commands_cpy[i][0]]
            dacc = explore_tree(commands_cpy, False, visited, i, acc)
            if dacc:
                return(dacc)

        visited.add(i)
        i += 1 if cmd in ['acc','nop'] else inc
        print(' ' * int(not switch), cmd, inc, acc)
        acc += inc if cmd == 'acc' else 0
    
print(explore_tree(commands, True, set(), 0, 0))
