#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

int compute_area(struct Rectangle rect) {
    int width = abs(rect.bottomRight.x - rect.topLeft.x);
    int height = abs(rect.bottomRight.y - rect.topLeft.y);
    return width * height;
}

int recursive_sum(int n) {
    if (n <= 0) return 0;
    return n + recursive_sum(n - 2);
}

int main() {
    struct Rectangle rects[2];
    
    rects[0].topLeft.x = 1;
    rects[0].topLeft.y = 5;
    rects[0].bottomRight.x = 7;
    rects[0].bottomRight.y = 1;
    
    rects[1].topLeft.x = 3;
    rects[1].topLeft.y = 8;
    rects[1].bottomRight.x = 9;
    rects[1].bottomRight.y = 2;
    
    int area1 = compute_area(rects[0]);
    int area2 = compute_area(rects[1]);
    
    int combined_areas = (area1 << 2) ^ (area2 >> 1);
    
    double sqrt_combined = sqrt((double)combined_areas);
    int truncated_sqrt = (int)sqrt_combined;
    
    int sum_odd = recursive_sum(truncated_sqrt);
    
    int final_result = (sum_odd & 0xF) | ((truncated_sqrt % 5) << 4);
    
    printf("Result: %d\n", final_result);
    return 0;
}