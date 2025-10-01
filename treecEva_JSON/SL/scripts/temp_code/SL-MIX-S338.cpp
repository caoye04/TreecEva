#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int sum = 0;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sum += matrix[i][j] * pow(-1, i + j);
        }
    }
    
    string s = "HELLO";
    int charSum = 0;
    for (char c : s) {
        charSum += (c - 'A' + 1);
    }
    
    int x = 10, y = 3;
    int expr = (x & y) * (x | y) + (x ^ y);
    
    double angle = M_PI / 4;
    double trigResult = sin(angle) * cos(angle) * 100;
    int trigInt = static_cast<int>(round(trigResult));
    
    int result = sum + charSum + expr + trigInt;
    cout << "Result: " << result << endl;
    return 0;
}