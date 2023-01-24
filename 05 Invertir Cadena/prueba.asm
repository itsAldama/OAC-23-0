section .data
    mensaje db "Hola Mundo", 0
    contador dq 0

section .bss
    inverse resb 20

section .text
    global _start

_start:
    ; Almaceno la dirección de memoria del mensaje a RAX
    mov rax, mensaje
    mov rbx, contador

_count_loop:
    ; Siguiente dirección del mensaje
    inc rax
    ; Incrementamos el contador de letras
    inc qword [rbx]
    mov cl, [rax]
    cmp cl, 0
    jne _count_loop

    mov r9, inverse
    ; RAX apunta al inicio del mensaje

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
    inc qword [rbx] 
    
    mov rax, 1
    mov rdi, 1
    mov rsi, inverse
    mov rdx, [rbx]
    syscall

    mov rax, 60
    mov rdi, 0
    syscall