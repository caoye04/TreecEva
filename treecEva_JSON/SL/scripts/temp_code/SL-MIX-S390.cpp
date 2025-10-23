#define _USE_MATH_DEFINES
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <climits>

class StockAnalyzer {
public:
    int max_subsequence_gain = INT_MIN;
    int highest_single_change = INT_MIN;
    
    void process(const std::string& data) {
        std::stringstream ss(data);
        std::string token;
        int current_sum = 0;
        
        while (std::getline(ss, token, ',')) {
            int change = std::stoi(token);
            highest_single_change = std::max(highest_single_change, change);
            current_sum = std::max(change, current_sum + change);
            max_subsequence_gain = std::max(max_subsequence_gain, current_sum);
        }
    }
    
    int peak_performance() const {
        return std::max(max_subsequence_gain, highest_single_change);
    }
    
    // Overloaded operator to allow analyzer combination (feature requirement)
    StockAnalyzer operator+(const StockAnalyzer& other) const {
        StockAnalyzer result;
        result.max_subsequence_gain = std::max(max_subsequence_gain, other.max_subsequence_gain);
        result.highest_single_change = std::max(highest_single_change, other.highest_single_change);
        return result;
    }
};

int main() {
    StockAnalyzer analyzer;
    std::string price_changes = "5,-3,2,6,-8,4,7,-1,3";
    analyzer.process(price_changes);
    int peak_performance = analyzer.peak_performance();
    std::cout << "Result: " << peak_performance << std::endl;
    return 0;
}