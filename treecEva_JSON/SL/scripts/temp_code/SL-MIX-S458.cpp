#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double calculate_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    int x = matrix[1][2] >> 1;  // Right shift by 1 (equivalent to divide by 2)
    int y = matrix[0][1] << 2;  // Left shift by 2 (equivalent to multiply by 4)
    
    double z = calculate_expression(x, y, M_PI / 4);
    
    string s = "COMPUTATION";
    int char_sum = 0;
    for(char c : s) {
        char_sum += (c - 'A' + 1);  // Convert letter to number (A=1, B=2, ...)
    }
    
    bool condition1 = (z > 50) && (char_sum % 2 == 0);
    bool condition2 = (x | y) > 30;  // Bitwise OR
    
    int intermediate = 0;
    if(condition1 || condition2) {
        intermediate = static_cast<int>(z) ^ char_sum;  // Bitwise XOR
    } else {
        intermediate = x * y + char_sum;
    }
    
    vector<int> flat;
    for(auto& row : matrix) {
        for(int val : row) {
            flat.push_back(val * (val % 2 == 0 ? 2 : 3));
        }
    }
    
    int accumulator = 0;
    for(size_t i = 0; i < flat.size(); ++i) {
        if(i % 2 == 0) {
            accumulator += flat[i];
        } else {
            accumulator -= flat[i];
        }
    }
    
    int result = (intermediate & accumulator) + (intermediate | accumulator);  // Bitwise AND and OR
    
    cout << "Result: " << result << endl;
    return 0;
}