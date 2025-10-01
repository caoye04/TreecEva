#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize complex nested data structure
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> coefficients = {1, -2, 3, -4, 5};
    
    // Step 1: Apply mathematical transformations to matrix
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (i % 2 == 0) {
                matrix[i][j] = pow(matrix[i][j], 2) + 2 * matrix[i][j];
            } else {
                matrix[i][j] = sqrt(matrix[i][j] * matrix[i][j] + 12);
            }
        }
    }
    
    // Step 2: Calculate weighted sum using coefficients
    int weighted_sum = 0;
    for (int i = 0; i < min(matrix.size(), coefficients.size()-1); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            weighted_sum += matrix[i][j] * coefficients[i];
        }
    }
    
    // Step 3: Bitwise operations
    int bitwise_result = (weighted_sum & 0xFF) | ((weighted_sum >> 4) ^ 0xF0);
    
    // Step 4: Trigonometric adjustment
    double trig_adjustment = sin(bitwise_result % 360 * M_PI / 180.0);
    
    // Step 5: Final calculation combining all transformations
    int final_result = static_cast<int>(round(abs(trig_adjustment) * bitwise_result + 
                         *max_element(coefficients.begin(), coefficients.end()) - 
                         log2(abs(weighted_sum) + 1)));
    
    cout << "Result: " << final_result << endl;
    return 0;
}