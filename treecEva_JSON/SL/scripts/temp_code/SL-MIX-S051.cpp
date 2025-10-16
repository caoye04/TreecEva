#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

constexpr bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

constexpr long long fibonacci(int n) {
    if (n <= 1) return n;
    long long a = 0, b = 1, c;
    for (int i = 2; i <= n; ++i) {
        c = a + b;
        a = b;
        b = c;
    }
    return b;
}

int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a % b);
}

int main() {
    std::vector<long long> prime_indexed_fib;
    
    // Generate Fibonacci numbers at prime indices up to 20
    for (int i = 2; i <= 20; ++i) {
        if (is_prime(i)) {
            prime_indexed_fib.push_back(fibonacci(i));
        }
    }
    
    // Sort in descending order
    std::sort(prime_indexed_fib.rbegin(), prime_indexed_fib.rend());
    
    // Greedy selection of coprime pairs
    int verification_checksum = 0;
    for (size_t i = 0; i < prime_indexed_fib.size(); ++i) {
        for (size_t j = i + 1; j < prime_indexed_fib.size(); ++j) {
            // Use ternary to check if numbers are coprime
            bool coprime = (gcd(prime_indexed_fib[i] % 1000, prime_indexed_fib[j] % 1000) == 1) ? true : false;
            if (coprime) {
                // Apply modular arithmetic for checksum
                verification_checksum += (prime_indexed_fib[i] * prime_indexed_fib[j]) % 997;
                verification_checksum %= 997;
                break;
            }
        }
    }
    
    std::cout << "Result: " << verification_checksum << std::endl;
    return 0;
}