#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <bitset>

using namespace std;

double compute_expression(int x, int y) {
    return pow(x, 2) + sqrt(abs(y)) + log(static_cast<double>(x + 1));
}

int main() {
    vector<vector<int>> matrix = {{2, 3, 5}, {7, 11, 13}, {17, 19, 23}};
    string s = "HelloWorld";
    
    int a = matrix[1][2]; // 13
    int b = static_cast<int>(s.length()); // 10
    
    double c = compute_expression(a, b); // pow(13,2) + sqrt(10) + log(14)
    
    unsigned int d = static_cast<unsigned int>(c);
    unsigned int e = d << 2;
    unsigned int f = (d & 0xFF) | ((d >> 8) & 0xFF);
    
    bitset<32> bs1(d);
    bitset<32> bs2(e);
    bitset<32> bs3(f);
    
    int count1 = bs1.count();
    int count2 = bs2.count();
    int count3 = bs3.count();
    
    int combined_count = (count1 ^ count2) + (count1 & count3);
    
    int result = static_cast<int>(combined_count * sin(M_PI / 6)); // sin(30 degrees) = 0.5
    
    cout << "Result: " << result << endl;
    return 0;
}