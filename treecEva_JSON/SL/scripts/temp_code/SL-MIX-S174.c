#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX(a,b) ((a) > (b) ? (a) : (b))

struct Point {
    int x;
    int y;
};

struct Circle {
    struct Point center;
    double radius;
};

union Data {
    int i;
    float f;
    char str[20];
};

int main() {
    struct Circle circles[3] = {{{10, 20}, 5.0}, {{-5, 15}, 3.5}, {{0, 0}, 2.0}};
    union Data udata;
    int values[4][4] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {13, 14, 15, 16}};
    
    int sum = 0;
    for(int i=0; i<3; i++) {
        sum += (int)ceil(circles[i].radius);
    }
    
    int mask = 0xF0;
    int shifted = (sum << 2) & mask;
    
    strcpy(udata.str, "complex");
    int strlength = strlen(udata.str);
    
    double product = 1.0;
    for(int i=0; i<4; i++) {
        for(int j=0; j<4; j++) {
            if(values[i][j] % 2 == 0) {
                product *= sqrt((double)values[i][j]);
            }
        }
    }
    
    int xor_result = shifted ^ strlength;
    
    int result = (int)(product + xor_result);
    
    printf("Result: %d\n", result);
    return 0;
}