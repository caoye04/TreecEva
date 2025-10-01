#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

double compute_inner_value(const std::vector<int>& nums) {
    double sum = 0.0;
    for (size_t i = 0; i < nums.size(); ++i) {
        if (i % 2 == 0) {
            sum += std::pow(nums[i], 2);
        } else {
            sum -= std::sqrt(std::abs(nums[i]));
        }
    }
    return sum;
}

int main() {
    std::vector<int> data = {9, 16, 25, 36, 49};
    
    double inner = compute_inner_value(data);
    int a = static_cast<int>(std::floor(inner));
    int b = 12;
    int c = 7;
    
    // Perform bitwise operations
    int step1 = (a & b) | c;
    int step2 = (step1 << 2) ^ 0xF;
    
    // String manipulation for index calculation
    std::string key = "complex";
    int key_len = static_cast<int>(key.length());
    int index = (step2 % key_len) + 1;
    
    // Nested conditional logic
    int selector = 0;
    if (index > 3) {
        if ((step2 & 0x1) == 1) {
            selector = 1;
        } else {
            selector = 2;
        }
    } else {
        selector = 3;
    }
    
    // Multi-step arithmetic
    double base = std::log(inner + 100);
    double exp = std::sin(selector) * std::cos(selector);
    double power_result = std::pow(base, exp);
    
    // Final calculation sequence
    long long final_result = static_cast<long long>(power_result);
    final_result = (final_result * 17) % 1000;
    final_result += (step2 ^ key_len);
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}