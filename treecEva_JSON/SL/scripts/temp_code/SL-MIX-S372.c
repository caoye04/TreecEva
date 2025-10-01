#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

struct Point {
    int x;
    int y;
};

struct Rectangle {
    struct Point topLeft;
    struct Point bottomRight;
};

union Data {
    int i;
    float f;
    char str[MAX_LEN];
};

int calculateArea(struct Rectangle rect) {
    int width = rect.bottomRight.x - rect.topLeft.x;
    int height = rect.topLeft.y - rect.bottomRight.y;
    return width * height;
}

int main() {
    struct Rectangle rects[2];
    
    rects[0].topLeft.x = 2;
    rects[0].topLeft.y = 10;
    rects[0].bottomRight.x = 8;
    rects[0].bottomRight.y = 4;
    
    rects[1].topLeft.x = 5;
    rects[1].topLeft.y = 15;
    rects[1].bottomRight.x = 12;
    rects[1].bottomRight.y = 7;
    
    int areas[2];
    areas[0] = calculateArea(rects[0]);
    areas[1] = calculateArea(rects[1]);
    
    int xor_result = areas[0] ^ areas[1];
    int shifted = xor_result << 2;
    
    union Data d;
    d.i = shifted;
    
    double sqrt_val = sqrt((double)d.i);
    long rounded = lround(sqrt_val);
    
    char buffer[MAX_LEN];
    sprintf(buffer, "%ld", rounded);
    
    int str_len = strlen(buffer);
    int bit_count = 0;
    for(int i=0; i<str_len; i++) {
        if(buffer[i] == '1') bit_count++;
    }
    
    int result = (bit_count << 3) | (str_len & 0x7);
    
    printf("Result: %d\n", result);
    
    return 0;
}