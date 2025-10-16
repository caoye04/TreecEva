#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

const int MOD = 998244353;

// Fast exponentiation
long long power(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) result = (result * base) % mod;
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Modular inverse using Fermat's little theorem
long long modInverse(long long a, long long mod) {
    return power(a, mod - 2, mod);
}

// Discrete logarithm (Baby-step Giant-step)
long long discreteLog(long long base, long long value, long long mod) {
    long long m = ceil(sqrt(mod));
    std::vector<std::pair<long long, long long>> baby_steps(m);
    
    long long giant_step = 1;
    for (long long i = 0; i < m; ++i) {
        baby_steps[i] = {giant_step, i};
        giant_step = (giant_step * base) % mod;
    }
    
    std::sort(baby_steps.begin(), baby_steps.end());
    
    long long base_m = power(modInverse(base, mod), m, mod);
    long long gamma = value;
    
    for (long long i = 0; i < m; ++i) {
        auto it = std::lower_bound(baby_steps.begin(), baby_steps.end(), std::make_pair(gamma, 0LL));
        if (it != baby_steps.end() && it->first == gamma) {
            return i * m + it->second;
        }
        gamma = (gamma * base_m) % mod;
    }
    
    return -1; // Not found
}

template<typename T>
class SignalProcessor {
private:
    std::vector<T> signals;
    
public:
    void addSignal(T sig) {
        signals.push_back(sig);
    }
    
    std::vector<T> getTopThree() {
        std::sort(signals.rbegin(), signals.rend());
        if (signals.size() > 3) signals.resize(3);
        return signals;
    }
};

// Custom comparator for sorting by discrete log
struct DiscreteLogComparator {
    bool operator()(const std::pair<long long, long long>& a, const std::pair<long long, long long>& b) {
        return a.first < b.first;
    }
};

int main() {
    SignalProcessor<long long> processor;
    
    // Signal strengths (base^exponent mod MOD)
    std::vector<std::pair<long long, long long>> raw_signals = {{3, 100}, {5, 77}, {2, 200}, {7, 50}, {11, 30}};
    
    // Convert to actual signal values
    for (auto& s : raw_signals) {
        long long signal_value = power(s.first, s.second, MOD);
        processor.addSignal(signal_value);
    }
    
    // Get top three signals
    auto top_signals = processor.getTopThree();
    
    // Calculate discrete logs and sort by them
    std::vector<std::pair<long long, long long>> adjusted_signals; // {discrete_log, original_value}
    for (auto& sig : top_signals) {
        long long dlog = discreteLog(3, sig, MOD); // Using base 3 for discrete log
        adjusted_signals.push_back({dlog, sig});
    }
    
    std::sort(adjusted_signals.begin(), adjusted_signals.end(), DiscreteLogComparator());
    
    // Calculate cumulative resonance of top three adjusted signals
    long long cumulative_resonance = 0;
    for (int i = 0; i < std::min(3, (int)adjusted_signals.size()); ++i) {
        cumulative_resonance = (cumulative_resonance + adjusted_signals[i].second) % MOD;
    }
    
    std::cout << "Result: " << cumulative_resonance << std::endl;
    return 0;
}