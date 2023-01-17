section .data
    strbin db "10100101"
    result db 0
    potencia db 7
section .text
    global _start
  _start:
    ; Guardamos la posición de memoeria en R15
    mov r15, strbin 
    ; potencias de 2
    mov r13, 2
    ; Acumulador del resultado
    mov r12, 0 
    mov r8, 0
    bucle:
         ;Guarda el valor de la potencia
    mov r14, [potencia]
        mov bl, [r15]
        sub bl, 48
        Potencia:
            mul r13
            add r10,rax
            dec r14
            cmp r14, 0
            jne Potencia
        inc r8
        cmp r8,7
        jne bucle
    fin:
    mov [result], r12b

    mov rax, 1
    mov rdi, 1
    mov rsi, result
    mov rdx, 8
    syscall

    mov rax, 60
    mov rdi, 0
    syscall