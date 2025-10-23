#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

constexpr long long mod_power(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

int main() {
    std::vector<int> candidate_primes = {11, 13, 17, 19, 23, 29, 31};
    std::vector<double> prime_scores(candidate_primes.size());
    
    // Calculate logarithmic scores for each prime
    for (size_t i = 0; i < candidate_primes.size(); ++i) {
        prime_scores[i] = std::log(candidate_primes[i]) * 100;
    }
    
    // Sort primes by their scores in descending order using lambda
    std::vector<std::pair<double, int>> score_prime_pairs;
    for (size_t i = 0; i < candidate_primes.size(); ++i) {
        score_prime_pairs.push_back({prime_scores[i], candidate_primes[i]});
    }
    
    std::sort(score_prime_pairs.begin(), score_prime_pairs.end(), 
              [](const std::pair<double, int>& a, const std::pair<double, int>& b) {
                  return a.first > b.first;
              });
    
    // Greedy selection: pick top 3 primes
    long long derivedKey = 1;
    const long long MOD = 1000000007;
    
    for (int i = 0; i < 3; ++i) {
        int prime = score_prime_pairs[i].second;
        int exponent = static_cast<int>(std::floor(std::log2(prime)));
        derivedKey = (derivedKey * mod_power(prime, exponent, MOD)) % MOD;
    }
    
    std::cout << "Result: " << derivedKey << std::endl;
    return 0;
}