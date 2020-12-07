def insides_parser(insides):
    insides = insides.strip('.').split(', ')
    insides = [ x.split(' ') for x in insides ]
    insides = { x[1]+' '+x[2]: int(x[0]) for x in insides if x[0] != 'no' }
    
    return(insides)

rules = open(r'input').read().split('\n')
rules = [ x.replace(' bags','').replace(' bag','') for x in rules ]
rules = [ x.split(' contain ') for x in rules if x ]
rules = { x[0]: insides_parser(x[1]) for x in rules }

def get_nbags(rules, bag):
    
    num_bags = 0

    for new_bag, reps in rules[bag].items():
        num_bags += reps
        num_bags += reps * get_nbags(rules, new_bag)

    return(num_bags)

num_bags = get_nbags(rules, 'shiny gold') 

print(num_bags)
