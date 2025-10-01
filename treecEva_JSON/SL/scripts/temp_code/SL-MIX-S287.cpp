#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<int>> matrix = {{12, -5, 8}, {3, 17, -2}, {9, 0, 14}};
    
    // Perform transformations on matrix
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] < 0) {
                matrix[i][j] = abs(matrix[i][j]) * 2;
            } else if (matrix[i][j] % 2 == 0) {
                matrix[i][j] = sqrt(matrix[i][j]) * sqrt(matrix[i][j]); // Keep even numbers unchanged
            } else {
                matrix[i][j] = pow(matrix[i][j], 2);
            }
        }
    }
    
    // Calculate row products
    vector<long long> row_products(3, 1);
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            row_products[i] *= matrix[i][j];
        }
    }
    
    // Apply mathematical transformations
    double transformed_value = pow(row_products[0], 1.0/3.0); // Cube root
    long long intermediate = static_cast<long long>(transformed_value);
    
    // Bitwise operations
    int bitwise_result = (intermediate & 0xFF) | ((intermediate >> 8) ^ 0xF0);
    
    // Final calculation combining all results
    long long final_result = (row_products[1] / row_products[2]) + bitwise_result - static_cast<long long>(sin(0) * 1000);
    
    cout << "Result: " << final_result << endl;
    return 0;
}