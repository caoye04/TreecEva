#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>

using namespace std;

double compute_expression(int a, int b, double c) {
    return pow(a, 2) + sqrt(b) * sin(c);
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    int x = matrix[1][2];
    int y = matrix[0][1] + matrix[2][0];
    
    double angle = 1.5708; // approximately pi/2
    double intermediate = compute_expression(x, y, angle);
    
    string s = "HelloWorld";
    int len = s.length();
    int z = len ^ (int(intermediate) & 0xFF);
    
    vector<int> arr = {z, x, y};
    sort(arr.begin(), arr.end());
    
    int product = 1;
    for (int i = 0; i < arr.size(); i++) {
        product *= arr[i];
        if (i == 1) {
            product -= arr[0];
        }
    }
    
    int final_result = (product >> 2) + (z & 0x0F);
    
    cout << "Result: " << final_result << endl;
    return 0;
}