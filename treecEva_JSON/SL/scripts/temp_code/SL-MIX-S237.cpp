#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <functional>

template<typename T>
struct InvestmentNode {
    T riskFactor;
    InvestmentNode* left;
    InvestmentNode* right;
    
    InvestmentNode(T factor) : riskFactor(factor), left(nullptr), right(nullptr) {}
};

template<typename T>
class RiskEvaluator {
public:
    std::function<bool(T, T)> riskComparator;
    
    RiskEvaluator() {
        // Lambda to evaluate if risk is within acceptable bounds
        riskComparator = [](T current, T threshold) -> bool {
            return (current < threshold) && (current > 0.0);
        };
    }
    
    bool assessRisk(T primaryFactor, T secondaryFactor, T tolerance) {
        bool primaryCheck = riskComparator(primaryFactor, tolerance);
        bool secondaryCheck = riskComparator(secondaryFactor, tolerance * 1.5);
        
        // Complex logical operation combining AND/OR
        return (primaryCheck || secondaryCheck) && !(primaryCheck && secondaryCheck);
    }
};

int main() {
    // Build investment tree
    InvestmentNode<double>* root = new InvestmentNode<double>(2.5);
    root->left = new InvestmentNode<double>(1.8);
    root->right = new InvestmentNode<double>(3.2);
    root->left->left = new InvestmentNode<double>(0.9);
    root->left->right = new InvestmentNode<double>(2.1);
    
    RiskEvaluator<double> evaluator;
    double toleranceLevel = 2.0;
    
    // Calculate risk scores through tree traversal
    double aggregateRisk = 0.0;
    aggregateRisk += root->riskFactor * 0.5;
    aggregateRisk += root->left->riskFactor * 0.3;
    aggregateRisk += root->right->riskFactor * 0.7;
    aggregateRisk += root->left->left->riskFactor * 0.2;
    aggregateRisk += root->left->right->riskFactor * 0.4;
    
    // Apply risk assessment logic
    bool riskStatus = evaluator.assessRisk(root->riskFactor, root->left->riskFactor, toleranceLevel);
    
    // Final calculation incorporating floating point operations and logical results
    double adjustmentFactor = riskStatus ? 1.25 : 0.75;
    double finalRiskScore = aggregateRisk * adjustmentFactor + std::sin(M_PI/6.0);
    
    // Clean up memory
    delete root->left->left;
    delete root->left->right;
    delete root->left;
    delete root->right;
    delete root;
    
    std::cout << "Result: " << finalRiskScore << std::endl;
    return 0;
}