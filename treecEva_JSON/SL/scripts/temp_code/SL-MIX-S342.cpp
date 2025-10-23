#define _USE_MATH_DEFINES
#include <iostream>
#include <queue>
#include <stack>
#include <cmath>
#include <vector>

using namespace std;

template<typename T>
struct RiskComparator {
    bool operator()(const T& a, const T& b) const {
        return a < b; // Max heap
    }
};

template<>
struct RiskComparator<int> {
    bool operator()(const int& a, const int& b) const {
        return a > b; // Min heap for integers
    }
};

int main() {
    priority_queue<double, vector<double>, RiskComparator<double>> riskQueue;
    stack<double> validationStack;
    
    // Initialize risk values
    vector<double> initialRisks = {2.5, 3.7, 1.2, 4.8, 2.1};
    for (double risk : initialRisks) {
        riskQueue.push(risk);
    }
    
    // Process through validation layers
    while (!riskQueue.empty()) {
        double currentRisk = riskQueue.top();
        riskQueue.pop();
        
        // Apply logarithmic scaling
        double scaledRisk = log(currentRisk) * 10.0;
        validationStack.push(scaledRisk);
    }
    
    // Apply exponential adjustment
    vector<double> adjustedRisks;
    while (!validationStack.empty()) {
        double stackValue = validationStack.top();
        validationStack.pop();
        
        double adjustedValue = exp(stackValue / 10.0);
        adjustedRisks.push_back(adjustedValue);
    }
    
    // Re-insert into priority queue with specialized comparator
    priority_queue<int, vector<int>, RiskComparator<int>> integerRiskQueue;
    for (double risk : adjustedRisks) {
        integerRiskQueue.push(static_cast<int>(risk * 1000));
    }
    
    // Final processing with bit manipulation
    int finalRiskScore = integerRiskQueue.top();
    integerRiskQueue.pop();
    
    // Apply bit manipulation - rotate left by 3 positions
    finalRiskScore = (finalRiskScore << 3) | (finalRiskScore >> (32 - 3));
    
    cout << "Result: " << finalRiskScore << endl;
    return 0;
}