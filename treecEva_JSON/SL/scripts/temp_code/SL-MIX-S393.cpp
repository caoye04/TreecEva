#define _USE_MATH_DEFINES
#include <iostream>
#include <functional>
#include <memory>

int compute_volatility_factor(int day) {
    if (day <= 1) return 1;
    return (day % 2 == 0) ? (compute_volatility_factor(day - 1) + 3) : (compute_volatility_factor(day - 1) * 2);
}

int calculate_recursive_risk(std::shared_ptr<int> base_score, int depth) {
    if (depth <= 0) return *base_score;
    auto next_score = std::make_shared<int>(*base_score + compute_volatility_factor(depth));
    return calculate_recursive_risk(next_score, depth - 1);
}

int main() {
    auto initial_score = std::make_shared<int>(10);
    int market_depth = 4;
    int final_adjustment_score = calculate_recursive_risk(initial_score, market_depth);
    std::cout << "Result: " << final_adjustment_score << std::endl;
    return 0;
}