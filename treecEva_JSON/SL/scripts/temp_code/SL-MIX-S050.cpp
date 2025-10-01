#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <map>
#include <cmath>
#include <string>

class DataProcessor {
private:
    std::map<int, std::vector<int>> data_map;
public:
    void insert(int key, const std::vector<int>& values) {
        data_map[key] = values;
    }
    
    int process() {
        int sum = 0;
        for (const auto& pair : data_map) {
            int sub_sum = 0;
            for (int val : pair.second) {
                sub_sum += (val ^ (val >> 1)); // Gray code transformation
            }
            sum += (pair.first * sub_sum);
        }
        return sum;
    }
};

int main() {
    DataProcessor processor;
    
    // Initialize data
    processor.insert(3, {15, 27, 9});
    processor.insert(7, {12, 6, 18, 24});
    processor.insert(2, {30, 45});
    
    // Perform processing
    int intermediate = processor.process();
    
    // Apply mathematical transformations
    double temp = std::pow(intermediate, 1.0/3.0); // Cube root
    long long shifted = static_cast<long long>(temp) << 4; // Left shift by 4 bits
    
    // String manipulation component
    std::string binary_str = "";
    long long copy_shifted = shifted;
    while (copy_shifted > 0) {
        binary_str = (char)((copy_shifted & 1) + '0') + binary_str;
        copy_shifted >>= 1;
    }
    
    // Convert binary string back to integer
    long long reconstructed = 0;
    for (char c : binary_str) {
        reconstructed = (reconstructed << 1) | (c - '0');
    }
    
    // Final calculation
    long long final_result = (reconstructed & 0xFF) * ((intermediate % 7) + 1);
    
    std::cout << "Result: " << final_result << std::endl;
    
    return 0;
}