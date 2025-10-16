#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <variant>
#include <memory>

double compute_compound_interest(double principal, double rate, int periods) {
    return principal * std::pow(1.0 + rate, periods);
}

int main() {
    std::vector<std::variant<double, int>> interest_rates = {0.05, 0.03, 0.04, 2, 0.06};
    double initial_capital = 1000.0;
    std::unique_ptr<std::vector<double>> dp_table(new std::vector<double>(interest_rates.size() + 1, 0.0));
    
    (*dp_table)[0] = initial_capital;
    
    for (size_t i = 0; i < interest_rates.size(); ++i) {
        std::visit([&](auto&& arg) {
            using T = std::decay_t<decltype(arg)>;
            if constexpr (std::is_same_v<T, double>) {
                (*dp_table)[i+1] = compute_compound_interest((*dp_table)[i], arg, 1);
            } else if constexpr (std::is_same_v<T, int>) {
                // Handle integer as a special case - maybe a bonus period
                double temp_result = compute_compound_interest((*dp_table)[i], 0.02, arg);
                (*dp_table)[i+1] = temp_result;
            }
        }, interest_rates[i]);
    }
    
    // Sort the dp_table in descending order and take the first element as final wealth
    std::sort(dp_table->begin(), dp_table->end(), std::greater<double>());
    double accumulated_wealth = (*dp_table)[0];
    
    std::cout << "Result: " << accumulated_wealth << std::endl;
    return 0;
}