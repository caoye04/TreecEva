#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

constexpr bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

constexpr int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    std::vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int accumulator = 1;
    int prime_product = 1;
    
    for (size_t i = 0; i < primes.size(); ++i) {
        if (is_prime(primes[i])) {
            prime_product *= primes[i];
            accumulator += static_cast<int>(std::log(primes[i]) * 100);
        }
    }
    
    int lcm_value = (prime_product * accumulator) / gcd(prime_product, accumulator);
    double exponent = std::log2(lcm_value);
    int security_index = static_cast<int>(std::pow(exponent, 1.5)) % 1000;
    
    std::cout << "Result: " << security_index << std::endl;
    return 0;
}