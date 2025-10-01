#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    vector<double> powers;
    int sum = 0;
    
    // Step 1: Calculate sum of all elements in matrix
    for (const auto& row : matrix) {
        for (int val : row) {
            sum += val;
        }
    }
    
    // Step 2: Generate powers vector
    for (int i = 1; i <= 5; i++) {
        powers.push_back(pow(sum * 0.1, i));
    }
    
    // Step 3: Perform bitwise operations
    int bitwise_result = 0;
    for (size_t i = 0; i < powers.size(); i++) {
        int truncated = (int)powers[i];
        if (i % 2 == 0) {
            bitwise_result |= truncated;
        } else {
            bitwise_result &= truncated;
        }
    }
    
    // Step 4: Apply trigonometric transformations
    double trig_sum = 0;
    for (double val : powers) {
        trig_sum += sin(val) * cos(val);
    }
    
    // Step 5: Complex calculation involving both bitwise and trigonometric results
    int final_result = (int)(bitwise_result * trig_sum * 1000);
    
    // Apply modulo to ensure result is in expected range
    final_result = abs(final_result) % 10000;
    
    cout << "Result: " << final_result << endl;
    return 0;
}