section .data
    question db "What is your name?: "
    lenq equ $- question
    greet db "Hello, "
    leng equ $- greet

section .bss
    ; Reservamos 16 bytes para el nombre que será ingresado
    name resb 16

section .text
    global _start

; SYS_WRITE
_start:
    mov rax, 1
    mov rdi, 1
    mov rsi, question
    mov rdx, lenq
    syscall

; SYS_READ
    mov rax, 0
    mov rdi, 0
    mov rsi, name
    mov rdx, 16
    syscall

; SYS_WRITE
    mov rax, 1
    mov rdi, 1
    mov rsi, greet
    mov rdx, leng
    syscall

; SYS_WRITE
    mov rax, 1
    mov rdi, 1
    mov rsi, name
    mov rdx, 16
    syscall

; SYS_EXIT
    mov rax, 60
    mov rdi, 0
    syscall



