section .data
    mensaje_in db "Ingrese los numeros: "
    mensaje_in_len equ $-mensaje_in

    mensaje_out db "La solucion es: "
    mensaje_out_len equ $-mensaje_out

    nl db 10

section .bss
    num1 resb 1
    num2 resb 1
    num3 resb 1
    resultado resb 1
    espacio resb 1

section .text
    global _start

_start:
    ; sys_write
    mov rax, 1
    mov rdi, 1
    mov rsi, mensaje_in
    mov rdx, mensaje_in_len
    syscall

    ; sys_read
    mov rax, 0
    mov rdi, 0
    mov rsi, num1
    mov rdx, 1
    syscall

    mov rax, 0
    mov rdi, 0
    mov rsi, espacio
    mov rdx, 1
    syscall
    
    mov rax, 0
    mov rdi, 0
    mov rsi, num2
    mov rdx, 1
    syscall

    mov rax, 0
    mov rdi, 0
    mov rsi, espacio
    mov rdx, 1
    syscall
    
    mov rax, 0
    mov rdi, 0
    mov rsi, num3
    mov rdx, 1
    syscall

    ; convertir los ascci en int
    mov r8b, [num1]
    sub r8b, '0'
    mov r9b, [num2]
    sub r9b, '0'
    mov r10b, [num3]
    sub r10b, '0'

    mov rax, 1
    mov rdi, 1
    mov rsi, mensaje_out
    mov rdx, mensaje_out_len
    syscall

    mov rax, r9
    ; se guarda en rax los 8 bits menos significativos
    mul r9
    ; guardamos b^2 en r11
    mov r11, rax

    ; copiamos num1 en rax
    mov rax, r8
    ; multiplicamos el num1 x num3 y se guarda en rax
    mul r10
    ; copiamos 4 en un registro cualquiera
    mov r12, 4
    ; mutiplicamos num1*num3 x 4 y se guarda en rax
    mul r12

    mov r13, rax
    sub r11, r13

    mov rax, 0
    mov rdi, 0
    mov rsi, r11
    mov rdx, 8
    syscall
    
fin:
    mov rax, 60
    mov rdi, 0
    syscall
