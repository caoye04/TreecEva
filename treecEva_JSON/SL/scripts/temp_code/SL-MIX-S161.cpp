#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(static_cast<double>(x + 1));
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    int a = 10, b = 20;
    double temp_result = 0.0;
    
    // Step 1: Perform bitwise operations
    int xor_val = matrix[0][1] ^ matrix[1][2];
    int and_val = matrix[2][0] & matrix[0][0];
    int shifted = (xor_val << 1) | and_val;
    
    // Step 2: Manipulate string
    reverse(s.begin(), s.end());
    int str_len = static_cast<int>(s.length());
    
    // Step 3: Nested loop with conditionals
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            if ((matrix[i][j] & 1) == 1) {  // Check if odd
                temp_result += compute_expression(matrix[i][j], str_len);
            }
        }
    }
    
    // Step 4: Combine results
    double intermediate = temp_result / (shifted + str_len);
    int final_shift = static_cast<int>(intermediate) >> 1;
    
    // Final computation
    int result = (final_shift * a) + (b / static_cast<int>(log(intermediate + 1)));
    
    cout << "Result: " << result << endl;
    return 0;
}