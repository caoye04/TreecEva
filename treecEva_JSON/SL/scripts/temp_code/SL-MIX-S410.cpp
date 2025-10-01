#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

double computeValue(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(static_cast<double>(x + 1));
}

int main() {
    vector<vector<int>> matrix = {{2, -4, 6}, {3, 5, -7}, {-1, 8, 0}};
    double accumulator = 0.0;
    int i = 0;
    
    while (i < matrix.size()) {
        int j = 0;
        while (j < matrix[i].size()) {
            if ((i + j) % 2 == 0) {
                accumulator += computeValue(matrix[i][j], matrix[j][(i + 1) % 3]);
            } else {
                accumulator -= static_cast<double>(matrix[i][j] & matrix[(i + 1) % 3][j]);
            }
            j++;
        }
        i++;
    }
    
    int xor_result = 0;
    for (const auto& row : matrix) {
        for (int val : row) {
            xor_result ^= val;
        }
    }
    
    bool flag = (xor_result > 0);
    double result = 0.0;
    
    if (flag && accumulator > 10) {
        result = floor(accumulator / static_cast<double>(xor_result));
    } else if (!flag || accumulator <= 10) {
        result = ceil(accumulator * static_cast<double>(xor_result));
    } else {
        result = round(accumulator);
    }
    
    cout << "Result: " << static_cast<long long>(result) << endl;
    return 0;
}