#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (int i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int smallest_prime_factor(long long num) {
    if (num <= 1) return -1;
    for (int i = 2; i <= sqrt(num) + 1; ++i) {
        if (num % i == 0 && is_prime(i)) {
            return i;
        }
    }
    if (is_prime(num)) return num;
    return -1;
}

int euler_totient(int p) {
    if (is_prime(p)) {
        return p - 1;
    }
    return 0; // Not prime
}

int main() {
    int hash_evaluation_score = 0;
    for (int n = 5; n <= 9; ++n) {
        long long mersenne_like = (1LL << n) - 1; // 2^n - 1
        int spf = smallest_prime_factor(mersenne_like);
        if (spf != -1) {
            hash_evaluation_score += euler_totient(spf);
        }
    }
    std::cout << "Result: " << hash_evaluation_score << std::endl;
    return 0;
}