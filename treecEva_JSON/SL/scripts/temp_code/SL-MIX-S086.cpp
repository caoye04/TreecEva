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
    
    int computeAggregate(const std::string& key) {
        int sum = 0;
        if (data.find(key) != data.end()) {
            for (int val : data[key]) {
                sum += val * static_cast<int>(std::pow(2, val % 3));
            }
        }
        return sum;
    }
};

int main() {
    DataProcessor processor;
    
    // Initialize data
    processor.addData("alpha", {3, 1, 4});
    processor.addData("beta", {2, 7, 1, 8});
    
    // Perform computations
    int a = processor.computeAggregate("alpha");
    int b = processor.computeAggregate("beta");
    
    // Bitwise operations
    int x = (a & b) | ((a ^ b) << 2);
    int y = (~x >> 1) & 0xFF;
    
    // Mathematical transformations
    double dx = static_cast<double>(x);
    double dy = static_cast<double>(y);
    double z = std::sin(dx) * std::cos(dy) + std::log(std::abs(dx - dy) + 1);
    
    // String manipulation
    std::string s1 = std::to_string(static_cast<long long>(std::round(z * 1000)));
    std::string s2 = "12345";
    int concatValue = std::stoi(s1 + s2.substr(2, 3));
    
    // Final computation
    int result = (concatValue % 256) ^ (static_cast<int>(z * 100) & 0x7F);
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}