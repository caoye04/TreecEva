#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int base = 2;
    int exp = 4;
    double log_val = log2(1024);
    int xor_result = 0;
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] % 2 == 0) {
                matrix[i][j] = pow(matrix[i][j], 2);
            } else {
                matrix[i][j] = sqrt(matrix[i][j] * matrix[i][j]);
            }
        }
    }
    
    int power_result = pow(base, exp);
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            xor_result ^= matrix[i][j];
        }
    }
    
    int intermediate = static_cast<int>(log_val) * power_result;
    int final_result = (xor_result & 0xFF) | (intermediate << 2);
    
    cout << "Result: " << final_result << endl;
    return 0;
}