#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <functional>

double calculate_compound_interest(double principal, double rate, int days) {
    return principal * (1 + rate / 100) - principal;
}

int main() {
    std::vector<std::pair<double, double>> accounts = {{1000.0, 2.5}, {1500.0, 3.0}, {2000.0, 1.5}};
    int duration_days = 30;
    
    auto interest_calculator = [](double p, double r, int d) -> double {
        double total = p;
        for (int i = 0; i < d; ++i) {
            total *= (1 + r / 100);
        }
        return total - p;
    };
    
    double total_accumulated_interest = 0.0;
    
    for (const auto& account : accounts) {
        double principal = account.first;
        double rate = account.second;
        
        for (int day = 1; day <= duration_days; ++day) {
            total_accumulated_interest += interest_calculator(principal, rate, 1);
            principal *= (1 + rate / 100); // Update principal for next day's calculation
        }
    }
    
    std::cout << "Result: " << static_cast<long long>(total_accumulated_interest) << std::endl;
    return 0;
}