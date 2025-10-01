#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

double compute_inner_value(const std::vector<int>& nums) {
    double sum = 0;
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
    
    std::string flag = "complex_mix";
    bool cond1 = (inner > 0);
    bool cond2 = (flag.length() > 5);
    bool combined = cond1 && cond2;
    
    int base = 12;
    int shift = 3;
    int shifted = base << shift;
    
    double trig_result = std::sin(M_PI / 6) * 100; // sin(30 degrees) * 100
    
    double mixed;
    if (combined) {
        mixed = inner + shifted + trig_result;
    } else {
        mixed = inner - shifted - trig_result;
    }
    
    int xor_result = 0xF0 ^ 0x0F;
    
    double final_result = mixed / xor_result;
    
    std::cout << "Result: " << final_result << std::endl;
    
    return 0;
}