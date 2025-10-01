#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double complex_calc(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    // Initialize complex nested data structures
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<double> coefficients = {1.5, 2.7, 3.14159};
    
    // Multi-step arithmetic and logical operations
    int x = matrix[1][2] << 1;  // Bitwise left shift
    int y = (x & 0xF0) | 0x0A;  // Bitwise AND/OR operations
    
    // Conditional logic with short-circuit evaluation
    bool condition = (y > 100) && (matrix[0][0] * matrix[2][2] < 500);
    
    double accumulator = 0.0;
    if (condition) {
        for (int i = 0; i < 3; i++) {
            accumulator += complex_calc(matrix[i][0], matrix[i][1], coefficients[i]);
        }
    } else {
        // Nested loop with complex calculations
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                double temp = pow(matrix[i][j], 1.5) * cos(coefficients[j]);
                if (temp > 50) {
                    accumulator += temp / 2;
                } else {
                    accumulator += temp * 2;
                }
            }
        }
    }
    
    // String manipulation and conversion
    string num_str = to_string(static_cast<long long>(accumulator));
    int str_length = num_str.length();
    
    // Final calculation combining all previous results
    int result = (y ^ str_length) + static_cast<int>(accumulator) % 100;
    
    // Execution Point Y
    cout << "Result: " << result << endl;
    
    return 0;
}