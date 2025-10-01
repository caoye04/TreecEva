#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double complex_calculation(int a, int b) {
    return pow(a, 2) + sqrt(b) - log(static_cast<double>(a + b));
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 4}, {5, 6, 7}, {8, 9, 10}};
    int x = 0, y = 0;
    double accumulator = 0.0;
    string s = "COMPUTATION";
    
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if ((i * j) % 2 == 0) {
                x = matrix[i][j] & (1 << 2);  // Bitwise AND with 4
                y = matrix[j][i] | (1 << 1);  // Bitwise OR with 2
                accumulator += complex_calculation(x, y);
            } else {
                x = matrix[i][j] ^ matrix[j][i];  // Bitwise XOR
                y = (matrix[i][j] << 1) + (matrix[j][i] >> 1);  // Left shift and right shift
                accumulator -= complex_calculation(y, x);
            }
        }
    }
    
    int char_sum = 0;
    for (char c : s) {
        char_sum += static_cast<int>(c) % 10;
    }
    
    double result = accumulator * char_sum;
    result = static_cast<int>(result) % 1000;  // Final step to get a bounded integer result
    
    cout << "Result: " << result << endl;
    return 0;
}