#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <bitset>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - (a & b);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    int x = 15, y = 9;
    double z = 2.5;
    
    // Step 1: Perform bitwise AND between x and y
    int bitwise_result = x & y;
    
    // Step 2: Extract substring from index 5 with length 5
    string sub_str = s.substr(5, 5);
    
    // Step 3: Convert last character of substring to its ASCII value
    int ascii_val = static_cast<int>(sub_str.back());
    
    // Step 4: Compute expression using first row of matrix
    vector<int> first_row = matrix[0];
    double expr_result = compute_expression(first_row[0], first_row[1], z);
    
    // Step 5: Sum all elements in second column of matrix
    int col_sum = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        col_sum += matrix[i][1];
    }
    
    // Step 6: Calculate final result using previous computations
    double result = (bitwise_result * ascii_val) + expr_result - col_sum;
    
    cout << "Result: " << result << endl;
    return 0;
}