section .data
    message db "Hello World", 10, 0

section .text
    global _start

_start:
    ; rax apunta al principio de la cadena
    mov rax, message
    ; rbx se empleará como contador
    mov rbx, 0

_count_loop:
    inc rax
    inc rbx
    mov cl, [rax]
    cmp cl, 0
    jne _count_loop

; SYS_WRITE
    mov rax, 1
    mov rdi, 1
    mov rsi, message
    mov rdx, rbx
    syscall

; SYS_EXIT
    mov rax, 60
    mov rdi, 0
    syscall