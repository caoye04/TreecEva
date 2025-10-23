#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <algorithm>
#include <memory>

class Asset {
public:
    int id;
    double expected_return;
    double risk;
    
    Asset(int i, double r, double k) : id(i), expected_return(r), risk(k) {}
    
    // Operator overloading for sorting
    bool operator<(const Asset& other) const {
        return (expected_return / risk) > (other.expected_return / other.risk);
    }
};

double calculate_subportfolio_return(std::vector<Asset>& assets, int start, int end, double risk_limit) {
    if (start > end) return 0.0;
    if (start == end) {
        return assets[start].risk <= risk_limit ? assets[start].expected_return : 0.0;
    }
    
    int mid = start + (end - start) / 2;
    double left_return = calculate_subportfolio_return(assets, start, mid, risk_limit);
    double right_return = calculate_subportfolio_return(assets, mid+1, end, risk_limit);
    
    return left_return + right_return;
}

enum MarketState { BULL, BEAR, STABLE };

int main() {
    std::vector<Asset> portfolio;
    portfolio.emplace_back(1, 8.5, 2.0);
    portfolio.emplace_back(2, 6.2, 1.5);
    portfolio.emplace_back(3, 12.0, 4.0);
    portfolio.emplace_back(4, 4.3, 1.0);
    portfolio.emplace_back(5, 9.7, 3.0);
    
    // Greedy selection based on return-to-risk ratio
    std::sort(portfolio.begin(), portfolio.end());
    
    double risk_budget = 5.0;
    double total_return = 0.0;
    double accumulated_risk = 0.0;
    
    MarketState state = STABLE;
    int transition_counter = 0;
    
    for (auto& asset : portfolio) {
        if (accumulated_risk + asset.risk <= risk_budget) {
            accumulated_risk += asset.risk;
            total_return += asset.expected_return;
            
            // State machine logic
            switch(state) {
                case STABLE:
                    if (asset.expected_return > 8.0) {
                        state = BULL;
                        transition_counter++;
                    }
                    break;
                case BULL:
                    if (asset.risk > 2.5) {
                        state = BEAR;
                        transition_counter++;
                    }
                    break;
                case BEAR:
                    if (asset.expected_return/asset.risk < 3.0) {
                        state = STABLE;
                        transition_counter++;
                    }
                    break;
            }
        }
    }
    
    // Apply divide and conquer refinement
    double refined_return = calculate_subportfolio_return(portfolio, 0, portfolio.size()-1, risk_budget);
    
    // Adjust total return based on state transitions
    total_return = total_return * (1.0 + transition_counter * 0.05) + refined_return * 0.1;
    
    std::cout << "Result: " << static_cast<int>(total_return * 100) << std::endl;
    return 0;
}