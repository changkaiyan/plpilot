#include <stdio.h>

int main() {
    int x = 5;
    char y = 'a';
    
    x = y;  // Type error, cannot assign char to int
    printf("%d\n", x);  

    printf("%c", x); // Type error, cannot print int as char

    double z = 3.14;
    z = x; // Type error, cannot assign int to double  

    y = z; // Type error, cannot assign double to char
}