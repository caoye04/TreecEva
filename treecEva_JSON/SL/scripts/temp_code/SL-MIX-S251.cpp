#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <cmath>
#include <optional>

double calculate_mean(const std::vector<double>& values) {
    double sum = 0.0;
    for (const auto& val : values) {
        sum += val;
    }
    return sum / values.size();
}

double calculate_variance(const std::vector<double>& values, double mean) {
    double sum_sq_diff = 0.0;
    for (const auto& val : values) {
        sum_sq_diff += (val - mean) * (val - mean);
    }
    return sum_sq_diff / values.size();
}

std::optional<double> parse_transaction(const std::string& transaction) {
    try {
        size_t pos;
        double value = std::stod(transaction, &pos);
        if (pos == transaction.length()) {
            return value;
        } else {
            return std::nullopt;
        }
    } catch (...) {
        return std::nullopt;
    }
}

int main() {
    std::vector<std::string> raw_transactions = {"100.50", "200.75", "invalid", "150.25", "300.00", "175.80"};
    std::vector<double> valid_transactions;
    
    for (const auto& tx : raw_transactions) {
        auto parsed = parse_transaction(tx);
        if (parsed.has_value()) {
            valid_transactions.push_back(parsed.value());
        }
    }
    
    double mean = calculate_mean(valid_transactions);
    double variance = calculate_variance(valid_transactions, mean);
    
    // Risk adjustment logic
    double risk_factor = 1.0;
    if (variance > 5000.0) {
        risk_factor = 1.2;
    } else if (variance > 2000.0) {
        risk_factor = 1.1;
    }
    
    double adjusted_variance = variance * risk_factor;
    
    std::cout << "Result: " << adjusted_variance << std::endl;
    return 0;
}