#define M_PI 3.14159265358979323846
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
    
    // Step 2: Calculate powers and store in vector
    for (int i = 1; i <= 5; i++) {
        double power = pow(static_cast<double>(sum % 10), i);
        powers.push_back(power);
    }
    
    // Step 3: Perform bitwise operations
    int bitwise_result = 0;
    for (size_t i = 0; i < powers.size(); i++) {
        int val = static_cast<int>(powers[i]);
        if (i % 2 == 0) {
            bitwise_result |= val;
        } else {
            bitwise_result &= val;
        }
    }
    
    // Step 4: Complex mathematical expression
    double expr1 = sin(bitwise_result * M_PI / 180.0);
    double expr2 = cos(bitwise_result * M_PI / 180.0);
    double intermediate = pow(expr1, 2) + pow(expr2, 2);
    
    // Step 5: Final calculation using all previous results
    int final_result = static_cast<int>(intermediate * sum) + (bitwise_result ^ (sum & 0xF));
    
    cout << "Result: " << final_result << endl;
    return 0;
}