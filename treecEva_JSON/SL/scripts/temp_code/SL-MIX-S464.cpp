#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int x = matrix[1][2];
    int y = matrix[0][1] + matrix[2][0];
    double z = M_PI / 4;
    
    double expr_result = compute_expression(x, y, z);
    
    string s1 = "hello";
    string s2 = "world";
    string s3 = s1 + s2;
    int str_len = s3.length();
    
    int bit_op_result = (x & y) | (str_len ^ 6);
    
    bool cond1 = (expr_result > 100.0);
    bool cond2 = (bit_op_result <= 20);
    bool final_cond = cond1 && cond2;
    
    int final_result = 0;
    if(final_cond) {
        final_result = static_cast<int>(expr_result) % 10;
    } else {
        final_result = (bit_op_result << 1) + static_cast<int>(floor(expr_result));
    }
    
    cout << "Result: " << final_result << endl;
    return 0;
}