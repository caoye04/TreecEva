#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - (a & b);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    int x = 12;
    int y = 15;
    double z = 2.5;
    
    // Step 1: Perform bitwise AND between x and y
    int step1 = x & y;
    
    // Step 2: Left shift step1 by 2 positions
    int step2 = step1 << 2;
    
    // Step 3: Calculate XOR between step2 and the first element of the last row in matrix
    int step3 = step2 ^ matrix[2][0];
    
    // Step 4: Reverse the string s
    reverse(s.begin(), s.end());
    
    // Step 5: Get length of reversed string and multiply with step3
    int step5 = static_cast<int>(s.length()) * step3;
    
    // Step 6: Compute expression using second row elements of matrix
    double expr_result = compute_expression(matrix[1][0], matrix[1][1], z);
    
    // Step 7: Add step5 to expr_result and divide by 2
    double intermediate = (step5 + expr_result) / 2.0;
    
    // Step 8: Apply floor function to intermediate result
    int result = static_cast<int>(floor(intermediate));
    
    cout << "Result: " << result << endl;
    return 0;
}