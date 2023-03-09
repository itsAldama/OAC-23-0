section .data
    mensaje db "Hola Mundo", 0

section .bss
    inverse resb 20

section .text
    global _start

_start:
    ; Almaceno la dirección de memoria del mensaje a RAX
    mov rax, mensaje
    mov rbx, 0

_count_loop:
    ; Siguiente dirección del mensaje
    inc rax
    ; Incrementamos el contador de letras
    inc rbx
    mov cl, [rax]
    cmp cl, 0
    jne _count_loop

    mov r8, rbx
    ; R9 apunta a la dirección de donde comienza el string invertido
    mov r9, inverse
    ; RAX apunta al inicio del mensaje
    mov rax, mensaje
    ; RAX apunta al final del mensaje 
    add rax, r8

_reverse:
    dec rax
    mov r10, [rax]
    mov [r9], r10
    inc r9
    cmp rax, mensaje
    jne _reverse

    ; Agregamos el cambio del línea al final
    mov [r9], byte 10
    ; Para que salga el salto de línea
    inc rbx
    
    mov rax, 1
    mov rdi, 1
    mov rsi, inverse
    mov rdx, rbx
    syscall

    mov rax, 60
    mov rdi, 0
    syscall