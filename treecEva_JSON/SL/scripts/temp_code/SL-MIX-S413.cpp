#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double computeValue(int n) {
    vector<vector<double>> matrix(n, vector<double>(n, 0.0));
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            matrix[i][j] = pow(sin(M_PI * i / n), 2) + pow(cos(M_PI * j / n), 2);
        }
    }
    
    double sum = 0.0;
    for (const auto& row : matrix) {
        for (double val : row) {
            sum += val;
        }
    }
    
    return sum / (n * n);
}

int main() {
    string s = "COMPLEX_LOGIC_TEST";
    int a = s.length();
    int b = 0;
    
    for (char c : s) {
        b += (c & 0xF) ^ (c >> 4);
    }
    
    int x = (a << 2) | (b & 0x7);
    int y = (x & 0xF0) >> 4;
    
    double d = computeValue(y);
    
    int result = static_cast<int>(round(d * 1000));
    
    cout << "Result: " << result << endl;
    
    return 0;
}