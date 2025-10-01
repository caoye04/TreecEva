#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c;
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    
    int x = matrix[1][2] << 2;
    int y = (matrix[0][1] & matrix[2][0]) | 6;
    double z = compute_expression(matrix[0][0], matrix[2][1], 1.5);
    
    string s1 = "hello";
    string s2 = "world";
    string combined = s1 + s2;
    int str_length = static_cast<int>(combined.length());
    
    int bitwise_combo = (x ^ str_length) & (y | static_cast<int>(z));
    
    double accumulator = 0.0;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if ((i + j) % 2 == 0) {
                accumulator += matrix[i][j] * 0.5;
            } else {
                accumulator -= matrix[i][j] * 0.25;
            }
        }
    }
    
    int final_result = static_cast<int>(accumulator) + bitwise_combo;
    cout << "Result: " << final_result << endl;
    
    return 0;
}