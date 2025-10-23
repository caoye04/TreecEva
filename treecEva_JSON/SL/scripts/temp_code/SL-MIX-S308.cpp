#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    std::vector<int> primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29};
    int seed = 42;
    int master_key = 0;
    
    auto transform = [&primes](int value, int index) -> int {
        int p = primes[index % primes.size()];
        return is_prime(value) ? value * p : value + p;
    };
    
    for (size_t i = 0; i < primes.size(); ++i) {
        int candidate = transform(seed, i);
        master_key += (candidate > 100) ? (candidate / 2) : (candidate * 2);
        seed = gcd(seed, candidate) > 1 ? seed + candidate : seed ^ candidate;
    }
    
    std::cout << "Result: " << master_key << std::endl;
    return 0;
}