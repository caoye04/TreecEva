#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int accumulator = 0;
    double product = 1.0;
    string text = "COMPUTATION";
    
    for (int i = 0; i < matrix.size(); i++) {
        for (int j = 0; j < matrix[i].size(); j++) {
            if (matrix[i][j] % 2 == 0) {
                product *= sqrt(matrix[i][j]);
            } else {
                accumulator += matrix[i][j];
            }
        }
    }
    
    int text_sum = 0;
    for (char c : text) {
        text_sum += (c - 'A' + 1);
    }
    
    int bitwise = (accumulator & text_sum) | ((int)product ^ 0xF);
    
    double trig_result = sin(bitwise % 360 * M_PI / 180.0);
    
    int result = (int)(trig_result * 1000) + (bitwise >> 2);
    
    cout << "Result: " << result << endl;
    
    return 0;
}