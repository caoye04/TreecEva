#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(double x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(x + 1);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string text = "AdvancedProgramming";
    double accumulator = 0.0;
    int toggle = 1;
    int index = 0;
    
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            int val = matrix[i][j];
            if (toggle) {
                accumulator += compute_expression(val, static_cast<int>(text[index % text.length()]));
            } else {
                accumulator -= compute_expression(static_cast<double>(text[index % text.length()]), val);
            }
            toggle ^= 1;
            index++;
        }
    }
    
    // Perform bitwise operations on the integer part of accumulator
    int acc_int = static_cast<int>(accumulator);
    int shifted = (acc_int << 2) ^ 0xF0F0;
    
    // Final adjustment using trigonometric functions
    double final_result = sin(shifted) * cos(accumulator - acc_int) + tan(shifted % 100);
    
    cout << "Result: " << final_result << endl;
    return 0;
}