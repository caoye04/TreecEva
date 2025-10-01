#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define PI 3.14159265359

int complex_operation(int* arr, int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i] ^ (int)pow((double)(i+1), 2.0);
    }
    return sum >> 2;
}

int main() {
    int values[5] = {12, -5, 8, 15, -3};
    int* ptr = values;
    double angles[3] = {PI/4, PI/3, PI/6};
    char text[] = "COMPLEX";
    
    int a = 0x1F & 0x73;
    int b = (~a) | 0x0F;
    int c = (b << 1) ^ 0xAA;
    
    double x = sin(angles[0]) * cos(angles[1]);
    double y = tan(angles[2]) + log(2.71828);
    int d = (int)((x + y) * 100);
    
    for (int i = 0; i < strlen(text); i++) {
        d += (text[i] & 0x1F) ^ (i << 2);
    }
    
    int e = complex_operation(values, 5);
    int f = (d & 0xFF) | (e << 4);
    
    int mask = 0;
    for (int i = 0; i < 8; i++) {
        mask |= (1 << i);
    }
    
    int result = (f ^ mask) & 0x1FF;
    
    // CRITICAL_POINT
    printf("Result: %d\n", result);
    return 0;
}