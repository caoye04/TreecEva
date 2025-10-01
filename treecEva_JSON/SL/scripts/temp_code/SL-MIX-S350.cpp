#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <map>

double complex_operation(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) - log(x + y + 1);
}

int main() {
    std::vector<std::vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    std::map<int, double> lookup_table;
    
    // Populate lookup table with complex operations
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            int key = matrix[i][j];
            lookup_table[key] = complex_operation(i+1, j+1);
        }
    }
    
    // Perform bit-wise manipulations
    int a = matrix[0][0] << 1;  // 2 << 1 = 4
    int b = matrix[0][1] >> 1;  // 3 >> 1 = 1
    int c = a & b;              // 4 & 1 = 0
    int d = a | b;              // 4 | 1 = 5
    int e = c ^ d;              // 0 ^ 5 = 5
    
    // Use lookup table values
    double val1 = lookup_table[matrix[1][1]];  // lookup_table[11]
    double val2 = lookup_table[matrix[2][0]];  // lookup_table[17]
    
    // Perform trigonometric operations
    double trig_result = sin(val1) + cos(val2) + tan(e);
    
    // Conditional logic with short-circuit evaluation
    int condition_a = (a > b) && (c < d);
    int condition_b = (val1 > 0) || (val2 < 0);
    
    // Complex calculation chain
    double intermediate = (trig_result * condition_a) + (val1 / (val2 + 1.0)) - (e * condition_b);
    
    // Final calculation
    double final_result = round(intermediate * 1000.0) / 1000.0;  // Round to 3 decimal places
    
    std::cout << "Result: " << final_result << std::endl;
    return 0;
}