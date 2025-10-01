#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
    int area;
};

int main() {
    struct Rectangle rects[2];
    
    rects[0].topLeft.x = 3;
    rects[0].topLeft.y = 7;
    rects[0].bottomRight.x = 11;
    rects[0].bottomRight.y = 2;
    
    rects[1].topLeft.x = 5;
    rects[1].topLeft.y = 9;
    rects[1].bottomRight.x = 13;
    rects[1].bottomRight.y = 4;
    
    // Calculate areas
    for(int i = 0; i < 2; i++) {
        int width = rects[i].bottomRight.x - rects[i].topLeft.x;
        int height = rects[i].topLeft.y - rects[i].bottomRight.y;
        rects[i].area = width * height;
    }
    
    // Complex computation involving bitwise operations and math functions
    int a = rects[0].area;
    int b = rects[1].area;
    
    int step1 = (a & b) | ((a ^ b) << 2);
    double step2 = pow(step1, 1.5);
    int step3 = (int)(step2) % 100;
    
    // String manipulation to derive a value
    char buffer[50];
    sprintf(buffer, "%d", step3);
    int len = strlen(buffer);
    int char_sum = 0;
    for(int i = 0; i < len; i++) {
        char_sum += buffer[i] - '0';
    }
    
    // Final complex calculation
    int result = ((step3 >> 2) & 0xF) * char_sum + (int)(sin(M_PI/6) * 100);
    
    printf("Result: %d\n", result);
    return 0;
}