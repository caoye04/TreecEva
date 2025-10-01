#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<double> results;
    
    // Step 1: Process each row with complex mathematical operations
    for (int i = 0; i < matrix.size(); i++) {
        double row_sum = 0;
        for (int j = 0; j < matrix[i].size(); j++) {
            row_sum += pow(matrix[i][j], 1.5) * log(matrix[i][j] + 1);
        }
        results.push_back(row_sum / 3.0);
    }
    
    // Step 2: Apply trigonometric transformations
    double trig_sum = 0;
    for (int i = 0; i < results.size(); i++) {
        trig_sum += sin(results[i]) * cos(results[i] / 2.0);
    }
    
    // Step 3: Bitwise operations on integer parts
    int int_part = (int)(trig_sum * 1000);
    int xor_result = 0;
    for (int i = 0; i < 8; i++) {
        xor_result ^= ((int_part >> i) & 1);
    }
    
    // Step 4: Final complex calculation
    double final_result = sqrt(abs(trig_sum)) * pow(2.71828, xor_result % 3) + atan2(1, 1) * 4;
    
    // Adjust based on parity
    if ((int)final_result % 2 == 0) {
        final_result = final_result / 2.0 + 10.0;
    } else {
        final_result = final_result * 1.5 - 5.0;
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}