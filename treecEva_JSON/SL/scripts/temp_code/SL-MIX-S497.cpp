#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    // Initialize a 3D vector with specific values
    std::vector<std::vector<std::vector<int>>> data = {
        {{1, 2, 3}, {4, 5, 6}},
        {{7, 8, 9}, {10, 11, 12}},
        {{13, 14, 15}, {16, 17, 18}}
    };
    
    // Step 1: Calculate sum of all elements in the 3D vector
    int sum = 0;
    for (const auto& layer : data) {
        for (const auto& row : layer) {
            for (const auto& elem : row) {
                sum += elem;
            }
        }
    }
    
    // Step 2: Apply a complex mathematical transformation
    double transformed = pow(sum, 1.5) + log(sum) * sin(sum % 100);
    
    // Step 3: Bitwise operations
    int bitwise_result = (static_cast<int>(transformed) & 0xFF) | ((sum >> 2) ^ 0xAA);
    
    // Step 4: Conditional logic with multiple branches
    int conditional_value;
    if (bitwise_result > 1000) {
        conditional_value = bitwise_result / 3;
    } else if (bitwise_result > 500) {
        conditional_value = bitwise_result * 2;
    } else {
        conditional_value = bitwise_result + 500;
    }
    
    // Step 5: String manipulation and conversion
    std::string num_str = std::to_string(conditional_value);
    std::reverse(num_str.begin(), num_str.end());
    int reversed_num = std::stoi(num_str);
    
    // Step 6: Final calculation combining all previous results
    int final_result = (reversed_num % 997) + (sum & 0xF) + (bitwise_result >> 3);
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}