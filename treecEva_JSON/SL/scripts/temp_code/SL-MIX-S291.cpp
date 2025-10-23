#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

class HashComponent {
public:
    long long value;
    
    HashComponent(long long v) : value(v) {}
    
    // Move constructor
    HashComponent(HashComponent&& other) noexcept : value(other.value) {
        other.value = 0;
    }
    
    // Move assignment operator
    HashComponent& operator=(HashComponent&& other) noexcept {
        if (this != &other) {
            value = other.value;
            other.value = 0;
        }
        return *this;
    }
    
    // Overloaded + operator for combining components
    HashComponent operator+(const HashComponent& other) const {
        return HashComponent((value + other.value) % 1000000007);
    }
    
    // Overloaded * operator for scaling
    HashComponent operator*(long long factor) const {
        return HashComponent((value * factor) % 1000000007);
    }
};

long long mod_pow(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

long long gcd(long long a, long long b) {
    while (b != 0) {
        long long temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

long long lcm(long long a, long long b) {
    return (a / gcd(a, b)) * b;
}

bool is_prime(long long n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    for (long long i = 5; i * i <= n; i += 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int main() {
    long long seed = 42;
    long long modulus = 1000000007;
    
    // Initialize components
    HashComponent component1(seed);
    HashComponent component2 = HashComponent(0); // Will be moved to
    
    // Perform modular exponentiation
    long long exp_result = mod_pow(seed, 3, modulus);
    
    // Move temporary result
    HashComponent temp(exp_result);
    component2 = move(temp);
    
    // Combine components
    HashComponent combined = component1 + component2;
    
    // Apply scaling based on a prime factor
    long long prime_factor = 101;
    HashComponent scaled = combined * prime_factor;
    
    // Compute GCD and LCM with another value
    long long other_value = 256;
    long long gcd_result = gcd(scaled.value, other_value);
    long long lcm_result = lcm(scaled.value, other_value);
    
    // Apply logarithmic transformation
    double log_transform = log(static_cast<double>(gcd_result + 1));
    
    // Generate a sequence for statistical analysis
    vector<long long> sequence;
    for (int i = 0; i < 10; i++) {
        long long val = (scaled.value + i * 7) % modulus;
        if (is_prime(val)) {
            sequence.push_back(val);
        }
    }
    
    // Calculate mean of the sequence
    double mean = 0;
    if (!sequence.empty()) {
        for (long long val : sequence) {
            mean += val;
        }
        mean /= sequence.size();
    }
    
    // Calculate variance
    double variance = 0;
    if (!sequence.empty()) {
        for (long long val : sequence) {
            variance += (val - mean) * (val - mean);
        }
        variance /= sequence.size();
    }
    
    // Final aggregated metric combining all transformations
    double aggregate_metric = log_transform + sqrt(variance) + static_cast<double>(lcm_result % 1000);
    
    cout << "Result: " << static_cast<long long>(aggregate_metric) << endl;
    
    return 0;
}