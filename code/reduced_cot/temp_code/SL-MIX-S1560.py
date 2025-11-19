import math

def combination(n, r):
    if r > n or r < 0:
        return 0
    return math.comb(n, r)

def permutation(n, r):
    if r > n or r < 0:
        return 0
    return math.perm(n, r)

MOD = 1000000007
signal_strength = [0] * 13
signal_strength[1] = 3
signal_strength[2] = 5

for n in range(3, 13):
    a = combination(10, n % 5 + 1)
    b = permutation(8, n % 4 + 1)
    term1 = pow(signal_strength[n-1], a, MOD) if a else 1
    term2 = pow(signal_strength[n-2], b, MOD) if b else 1
    signal_strength[n] = (term1 * term2) % MOD

# The target signal is the last computed term
lambda_check = lambda x: x if x > 0 else -x
target_signal = lambda_check(signal_strength[12])
print(f"Target result: {target_signal}")