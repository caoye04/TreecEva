#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<int>> matrix = {{12, -5, 8}, {3, 17, -2}, {9, 0, 15}};
    vector<int> coefficients = {2, -1, 3};
    
    // Step 1: Apply coefficient transformations
    for(int i = 0; i < matrix.size(); i++) {
        for(int j = 0; j < matrix[i].size(); j++) {
            matrix[i][j] = matrix[i][j] * coefficients[j % coefficients.size()];
        }
    }
    
    // Step 2: Calculate row sums and store in new vector
    vector<int> row_sums(matrix.size(), 0);
    for(int i = 0; i < matrix.size(); i++) {
        for(int j = 0; j < matrix[i].size(); j++) {
            row_sums[i] += matrix[i][j];
        }
    }
    
    // Step 3: Apply mathematical transformations
    double accumulator = 0.0;
    for(int i = 0; i < row_sums.size(); i++) {
        if(row_sums[i] > 0) {
            accumulator += sqrt(abs(row_sums[i]));
        } else {
            accumulator -= pow(abs(row_sums[i]), 1.5);
        }
    }
    
    // Step 4: Bitwise operations on coefficients
    int bitwise_result = coefficients[0];
    for(int i = 1; i < coefficients.size(); i++) {
        bitwise_result = bitwise_result ^ (coefficients[i] << i);
    }
    
    // Step 5: Complex logical evaluation
    bool condition_a = (accumulator > 10.0) && (bitwise_result < 0);
    bool condition_b = (row_sums[1] > row_sums[0]) || (coefficients[2] != 3);
    
    // Step 6: Final calculation combining all components
    int final_result;
    if(condition_a xor condition_b) {
        final_result = static_cast<int>(floor(accumulator)) + bitwise_result;
    } else if(condition_a && condition_b) {
        final_result = static_cast<int>(ceil(accumulator)) * coefficients[1];
    } else {
        final_result = static_cast<int>(accumulator) - (bitwise_result >> 1);
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}