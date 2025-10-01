#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

int main() {
    // Initialize complex nested data structure
    std::vector<std::vector<int>> matrix = {{15, -7, 32}, {8, -21, 14}, {45, 6, -13}};
    
    // Step 1: Apply mathematical transformations to each element
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] > 0) {
                matrix[i][j] = static_cast<int>(std::pow(matrix[i][j], 1.5));
            } else {
                matrix[i][j] = static_cast<int>(std::abs(matrix[i][j]) * 3);
            }
        }
    }
    
    // Step 2: Calculate row products and store in vector
    std::vector<long long> row_products(matrix.size(), 1);
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            row_products[i] *= matrix[i][j];
        }
    }
    
    // Step 3: Perform bitwise operations on row products
    long long xor_accum = 0;
    for (int i = 0; i < row_products.size(); i++) {
        xor_accum ^= row_products[i];
    }
    
    // Step 4: Apply trigonometric transformation
    double trig_result = std::sin(xor_accum % 100) * 1000;
    
    // Step 5: Complex logical evaluation with nested conditions
    int logical_counter = 0;
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if ((matrix[i][j] % 2 == 0 && matrix[i][j] > 50) || 
                (matrix[i][j] % 3 == 0 && std::abs(matrix[i][j]) < 1000)) {
                logical_counter++;
            }
        }
    }
    
    // Step 6: Final calculation combining all previous results
    long long final_result = static_cast<long long>(trig_result) * logical_counter + 
                            (xor_accum % 1000000);
    
    // Adjust for negative values
    if (final_result < 0) {
        final_result = std::abs(final_result) + 0xFFFF;
    }
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}