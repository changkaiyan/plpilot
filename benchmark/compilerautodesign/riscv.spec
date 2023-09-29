Here are some of the formal specification of RISC-V ISA.

Instruction Formats:
RISC-V ISA has three types of instruction formats. These are:

R-Type: These are Register Operands.



      | 31     25| 24     20| 19     15| 14     12| 11     7| 6      0 |
      |  funct7  |    rs2   |    rs1   |  funct3  |   rd    |  opcode |
I-Type: These are Immediate Instructions.



      | 31        20| 19     15| 14     12| 11     7| 6      0 |
      |  immediate |    rs1   |  funct3  |   rd    |  opcode |
S-Type: These are Store Instructions.



      | 31        25| 24     20| 19        15| 14     12| 11     7| 6      0 |
      |    offset   |    rs2    |      rs1   |  funct3  |   func  |  opcode |
Instruction Types:
RISC-V ISA has several types of instructions. Some of them are listed below:

Load Instructions: These instructions load values from memory.



lb    - Load Byte
lh    - Load Halfword
lw    - Load Word
ld    - Load Doubleword
Store Instructions: These instructions store values to memory.



sb    - Store Byte
sh    - Store Halfword
sw    - Store Word
sd    - Store Doubleword
Arithmetic Instructions: These instructions implement basic arithmetic operations.



add     - Add
sub     - Subtract
sll     - Shift Left Logical
slt     - Set Less Than
sltu    - Set Less Than Unsigned
xor     - Exclusive OR
srl     - Shift Right Logical
sra     - Shift Right Arithmetic
or      - OR
and     - AND
Control Transfer Instructions: These instructions implement program control transfers.



jal     - Jump and Link
jalr    - Jump and Link Register
beq     - Branch Equal
bne     - Branch Not Equal
blt     - Branch Less Than
bge     - Branch Greater Than Equal To
Registers:
RISC-V ISA has a total of 32 General Purpose Registers, among which x0 is a hardwired zero register. The remaining 31 registers (x1-x31) are used to store data and addresses. These registers are 32-bit wide.

Addressing:
RISC-V ISA uses byte addressing. Instructions can use either the immediate values or the registers to provide the memory addresses.