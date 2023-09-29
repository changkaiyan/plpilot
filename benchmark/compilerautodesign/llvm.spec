LLVM-IR has a rich set of instructions that can be used to implement programs. Here are some examples:

add: adds two values and stores the result in a variable.




%sum = add i32 %a, %b
sub: subtracts two values and stores the result in a variable.




%diff = sub i32 %a, %b
mul: multiplies two values and stores the result in a variable.




%product = mul i32 %a, %b
sdiv: signed integer division between two values and stores the result in a variable.




%quotient = sdiv i32 %a, %b
fadd: adds two floating-point values and stores the result in a variable.




%sum = fadd float %a, %b
fsub: subtracts two floating-point values and stores the result in a variable.




%diff = fsub float %a, %b
fmul: multiplies two floating-point values and stores the result in a variable.




%product = fmul float %a, %b
fdiv: divides two floating-point values and stores the result in a variable.




%quotient = fdiv float %a, %b
load: reads a value from memory and stores it in a variable.




%value = load i32, i32* %addr
store: writes a value to memory.




store i32 %value, i32* %addr
call: calls a function with arguments and returns a value.




%result = call i32 @function(i32 %arg1, i32 %arg2)
In this case, @function is the name of the function being called.

Control Flow
LLVM-IR supports several control flow instructions, including:

br: unconditional branch to a basic block.




br label %label
br i1: conditional branch to one of two basic blocks.




br i1 %condition, label %true_block, label %false_block
switch: branch based on an integer value.




switch i32 %value, label %default_block [ i32 0, label %case1 ] [ i32 1, label %case2 ]
ret: return from the current function.




ret void
Functions
Function definitions in LLVM-IR start with the define keyword, followed by the return type, function name, and a list of arguments.




define i32 @my_function(i32 %arg1, i32 %arg2) {
  ; function body here
}
Note that the function body is enclosed in curly braces. Each basic block is labeled with a unique identifier, which is used to reference it in control flow instructions.

Here is an example of a basic function that adds two integers and returns the result:




define i32 @add(i32 %a, i32 %b) {
entry:
  %sum = add i32 %a, %b
  ret i32 %sum
}
Modules
A module in LLVM-IR is a collection of functions. Modules can be loaded, optimized, and stored separately from the rest of the program. A typical module starts with the target triple directive, followed by a list of global variables and function definitions.




target triple = "x86_64-apple-macosx10.13.0"

@global_var = global i32 0

declare i32 @printf(i8*, ...)

define i32 @main(i32 %argc, i8** %argv) {
  ; function body here
}
In this example, @global_var is a global variable, declare is used to declare the external function printf, and define is used to define the program's main function.