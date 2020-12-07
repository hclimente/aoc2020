def insides_parser(insides):
    insides = insides.strip('.').split(', ')
    insides = [ x.split(' ') for x in insides ]
    insides = { x[1]+' '+x[2]: int(x[0]) for x in insides if x[0] != 'no' }
    
    return(insides)

rules = open(r'input').read().split('\n')
rules = [ x.replace(' bags','').replace(' bag','') for x in rules ]
rules = [ x.split(' contain ') for x in rules if x ]
rules = { x[0]: insides_parser(x[1]) for x in rules }

def find_shiny(rules, bag):
    
    num_shiny_gold = rules[bag].get('shiny gold', 0)
    
    for new_bag in rules[bag]:
        num_shiny_gold += find_shiny(rules, new_bag)
    
    return(bool(num_shiny_gold))

num_shiny_gold = 0
for bag in rules:
    num_shiny_gold += find_shiny(rules, bag) 

print(num_shiny_gold)
