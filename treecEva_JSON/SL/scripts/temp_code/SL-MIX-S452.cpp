#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) - log(x + y + 1);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string text = "ComplexLogicalEvaluation";
    
    double accumulator = 0.0;
    int counter = 0;
    
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            if ((matrix[i][j] & 1) == 1) { // Check if odd
                accumulator += compute_expression(matrix[i][j], static_cast<int>(text[counter % text.length()]));
                counter++;
            }
        }
    }
    
    int xor_result = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            xor_result ^= val;
        }
    }
    
    bool condition = (xor_result > 10) && (accumulator < 500);
    
    double final_result = 0;
    if (condition) {
        final_result = floor(accumulator / counter) * xor_result;
    } else {
        string reversed_text = text;
        reverse(reversed_text.begin(), reversed_text.end());
        final_result = ceil(accumulator) + reversed_text.length();
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}