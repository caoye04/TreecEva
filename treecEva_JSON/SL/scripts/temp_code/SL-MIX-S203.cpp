#define _USE_MATH_DEFINES
#include <iostream>
#include <stack>
#include <queue>
#include <cmath>

constexpr int fibonacci(int n) {
    return (n <= 1) ? n : fibonacci(n - 1) + fibonacci(n - 2);
}

int main() {
    // Delivery data matrix: rows = packages, columns = [weight, distance]
    int deliveryMatrix[3][2] = {{5, 10}, {8, 15}, {12, 20}};
    
    // Calculate initial efficiency score
    double initialScore = 0.0;
    for (int i = 0; i < 3; ++i) {
        int weight = deliveryMatrix[i][0];
        int distance = deliveryMatrix[i][1];
        // Apply Fibonacci weighting based on package index
        int fibWeight = fibonacci(i + 1);
        // Efficiency formula: (weight * distance) / ln(fibWeight + e)
        initialScore += (weight * distance) / log(fibWeight + M_E);
    }
    
    // Stack-based correction: push scores, then apply corrections
    std::stack<double> correctionStack;
    for (int i = 1; i <= 3; ++i) {
        double correctionFactor = pow(initialScore, 1.0/i);
        correctionStack.push(correctionFactor);
    }
    
    // Apply corrections from stack
    double correctedScore = initialScore;
    while (!correctionStack.empty()) {
        correctedScore -= correctionStack.top();
        correctionStack.pop();
    }
    
    // Queue-based final adjustment
    std::queue<int> adjustmentQueue;
    // Calculate combination C(5,2) for adjustment
    int comb = 1;
    for (int i = 0; i < 2; ++i) {
        comb *= (5 - i);
        comb /= (i + 1);
    }
    adjustmentQueue.push(comb);
    
    // Apply final adjustment
    double finalScore = correctedScore + adjustmentQueue.front();
    
    std::cout << "Result: " << static_cast<int>(finalScore) << std::endl;
    return 0;
}