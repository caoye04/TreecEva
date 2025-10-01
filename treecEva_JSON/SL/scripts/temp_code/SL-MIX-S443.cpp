#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    // Initialize complex nested data structure
    std::vector<std::vector<int>> matrix = {{15, -7, 32}, {-24, 45, -18}, {9, -33, 56}};
    
    // Step 1: Apply mathematical transformation to each element
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] > 0) {
                matrix[i][j] = static_cast<int>(std::pow(matrix[i][j], 1.5));
            } else {
                matrix[i][j] = static_cast<int>(std::abs(matrix[i][j]) * 2.5);
            }
        }
    }
    
    // Step 2: Calculate row products and store in array
    int row_products[3];
    for (int i = 0; i < 3; i++) {
        row_products[i] = 1;
        for (int j = 0; j < 3; j++) {
            row_products[i] *= matrix[i][j];
        }
    }
    
    // Step 3: Apply bitwise operations based on conditions
    int bitwise_result = 0;
    for (int i = 0; i < 3; i++) {
        if (row_products[i] % 2 == 0) {
            bitwise_result |= row_products[i];
        } else {
            bitwise_result ^= (row_products[i] >> 2);
        }
    }
    
    // Step 4: Perform complex mathematical calculation
    double temp_calc = std::log(static_cast<double>(bitwise_result)) * std::sin(1.25);
    
    // Step 5: Apply final transformation using nested conditions
    int final_result;
    if (temp_calc > 0) {
        final_result = static_cast<int>(temp_calc) % 1000;
    } else {
        final_result = static_cast<int>(std::abs(temp_calc)) * 3;
    }
    
    // Additional complexity: Modify based on prime check
    bool is_prime = true;
    if (final_result <= 1) {
        is_prime = false;
    } else {
        for (int i = 2; i <= std::sqrt(final_result); i++) {
            if (final_result % i == 0) {
                is_prime = false;
                break;
            }
        }
    }
    
    if (is_prime) {
        final_result += 100;
    } else {
        final_result -= 50;
    }
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}