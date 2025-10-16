#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>

class GainOptimizer {
private:
    std::vector<double> gainHistory;

public:
    GainOptimizer(std::initializer_list<double> gains) : gainHistory(gains) {}
    
    double computeOptimalGain() && {
        if (gainHistory.empty() || gainHistory.size() > 100) return 0.0;
        
        std::vector<double> dp(gainHistory.size(), 0.0);
        dp[0] = gainHistory[0];
        
        for (size_t i = 1; i < gainHistory.size(); ++i) {
            bool isValid = (gainHistory[i] >= -20.0) && (gainHistory[i] <= 20.0);
            dp[i] = isValid ? std::max(dp[i-1] + gainHistory[i], gainHistory[i]) : dp[i-1];
        }
        
        return dp.back();
    }
};

int main() {
    GainOptimizer processor{3.5, -2.1, 4.8, -0.5, 6.2, -3.3, 1.9};
    double finalGainFactor = std::move(processor).computeOptimalGain();
    std::cout << "Result: " << finalGainFactor << std::endl;
    return 0;
}