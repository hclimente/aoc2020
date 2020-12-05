bps = open('input','r').read().split('\n')
bps = [ x for x in bps if x ]

def bin2num(bp, mapping):
    bp = bp.replace(mapping[0][0], mapping[0][1])
    bp = bp.replace(mapping[1][0], mapping[1][1])
    pos = int(bp, 2)

    return(pos)

max_seat_id = 0

for bp in bps:
    seat_id = bin2num(bp[:7], (('F','0'),('B','1'))) * 8 + \
              bin2num(bp[7:], (('L','0'),('R','1')))

    if seat_id > max_seat_id:
        max_seat_id = seat_id

print(max_seat_id)
