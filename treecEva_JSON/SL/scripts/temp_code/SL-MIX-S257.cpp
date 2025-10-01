#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * c - sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    
    int x = matrix[1][2];
    int y = s.length();
    double z = M_PI / 4;
    
    double expr_result = compute_expression(x, y, z);
    
    int sum = 0;
    for(int i=0; i<3; i++) {
        for(int j=0; j<3; j++) {
            sum += matrix[i][j] & (1 << ((i+j)%4));
        }
    }
    
    int a = 15, b = 25;
    bool cond = (a < b) && ((a+b) > 30);
    
    int intermediate = cond ? (a | b) : (a ^ b);
    
    double final_result = (expr_result * 1000 + sum * 5 - intermediate) / 100.0;
    
    cout << "Result: " << final_result << endl;
    
    return 0;
}