def bp2bin(bp, mapping):
    bp = bp.replace(mapping[0][0], mapping[0][1])
    bp = bp.replace(mapping[1][0], mapping[1][1])
    return(bp)

bps = open('input','r').read().split('\n')
bin_bps = [ bp2bin(bp[:7], (('F','0'),('B','1'))) + \
            bp2bin(bp[7:], (('L','0'),('R','1'))) for bp in bps if bp ]
max_bp = sorted(bin_bps)[-1]
print(int(max_bp[:7], 2) * 8 + int(max_bp[7:],2))
