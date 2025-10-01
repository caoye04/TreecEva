#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    // Initialize nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<int> coefficients = {1, -2, 3, -4, 5};
    
    // Step 1: Calculate the determinant-like value of the matrix
    int det = matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]);
    
    // Step 2: Apply a complex mathematical transformation
    double transformed = pow(det, 1.0/3.0) * log(abs(det) + 1);
    
    // Step 3: Process coefficients with bitwise operations
    int coeff_result = 0;
    for(int i = 0; i < coefficients.size(); i++) {
        if(i % 2 == 0) {
            coeff_result ^= coefficients[i] << (i/2);
        } else {
            coeff_result |= coefficients[i] >> ((i-1)/2);
        }
    }
    
    // Step 4: Combine results using trigonometric functions
    double angle = transformed * 0.1;
    double trig_result = sin(angle) * cos(angle) * tan(angle);
    
    // Step 5: Apply logical operations on matrix elements
    int logical_count = 0;
    for(const auto& row : matrix) {
        for(int elem : row) {
            if((elem > 10 && elem % 2 != 0) || (elem <= 10 && elem % 2 == 0)) {
                logical_count++;
            }
        }
    }
    
    // Step 6: Final complex calculation
    int final_result = static_cast<int>(trunc(trig_result * 1000)) + (coeff_result & 0xFF) + (logical_count << 2);
    
    cout << "Result: " << final_result << endl;
    return 0;
}