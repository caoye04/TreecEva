#define M_PI 3.14159265358979323846
#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

int calculate_area(struct Rectangle rect) {
    int width = rect.bottomRight.x - rect.topLeft.x;
    int height = rect.topLeft.y - rect.bottomRight.y;
    return width * height;
}

int main() {
    struct Rectangle rects[2] = {
        {{10, 20}, {30, 5}},
        {{5, 15}, {25, 0}}
    };
    
    int areas[2];
    for (int i = 0; i < 2; i++) {
        areas[i] = calculate_area(rects[i]);
    }
    
    int max_area = MAX(areas[0], areas[1]);
    
    double angle = M_PI / 4; // 45 degrees
    double sin_val = sin(angle);
    double cos_val = cos(angle);
    
    int bitwise_result = (max_area << 2) ^ ((int)(sin_val * 100) & (int)(cos_val * 100));
    
    int final_result = (int)(sqrt(bitwise_result) * 10);
    
    printf("Result: %d\n", final_result);
    
    return 0;
}