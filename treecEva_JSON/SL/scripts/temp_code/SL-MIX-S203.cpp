#define M_PI 3.14159265358979323846
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
    string text = "COMPUTER_SCIENCE";
    int a = 12, b = 8;
    
    // Step 1: Perform bitwise operations
    int xor_val = a ^ b;
    int and_val = a & b;
    int shifted = (xor_val << 1) | (and_val >> 1);
    
    // Step 2: Manipulate string
    reverse(text.begin(), text.end());
    int str_len = static_cast<int>(text.length());
    char first_char = text[0];
    int ascii_diff = static_cast<int>(first_char) - static_cast<int>('A');
    
    // Step 3: Nested loop with conditional logic
    int sum = 0;
    for (int i = 0; i < matrix.size(); ++i) {
        for (int j = 0; j < matrix[i].size(); ++j) {
            if ((matrix[i][j] % 2 == 0 && i < j) || (matrix[i][j] % 3 == 0 && j >= i)) {
                sum += matrix[i][j];
            }
        }
    }
    
    // Step 4: Mathematical computation
    double expr_result = compute_expression(shifted, ascii_diff);
    
    // Step 5: Final calculation using all derived values
    double result = round((sum * expr_result + str_len) / M_PI);
    
    cout << "Result: " << static_cast<long long>(result) << endl;
    return 0;
}