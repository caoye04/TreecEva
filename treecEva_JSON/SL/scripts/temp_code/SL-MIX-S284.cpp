#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

double compute_expression(double x, int y) {
    return pow(x, 2) + sin(y) * cos(y) + log(x + 1);
}

int main() {
    vector<vector<int>> matrix = {{1, 2, 3}, {4, 5, 6}, {7, 8, 9}};
    vector<string> tokens = {"abc", "def", "ghi"};
    
    double accumulator = 0.0;
    int xor_result = 0;
    
    for (size_t i = 0; i < matrix.size(); ++i) {
        for (size_t j = 0; j < matrix[i].size(); ++j) {
            int val = matrix[i][j];
            accumulator += compute_expression(val, static_cast<int>(tokens[i].length()));
            xor_result ^= val;
        }
    }
    
    string concatenated = "";
    for (const auto& token : tokens) {
        reverse(token.begin(), token.end());
        concatenated += token;
    }
    
    int char_sum = 0;
    for (char c : concatenated) {
        char_sum += static_cast<int>(c);
    }
    
    double final_result = (accumulator / xor_result) * sqrt(char_sum);
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}