required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = [ x.split(' ') for x in open('input', 'r').read().split('\n') ]

valid = 0
valid_fields = 0

for p in passports:
    if p == ['']:
        if valid_fields == len(required_fields):
            valid += 1
        valid_fields = 0

    valid_fields += sum([ (x[0:3] in required_fields) for x in p ])

print(valid)
