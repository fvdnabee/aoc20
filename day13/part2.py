# Problem can be reformulated as a set of moduli congruences,
# e.g. 17,x,13,19
# * x cong 0 mod 17,
# * x cong -2 mod 13 = x cong 11 mod 13
# * x cong -3 mod 19 = x cong 16 mod 19
# This can be solved for x via CRT > Search by Sieving, cfr. https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Computation
inp = open('input').read().splitlines()
buses = [int(x) if x != 'x' else 'x' for x in inp[1].split(',')]  # important to keep x's
remainders = [-idx % n if n != 'x' else 'x' for idx, n in enumerate(buses)]

buses = list(filter(lambda a: a != 'x', buses))
remainders = list(filter(lambda a: a != 'x', remainders))

x = 0  # the earliest timestamp we see
prod_ns = 1  # keep a running product of the moduli
for i in range(1, len(buses)):
    n_i = buses[i]  # new x must satisfy that its remainder after division by n_i is equal to remainders[i]
    n_i_1 = buses[i-1]  # 'previous' divisor
    prod_ns *= n_i_1
    for j in range(n_i):  # as we calculate moduli n_i, we only need to loop up to n_i
        # add multiples of prod_ns to x as it is the only option that satifies all moduli congruences that were already processed
        if (new_x := x + j*prod_ns) % n_i == remainders[i]:
            x = new_x
            break

print(x)
