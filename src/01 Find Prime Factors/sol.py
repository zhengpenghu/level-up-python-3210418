
def get_prime_factors(num):
    factors = []
    fac_can = 2
    while num >= fac_can:
        if num % fac_can == 0:
            factors.append(fac_can)
            num /= fac_can
        else:
            fac_can += 1
    return factors
