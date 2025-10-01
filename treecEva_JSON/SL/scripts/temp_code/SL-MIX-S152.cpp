#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double computeExpression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - static_cast<double>(a & b);
}

int main() {
    vector<vector<int>> matrix = {{4, 9, 2}, {3, 5, 7}, {8, 1, 6}};
    
    int x = matrix[1][2] << 1;
    int y = matrix[0][0] | matrix[2][2];
    double z = static_cast<double>(matrix[1][1]) / 2.5;
    
    bool condition1 = (x > 10) && (y < 15);
    bool condition2 = !((matrix[0][1] ^ matrix[2][1]) > 5);
    
    double intermediate = 0.0;
    if (condition1 || condition2) {
        intermediate = computeExpression(matrix[0][2], matrix[2][0], z);
    } else {
        intermediate = computeExpression(y, x, static_cast<double>(matrix[1][0]));
    }
    
    string s1 = "hello";
    string s2 = "world";
    string s3 = s1 + s2;
    int len = s3.length();
    
    int indices[] = {len % 5, len / 4, abs(len - 12)};
    int sum_indices = 0;
    for (int i = 0; i < 3; i++) {
        sum_indices += indices[i] * matrix[i][i];
    }
    
    double result = intermediate + log(static_cast<double>(sum_indices)) - (condition1 ? M_PI : M_E);
    
    cout << "Result: " << result << endl;
    return 0;
}