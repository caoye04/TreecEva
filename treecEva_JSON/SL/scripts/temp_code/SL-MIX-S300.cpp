#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>

constexpr long long fibonacci_mod(int n, int mod) {
    if (n <= 1) return n;
    long long a = 0, b = 1;
    for (int i = 2; i <= n; ++i) {
        long long temp = (a + b) % mod;
        a = b;
        b = temp;
    }
    return b;
}

class SignalProcessor {
private:
    std::vector<long long> signal_data;
    int modulation_base;

public:
    SignalProcessor(int base) : modulation_base(base) {}
    
    void generate_signals(int count) {
        signal_data.reserve(count);
        for (int i = 1; i <= count; ++i) {
            long long fib_val = fibonacci_mod(i*2, 1000000007);
            long long modulated = fib_val ^ (i << 2);
            signal_data.push_back(modulated);
        }
    }
    
    long long greedy_selection() {
        std::sort(signal_data.begin(), signal_data.end(), std::greater<long long>());
        long long accumulator = 0;
        for (size_t i = 0; i < signal_data.size(); ++i) {
            if ((accumulator & signal_data[i]) > 0) {
                accumulator ^= signal_data[i];
            } else {
                accumulator += signal_data[i];
            }
        }
        return accumulator;
    }
    
    ~SignalProcessor() = default;
};

int main() {
    auto processor = std::make_unique<SignalProcessor>(1000000007);
    processor->generate_signals(12);
    long long selected_signal_strength = processor->greedy_selection();
    std::cout << "Result: " << selected_signal_strength << std::endl;
    return 0;
}