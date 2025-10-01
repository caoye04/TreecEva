#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <map>

double computeNestedValue(const std::vector<std::vector<int>>& matrix, int level) {
    if (level <= 0) return 1.0;
    
    double sum = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            sum += std::pow(val, level);
        }
    }
    
    return sum + computeNestedValue(matrix, level - 1);
}

int main() {
    // Initialize complex nested data structure
    std::vector<std::vector<int>> data = {{2, 3, -1}, {0, 4, -2}, {5, -3, 1}};
    
    // Perform mathematical transformations
    std::map<int, double> transformations;
    for (int i = 0; i < 3; i++) {
        double base = 0;
        for (int j = 0; j < 3; j++) {
            base += std::sin(data[i][j] * M_PI / 6);
        }
        transformations[i] = std::round(base * 1000) / 1000;
    }
    
    // Apply bitwise operations on transformed values
    long long accumulator = 0x0F0F;
    for (const auto& pair : transformations) {
        int key = pair.first;
        int value = static_cast<int>(pair.second * 1000);
        
        if (key & 1) {
            accumulator ^= value;
        } else {
            accumulator |= (value << 2);
        }
    }
    
    // Complex calculation combining all elements
    double intermediate = computeNestedValue(data, 3);
    long long mask = (accumulator & 0xFF) | ((accumulator >> 8) & 0xFF);
    
    // Execution Point Y
    double result = std::floor(intermediate) + std::log(mask + 1) * 10;
    
    std::cout << "Result: " << static_cast<long long>(result) << std::endl;
    return 0;
}