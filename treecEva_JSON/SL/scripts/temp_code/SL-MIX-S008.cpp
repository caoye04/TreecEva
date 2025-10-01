#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <bitset>

using namespace std;

double computeExpression(double x, int y) {
    return pow(x, 2) + sin(y) * cos(y) + log(x + 1);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int a = 10, b = 20;
    double c = 3.5;
    
    // Perform bitwise operations
    int bitwise_result = (a & b) | (a ^ b);
    
    // Nested loop to manipulate matrix values
    for(int i = 0; i < matrix.size(); i++) {
        for(int j = 0; j < matrix[i].size(); j++) {
            matrix[i][j] = matrix[i][j] * 2 + (i ^ j);
        }
    }
    
    // Calculate sum of all elements in the modified matrix
    int matrix_sum = 0;
    for(const auto& row : matrix) {
        for(int val : row) {
            matrix_sum += val;
        }
    }
    
    // Perform mathematical computation
    double expr_result = computeExpression(c, matrix_sum % 100);
    
    // Bit shifting and masking
    int shifted = (bitwise_result << 2) & 0xFF;
    
    // Final calculation combining all results
    int result = static_cast<int>(expr_result) + shifted + (matrix_sum >> 3);
    
    cout << "Result: " << result << endl;
    return 0;
}