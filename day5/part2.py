bps = open('input','r').read().split('\n')

def bp2bin(bp, mapping):
    bp = bp.replace(mapping[0][0], mapping[0][1])
    bp = bp.replace(mapping[1][0], mapping[1][1])
    return(bp)

bin_bps = [ bp2bin(bp[:7], (('F','0'),('B','1'))) + \
            bp2bin(bp[7:], (('L','0'),('R','1'))) for bp in bps if bp ]
bps = { int(bp,2):bp for bp in bin_bps }
sorted_bps = sorted(bps.keys())

for i in range(1, len(bps)):
    k1 = sorted_bps[i - 1]
    k2 = sorted_bps[i]

    if (k2 - k1) == 2:
        my_bp = "{0:b}".format(k1 + 1)
        my_seat = int(my_bp[:7],2) * 8 + int(my_bp[7:],2)
        print(my_seat)

