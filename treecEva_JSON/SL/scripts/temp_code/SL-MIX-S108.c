#define _USE_MATH_DEFINES
#include <stdio.h>
#include <math.h>
#include <string.h>

#define MAX_LEN 100

// Function to compute factorial recursively
long long factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);
}

// Function to reverse a string in place
void reverse_string(char* str) {
    int len = strlen(str);
    for (int i = 0; i < len / 2; i++) {
        char temp = str[i];
        str[i] = str[len - i - 1];
        str[len - i - 1] = temp;
    }
}

// Structure representing a complex number
typedef struct {
    double real;
    double imag;
} Complex;

// Function to multiply two complex numbers
Complex multiply_complex(Complex a, Complex b) {
    Complex result;
    result.real = a.real * b.real - a.imag * b.imag;
    result.imag = a.real * b.imag + a.imag * b.real;
    return result;
}

int main() {
    // Initialize variables
    int a = 5, b = 3;
    double x = 2.5, y = 4.0;
    char buffer[MAX_LEN] = "HELLO";
    
    // Perform arithmetic operations
    long long fact_a = factorial(a);
    long long fact_b = factorial(b);
    
    // Bitwise operations
    int xor_result = a ^ b;
    int shift_result = a << 2;
    
    // Trigonometric and logarithmic operations
    double sin_x = sin(x);
    double log_y = log(y);
    
    // String manipulation
    reverse_string(buffer);
    int str_len = strlen(buffer);
    
    // Complex number operations
    Complex c1 = {3.0, 4.0};
    Complex c2 = {1.0, 2.0};
    Complex c3 = multiply_complex(c1, c2);
    
    // Nested conditional logic
    int condition1 = (fact_a > 100) && (xor_result < 10);
    int condition2 = (sin_x > 0.5) || (str_len == 5);
    
    // Compute intermediate values based on conditions
    long long intermediate1 = condition1 ? fact_a / fact_b : fact_b / fact_a;
    double intermediate2 = condition2 ? sin_x * log_y : sin_x + log_y;
    
    // Final computation involving multiple data types
    long long target_result = (long long)(intermediate1 * c3.real + shift_result * str_len - (long long)intermediate2);
    
    // Adjust result using modulo operation to ensure it's within expected range
    target_result = target_result % 1000;
    
    // Ensure positive result
    if (target_result < 0) target_result += 1000;
    
    printf("Result: %lld\n", target_result);
    
    return 0;
}