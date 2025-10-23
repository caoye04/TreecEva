#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>

int main() {
    double initial_principal = 1000.0;
    std::vector<double> daily_rates = {0.01, 0.02, 0.015, 0.03, 0.025};
    
    // Apply dynamic programming to calculate daily balances
    std::vector<double> dp(daily_rates.size() + 1);
    dp[0] = initial_principal;
    
    for (size_t i = 1; i <= daily_rates.size(); ++i) {
        dp[i] = dp[i-1] * (1 + daily_rates[i-1]);
        // Conditional weekend bonus (indices 6 and 7 represent weekend days)
        if (i == 6 || i == 7) {
            dp[i] *= 1.05; // 5% weekend bonus
        }
    }
    
    double final_balance = dp[daily_rates.size()];
    
    // Using RAII pattern for resource management via lambda
    auto cleanup_and_report = [&final_balance]() {
        std::cout.precision(10);
        std::cout << "Result: " << final_balance << std::endl;
        return 0;
    };
    
    return cleanup_and_report();
}