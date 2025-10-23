#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>

constexpr int parseSignalToken(const std::string& token) {
    int value = 0;
    for (char c : token) {
        value = value * 10 + (c - '0');
    }
    return value;
}

int calculateEfficiencyComponent(int base, int exp) {
    return static_cast<int>(std::pow(base, exp));
}

int main() {
    std::vector<std::string> signalTokens = {"2", "3", "1", "4"};
    std::vector<int> parsedValues(signalTokens.size());
    
    // Parse signal tokens
    for (size_t i = 0; i < signalTokens.size(); ++i) {
        parsedValues[i] = parseSignalToken(signalTokens[i]);
    }
    
    // Dynamic programming table for efficiency calculation
    std::vector<int> dp(parsedValues.size(), 0);
    dp[0] = parsedValues[0];
    
    // Lambda for computing adjusted signal strength
    auto adjustSignal = [](int signal, int index) -> int {
        return signal + (index % 2 == 0 ? 1 : -1);
    };
    
    // Compute dynamic programming values
    for (size_t i = 1; i < parsedValues.size(); ++i) {
        int adjustedValue = adjustSignal(parsedValues[i], static_cast<int>(i));
        dp[i] = dp[i-1] + calculateEfficiencyComponent(adjustedValue, 2);
    }
    
    // Final efficiency calculation with smart pointer
    std::unique_ptr<int> transmission_efficiency = std::make_unique<int>(0);
    for (size_t i = 0; i < dp.size(); ++i) {
        *transmission_efficiency += dp[i] * (i + 1);
    }
    
    std::cout << "Result: " << *transmission_efficiency << std::endl;
    return 0;
}