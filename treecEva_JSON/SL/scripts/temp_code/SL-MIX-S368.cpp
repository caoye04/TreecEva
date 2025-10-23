#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <numeric>
using namespace std;

class SignalPattern {
public:
    int value;
    SignalPattern(int v = 0) : value(v) {}
    
    // Overload + operator
    SignalPattern operator+(const SignalPattern& other) const {
        return SignalPattern((this->value + other.value) % 100);
    }
    
    // Overload * operator
    SignalPattern operator*(const SignalPattern& other) const {
        return SignalPattern((this->value * other.value) % 100);
    }
};

// Function to calculate GCD
int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

// Recursive stabilization function
SignalPattern stabilize(const vector<SignalPattern>& signals, int index) {
    if (index >= signals.size() - 1) return signals[index];
    SignalPattern combined = signals[index] + signals[index+1];
    SignalPattern next = stabilize(signals, index + 1);
    return combined * next;
}

int main() {
    vector<int> raw_signals = {15, 25, 35, 45, 55};
    vector<SignalPattern> modulated_signals;
    
    // Apply modular transformation and create SignalPattern objects
    for (int sig : raw_signals) {
        modulated_signals.push_back(SignalPattern((sig * 3) % 100));
    }
    
    // Stabilize the signal configuration
    SignalPattern stable_configuration = stabilize(modulated_signals, 0);
    int stable_configuration_sum = stable_configuration.value;
    
    // Add mean of original signals adjusted by their GCD
    int sum_original = accumulate(raw_signals.begin(), raw_signals.end(), 0);
    int mean_adjusted = sum_original / raw_signals.size();
    int signal_gcd = raw_signals[0];
    for (size_t i = 1; i < raw_signals.size(); ++i) {
        signal_gcd = gcd(signal_gcd, raw_signals[i]);
    }
    
    stable_configuration_sum += (mean_adjusted + signal_gcd) % 100;
    
    cout << "Result: " << stable_configuration_sum << endl;
    return 0;
}