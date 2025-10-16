#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

double compute_compound_yield(double principal, double rate, int years) {
    return principal * std::pow(1.0 + rate, years);
}

std::vector<int> generate_fibonacci_periods(int max_period) {
    std::vector<int> fib = {1, 1};
    while (true) {
        int next = fib[fib.size()-1] + fib[fib.size()-2];
        if (next > max_period) break;
        fib.push_back(next);
    }
    return fib;
}

int main() {
    double initial_investment = 10000.0;
    std::vector<double> annual_rates = {0.05, 0.03, 0.07, 0.02, 0.06};
    int investment_horizon = 10;
    
    auto fib_periods = generate_fibonacci_periods(investment_horizon);
    double final_yield = initial_investment;
    
    for (int period : fib_periods) {
        if (period > investment_horizon) continue;
        
        double best_rate = 0.0;
        for (double rate : annual_rates) {
            double potential_yield = compute_compound_yield(final_yield, rate, period);
            if (potential_yield > final_yield * std::pow(1.0 + best_rate, period)) {
                best_rate = rate;
            }
        }
        
        final_yield = compute_compound_yield(final_yield, best_rate, period);
    }
    
    std::cout << "Result: " << static_cast<long long>(final_yield) << std::endl;
    return 0;
}