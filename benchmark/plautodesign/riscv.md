lw a0, n         # Load n
lw a1, result    # Load result
sub a0, a0, 1    # Decrement n
mul a1, a1, a0   # Multiply result by n
sw a1, result    # Store result
bnez a0, loop    # Loop if n != 0

lw a0, result
li a7, 1         # Set syscall number (print_int)
ecall            # Call kernel

li a7, 10
ecall