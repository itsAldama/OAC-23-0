section .data
    operando1 db "Ingrese primer operando: "
    operando1_len equ $-operando1
    operando2 db "Ingrese segundo operando: "
    operando2_len equ $-operando2
    operacion db "Seleccione operacion (1 -> suma, 2 -> resta, 3 -> mult): "
    operacion_len equ $-operacion
    
    msj_suma db "Seleccionó la operación de suma", 10
    msj_suma_len equ $-msj_suma
    msj_resta db "Seleccionó la operación de resta", 10
    msj_resta_len equ $-msj_resta
    msj_prod db "Seleccionó la operación de multiplicación", 10
    msj_prod_len equ $-msj_prod
    msj_incorrecto db "Opción incorrecta", 10
    msj_incorrecto_len equ $-msj_incorrecto

    msj_resultado db "El resultado de la operación es: "
    msj_resultado_len equ $-msj_resultado
    
    nl db 10

section .bss
    op1 resb 5
    op2 resb 5
    op resb 5
    resultado resb 1

section .text
    global _start

_start:
    ; Primer operando:
    ; SYS_WRITE
    mov rax, 1
    mov rdi, 1
    mov rsi, operando1
    mov rdx, operando1_len
    syscall

    ; SYS_READ
    mov rax, 0
    mov rdi, 0
    mov rsi, op1
    mov rdx, 5
    syscall

    ; Segundo operando:
    ; SYS_WRITE
    mov rax, 1
    mov rdi, 1
    mov rsi, operando2
    mov rdx, operando2_len
    syscall

    ; SYS_READ
    mov rax, 0
    mov rdi, 0
    mov rsi, op2
    mov rdx, 5
    syscall

    ; Operacion:
    ; SYS_WRITE
    mov rax, 1
    mov rdi, 1
    mov rsi, operacion
    mov rdx, operacion_len
    syscall

    ; SYS_READ
    mov rax, 0
    mov rdi, 0
    mov rsi, op
    mov rdx, 5
    syscall

    ; Validar opciones
    mov r9b, byte [op]
    ; ASCCI 49 -> 1
    cmp r9b, 49
    je suma
    ; 2
    cmp r9b, 50
    je resta
    ; 3
    cmp r9b, 51
    je multiplica
    jmp opcion_incorrecta

suma:
    mov rax, 1
    mov rdi, 1
    mov rsi, msj_suma
    mov rdx, msj_suma_len
    syscall

    mov r8, [op1]
    ; 48 <- 0 ASCCI
    sub r8, 48
    mov r9, [op2]
    sub r9, 48
    
    add r9, r8
    add r9, 48
    mov [resultado], r9
    
    call show_result

    call new_line
    jmp fin

show_result:
    mov rax, 1
    mov rdi, 1
    mov rsi, msj_resultado
    mov rdx, msj_resultado_len
    syscall

    mov rax, 1
    mov rdi, 1
    mov rsi, resultado
    mov rdx, 1
    syscall
    
    ret

new_line:
    mov rax, 1
    mov rdi, 1
    mov rsi, nl
    mov rdx, 1
    syscall
    ret

resta:
    mov rax, 1
    mov rdi, 1
    mov rsi, msj_resta
    mov rdx, msj_resta_len
    syscall

    mov r8, [op1]
    sub r8, 48
    mov r9, [op2]
    sub r9, 48
    sub r8, r9
    add r8, 48
    mov [resultado], r8

    call show_result
    call new_line

    jmp fin

multiplica:
    mov rax, 1
    mov rdi, 1
    mov rsi, msj_prod
    mov rdx, msj_prod_len
    syscall

    mov r8, [op1]
    sub r8, 48
    mov r9, [op2]
    sub r9, 48

    xor rax, rax
    xor rdx, rdx
    
    mov rax, r8
    mul r9
    mov r9, rax
    add r9, 48
    mov [resultado], r9

    call show_result
    call new_line

    jmp fin

opcion_incorrecta:
    mov rax, 1
    mov rdi, 1
    mov rsi, msj_incorrecto
    mov rdx, msj_incorrecto_len
    syscall

fin:
    mov rax, 60
    mov rdi, 0
    syscall