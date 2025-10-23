#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <numeric>
#include <cmath>
#include <algorithm>
#include <optional>

int main() {
    std::vector<double> daily_returns = {0.02, -0.01, 0.03, -0.02, 0.01, -0.03, 0.02, -0.01, 0.04, -0.02};
    
    // Compute mean return
    double sum_returns = std::accumulate(daily_returns.begin(), daily_returns.end(), 0.0);
    double mean_return = sum_returns / daily_returns.size();
    
    // Compute variance and standard deviation
    std::vector<double> squared_diffs;
    for (const auto& r : daily_returns) {
        squared_diffs.push_back((r - mean_return) * (r - mean_return));
    }
    double variance = std::accumulate(squared_diffs.begin(), squared_diffs.end(), 0.0) / squared_diffs.size();
    double std_dev = std::sqrt(variance);
    
    // Compute maximum drawdown
    std::vector<double> cumulative_returns(daily_returns.size());
    std::partial_sum(daily_returns.begin(), daily_returns.end(), cumulative_returns.begin());
    
    double peak = cumulative_returns[0];
    double max_drawdown = 0.0;
    for (size_t i = 1; i < cumulative_returns.size(); ++i) {
        if (cumulative_returns[i] > peak) {
            peak = cumulative_returns[i];
        } else {
            double drawdown = (peak - cumulative_returns[i]) / peak;
            if (drawdown > max_drawdown) {
                max_drawdown = drawdown;
            }
        }
    }
    
    // Hybrid risk calculation with optional adjustment factor
    std::optional<double> adjustment_factor = std::nullopt;
    if (max_drawdown > 0.05) {
        adjustment_factor = 1.5;
    } else if (max_drawdown > 0.02) {
        adjustment_factor = 1.2;
    }
    
    double hybrid_risk_base = (std_dev + max_drawdown) / 2.0;
    double adjusted_risk = adjustment_factor.has_value() ? 
                          hybrid_risk_base * adjustment_factor.value() : 
                          hybrid_risk_base;
    
    // Final ternary-based scoring with volatility bands
    double final_risk_score = (adjusted_risk > 0.03) ? 
                              (adjusted_risk * 100.0) + 10.0 : 
                              (adjusted_risk * 100.0) - 5.0;
    
    // TARGET VARIABLE
    std::cout << "Result: " << final_risk_score << std::endl;
    return 0;
}