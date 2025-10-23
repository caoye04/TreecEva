#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

constexpr long long mod_exp(long long base, long long exp, long long mod) {
    long long result = 1;
    base %= mod;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp >>= 1;
    }
    return result;
}

long long xor_shift_reduce(long long value, int shift) {
    return (value ^ (value >> shift)) & 0xFFFF;
}

long long recursive_validator(long long n, long long acc) {
    if (n <= 1) return acc;
    long long next = (n % 2 == 0) ? n / 2 : 3 * n + 1;
    return recursive_validator(next, acc ^ n);
}

int main() {
    long long seed = 1337;
    long long modulus = 100000007;
    long long exponent = 293847;
    
    // Step 1: Compute modular exponentiation
    long long mod_result = mod_exp(seed, exponent, modulus);
    
    // Step 2: Apply XOR-shift reduction
    long long reduced = xor_shift_reduce(mod_result, 8);
    
    // Step 3: Recursive validation with accumulator
    long long validated = recursive_validator(reduced, 0);
    
    // Step 4: Final transformation with bitwise operations
    long long authToken = ((validated << 3) | (validated >> 5)) & 0xFFFFFFFF;
    
    std::cout << "Result: " << authToken << std::endl;
    return 0;
}