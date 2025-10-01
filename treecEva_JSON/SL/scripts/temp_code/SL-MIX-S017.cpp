#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

int main() {
    // Initialize data structures
    std::vector<int> nums = {3, 7, 2, 9, 1, 8, 4, 6, 5};
    std::vector<std::vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    std::string text = "ComplexReasoningTask";
    
    // Step 1: Perform mathematical operations
    double x = 2.5;
    double y = std::pow(x, 3) + std::sqrt(16) - std::log(2.71828);
    int z = static_cast<int>(y) & 15; // Bitwise AND with 15 (0b1111)
    
    // Step 2: Manipulate the vector
    std::sort(nums.begin(), nums.end());
    int sum = 0;
    for(int i = 0; i < nums.size(); i++) {
        if(i % 2 == 0) {
            sum += nums[i];
        }
    }
    
    // Step 3: Work with the matrix
    int diag_product = 1;
    for(size_t i = 0; i < matrix.size(); i++) {
        diag_product *= matrix[i][i];
    }
    
    // Step 4: String manipulation
    int vowel_count = 0;
    std::string vowels = "aeiouAEIOU";
    for(char c : text) {
        if(vowels.find(c) != std::string::npos) {
            vowel_count++;
        }
    }
    
    // Step 5: Complex calculation combining all previous results
    int intermediate = (sum ^ diag_product) | (vowel_count << 2); // XOR, then OR with vowel_count shifted left by 2
    double temp = std::sin(M_PI/6) * 100; // sine of 30 degrees
    int sine_val = static_cast<int>(std::round(temp));
    
    // Final calculation
    int result = ((intermediate + z) * sine_val) % 1000;
    
    std::cout << "Result: " << result << std::endl;
    return 0;
}