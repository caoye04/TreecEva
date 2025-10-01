#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point top_left;
    struct Point bottom_right;
};

int calculate_area(struct Rectangle r) {
    return abs((r.bottom_right.x - r.top_left.x) * (r.top_left.y - r.bottom_right.y));
}

int bit_operation_chain(int a, int b) {
    int step1 = a & b;
    int step2 = step1 << 2;
    int step3 = step2 ^ 0xF0;
    int step4 = ~step3;
    return step4 & 0xFF;
}

int main() {
    struct Rectangle rect_array[2];
    
    rect_array[0].top_left.x = 3;
    rect_array[0].top_left.y = 7;
    rect_array[0].bottom_right.x = 9;
    rect_array[0].bottom_right.y = 2;
    
    rect_array[1].top_left.x = -2;
    rect_array[1].top_left.y = 5;
    rect_array[1].bottom_right.x = 4;
    rect_array[1].bottom_right.y = -1;
    
    int area1 = calculate_area(rect_array[0]);
    int area2 = calculate_area(rect_array[1]);
    
    double sqrt_area1 = sqrt((double)area1);
    double pow_area2 = pow((double)area2, 1.5);
    
    int combined_areas = (int)(sqrt_area1 + pow_area2);
    
    int bitwise_result = bit_operation_chain(area1, area2);
    
    int logic_expr = ((area1 > 20) && (area2 < 50)) || ((combined_areas % 7) == 0);
    
    int mixed_calc = (bitwise_result * 3) - (logic_expr ? 100 : 50) + (int)floor(sqrt_area1);
    
    int final_result = mixed_calc / 2 + (mixed_calc % 3);
    
    printf("Result: %d\n", final_result);
    
    return 0;
}