section .data
    num db '7'
    nl db 10

section .text
    global _start

_start:
    mov r8, num
    mov r9, [r8]
    inc r9
    mov [r8], r9

    mov rax, 1
    mov rdi, 1
    mov rsi, r8
    mov rdx, 1
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, nl
    mov rdx, 1
    syscall

    mov rax, 60
    mov rdi, 0
    syscall