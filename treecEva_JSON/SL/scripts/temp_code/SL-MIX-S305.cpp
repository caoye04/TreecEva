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
    string s = "HelloWorld";
    int x = 4, y = 9;
    double z = 1.57;
    
    int sum = 0;
    for(size_t i=0; i<matrix.size(); ++i)
        for(size_t j=0; j<matrix[i].size(); ++j)
            sum += matrix[i][j] & (1 << ((i+j)%4));
    
    bool cond1 = (x > 3) && (y < 10 || s.length() == 10);
    bool cond2 = !(static_cast<double>(y)/x > 2.0);
    
    double expr_val = compute_expression(x, y, z);
    
    int arr[] = {static_cast<int>(expr_val), sum, static_cast<int>(s.length())};
    int* ptr_arr[3];
    for(int i=0; i<3; ++i) ptr_arr[i] = &arr[i];
    
    int idx = (cond1 ^ cond2) ? (*ptr_arr[0])%3 : (*ptr_arr[1])%3;
    int final_result = *(ptr_arr[idx]) + (cond1 && cond2 ? 100 : -50);
    
    cout << "Result: " << final_result << endl;
    return 0;
}