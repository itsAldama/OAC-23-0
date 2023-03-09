section .data
    number1 dq 12
    number2 dq 18
section .text
    global _start

_start:
    mov rax, [number1] ; Move number1 into rax
    mov rbx, [number2] ; Move number2 into rbx

calculate:
    cmp rax, rbx ; Compare rax and rbx
    jge swap ; If rax is greater or equal, swap
    sub rbx, rax ; Subtract rax from rbx
    jmp calculate ; Loop back

swap:
    xchg rax, rbx ; Swap rax and rbx
    sub rax, rbx ; Subtract rbx from rax
    jmp calculate ; Loop back

exit:
    ; mcd is now stored in rax
    ; Exit the program
    mov rdi, 0
    mov rax, 60
    syscall