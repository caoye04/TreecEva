#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c;
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    int x = 10, y = 20;
    
    // Step 1: Perform bitwise operations
    int bitwise_result = (x << 2) & (y >> 1);
    
    // Step 2: Manipulate string
    reverse(s.begin(), s.end());
    int str_length = static_cast<int>(s.length());
    
    // Step 3: Nested loop with conditionals
    int sum = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            if ((matrix[i][j] % 2 == 0 && i < j) || (matrix[i][j] > 10 && j >= i)) {
                sum += matrix[i][j];
            }
        }
    }
    
    // Step 4: Mathematical computation
    double expr_result = compute_expression(bitwise_result, str_length, 1.5);
    
    // Step 5: Final calculation
    int final_sum = sum + static_cast<int>(expr_result);
    
    // Step 6: Bitwise XOR with a calculated value
    int xor_val = (final_sum ^ 0xFF) & 0x7F;
    
    // Step 7: Conditional assignment based on complex logic
    int conditional_result;
    if ((xor_val > 50 || str_length < 10) && (bitwise_result != 0)) {
        conditional_result = xor_val * 2;
    } else {
        conditional_result = xor_val / 2;
    }
    
    // Final result computation
    int result = conditional_result + static_cast<int>(compute_expression(conditional_result, 16, 2.0)) % 100;
    
    cout << "Result: " << result << endl;
    return 0;
}