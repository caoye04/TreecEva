#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <map>

double complex_calculation(int base, int exp, double offset) {
    double result = 1.0;
    for(int i = 0; i < exp; i++) {
        result *= base;
    }
    return result + offset;
}

int main() {
    // Initialize data structures
    std::vector<int> numbers = {2, 3, 5, 7, 11};
    std::map<std::string, double> constants;
    constants["pi"] = 3.14159;
    constants["e"] = 2.71828;
    
    // Perform nested calculations
    int a = numbers[0] * numbers[2];  // 2 * 5 = 10
    int b = static_cast<int>(constants["pi"] * 10);  // 31
    double c = complex_calculation(2, 3, constants["e"]);  // 2^3 + 2.71828 = 10.71828
    
    // Bitwise operations
    int d = (a & b) | static_cast<int>(c);  // (10 & 31) | 10 = 10 | 10 = 10
    int e = d << 2;  // 10 << 2 = 40
    
    // Trigonometric and logarithmic operations
    double f = sin(constants["pi"]/2) * 100;  // sin(π/2) * 100 = 100
    double g = log(constants["e"]) * 50;  // ln(e) * 50 = 50
    
    // Complex data structure manipulation
    std::vector<std::vector<int>> matrix(3, std::vector<int>(3, 0));
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            matrix[i][j] = (i+1) * (j+1) * e;
        }
    }
    
    // Calculate sum of diagonal elements
    int diagonal_sum = 0;
    for(int i = 0; i < 3; i++) {
        diagonal_sum += matrix[i][i];
    }
    
    // Final calculation combining all results
    double final_result = (diagonal_sum + f + g) / (e - (b >> 1)) + pow(c, 1.5);
    
    // Execution point Y
    std::cout << "Result: " << final_result << std::endl;
    
    return 0;
}