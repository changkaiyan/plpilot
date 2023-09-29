#include <stdio.h>

int main() {
    int x = 5;
    char *ptr;    // Pointer to char
    
    // Assign pointer to point to int - invalid!
    ptr = &x;    
    
    // Try to print int through char pointer - undefined behavior
    printf("x = %d\n", *ptr);
}