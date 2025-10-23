#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <functional>
#include <cmath>

struct RiskNode {
    double base_risk;
    bool is_high_yield;
    std::vector<RiskNode*> sectors;
    
    RiskNode(double risk, bool high_yield) : base_risk(risk), is_high_yield(high_yield) {}
};

double calculate_portfolio_volatility(RiskNode* root) {
    if (!root) return 0.0;
    
    // Lambda for dynamic risk weighting based on market conditions
    auto risk_weight = [](double base, bool high_yield) -> double {
        return high_yield ? base * 1.5 : base * 0.9;
    };
    
    // Short-circuit evaluation for conditional risk adjustment
    double adjusted_risk = root->is_high_yield && root->base_risk > 0.05 ? 
                          risk_weight(root->base_risk, true) + 0.02 :
                          risk_weight(root->base_risk, root->is_high_yield);
    
    // Aggregate sector risks using STL algorithms
    double sector_contribution = 0.0;
    for (auto& sector : root->sectors) {
        sector_contribution += calculate_portfolio_volatility(sector) * 0.3;
    }
    
    return adjusted_risk + sector_contribution;
}

int main() {
    // Creating a financial portfolio tree
    RiskNode* bonds = new RiskNode(0.03, false);
    RiskNode* stocks = new RiskNode(0.08, true);
    RiskNode* derivatives = new RiskNode(0.12, true);
    
    // High-yield bond sector
    RiskNode* high_yield_bonds = new RiskNode(0.06, true);
    bonds->sectors.push_back(high_yield_bonds);
    
    // Technology stocks sector
    RiskNode* tech_stocks = new RiskNode(0.10, true);
    stocks->sectors.push_back(tech_stocks);
    
    // Derivatives sub-sectors
    RiskNode* options = new RiskNode(0.15, true);
    RiskNode* futures = new RiskNode(0.09, true);
    derivatives->sectors.push_back(options);
    derivatives->sectors.push_back(futures);
    
    // Portfolio root
    RiskNode* portfolio = new RiskNode(0.05, false);
    portfolio->sectors.push_back(bonds);
    portfolio->sectors.push_back(stocks);
    portfolio->sectors.push_back(derivatives);
    
    double portfolio_volatility = calculate_portfolio_volatility(portfolio);
    
    // Clean up memory
    delete high_yield_bonds;
    delete tech_stocks;
    delete options;
    delete futures;
    delete bonds;
    delete stocks;
    delete derivatives;
    delete portfolio;
    
    std::cout << "Result: " << std::round(portfolio_volatility * 10000) / 10000 << std::endl;
    return 0;
}