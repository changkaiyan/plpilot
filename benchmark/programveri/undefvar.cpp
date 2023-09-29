#include <iostream>

int main() {
    int x = 5;
    
    // Use of undefined variable y
    std::cout << y;

    {
        int z = 10;
        // z is defined here, so this is okay
        std::cout << z; 
    }

    // Use of z outside of scope
    std::cout << z;

    // Use of undefined function foo()
    foo();

    // Attempt to access member of undefined type T
    T t;
    t.x;
}