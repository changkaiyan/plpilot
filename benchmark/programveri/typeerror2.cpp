#include <iostream>

// Create custom types
struct Type1
{
    int x;
};

struct Type2
{
    double x;
};
void foo(Type2 t) {}

// Type mismatch, cannot return Type2 from function returning Type1
Type1 bar()
{
    return t2;
}
int main()
{
    Type1 t1;
    t1.x = 5;

    Type2 t2;
    t2.x = 3.14;

    // Type mismatch, cannot assign Type1 to Type2
    t2 = t1;

    // Type mismatch, cannot assign Type2 to Type1
    t1 = t2;

    // Type mismatch, cannot pass Type1 argument to function expecting Type2

    foo(t1);

    bar();
}