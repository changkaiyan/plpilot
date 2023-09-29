#include <stdio.h>

int main() {
    char c = 'A';
    char d = 'B';
    
    // Common expressions: 
    
    // Arithmetic - Modulus 
    int mod = 15 % 4;    // mod = 3
    printf("15 %% 4 = %d\n", mod);
    
    // Relational - Not equal to 
    int not_equal = c != d;  // not_equal = 1 (true)
    printf("c != d = %d\n", not_equal);
    
    // Logical - NOT
    int not = !(c == d);   // not = 1 (true)
    printf("!(c == d) = %d\n", not);
    
    // Assignment 
    int x = 5;
    x += 10;               // x = x + 10 = 15
    printf("x += 10; x = %d\n", x);
    
    x *= 2;                // x = x * 2 = 30
    printf("x *= 2; x = %d\n", x);
    
    // Conditional - If-Else
    if (x > 10) {
        printf("x is greater than 10\n"); 
    } else {
        printf("x is less than or equal to 10\n");
    }
    
    // Loops - For loop
    for (int i = 0; i < 5; i++) {
        printf("i = %d\n", i);
    }
    
    // Loops - While loop
    int j = 0;
    while (j < 3) {
        printf("j = %d\n", j);
        j++;
    }
} 