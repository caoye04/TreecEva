#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <cmath>
#include <bitset>

class DataProcessor {
private:
    std::map<std::string, std::vector<int>> data;

public:
    void addData(const std::string& key, const std::vector<int>& values) {
        data[key] = values;
    }
    
    int computeWeightedSum(const std::string& key) {
        if (data.find(key) == data.end()) return 0;
        int sum = 0;
        for (size_t i = 0; i < data[key].size(); ++i) {
            sum += data[key][i] * static_cast<int>(std::pow(2, i));
        }
        return sum;
    }
    
    std::string getBinaryString(int value) {
        return std::bitset<32>(value).to_string();
    }
};

int main() {
    DataProcessor processor;
    
    // Initialize data
    std::vector<int> vec1 = {3, -1, 4, 2};
    std::vector<int> vec2 = {1, 5, -2};
    processor.addData("alpha", vec1);
    processor.addData("beta", vec2);
    
    // Compute weighted sums
    int alpha_sum = processor.computeWeightedSum("alpha");
    int beta_sum = processor.computeWeightedSum("beta");
    
    // Bitwise operations
    int xor_result = alpha_sum ^ beta_sum;
    int shifted = xor_result << 2;
    
    // Mathematical computation
    double sqrt_val = std::sqrt(std::abs(shifted));
    int mod_result = static_cast<int>(sqrt_val) % 7;
    
    // String manipulation
    std::string binary_str = processor.getBinaryString(mod_result);
    int count_ones = 0;
    for (char c : binary_str) {
        if (c == '1') count_ones++;
    }
    
    // Final calculation
    int result = (count_ones * 3) + (mod_result ^ 5);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}