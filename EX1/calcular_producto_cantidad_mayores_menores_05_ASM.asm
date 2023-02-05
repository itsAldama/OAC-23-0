; nasm -f elf64 calcular_producto_cantidad_mayores_menores_05_ASM.asm -o calcular_producto_cantidad_mayores_menores_05_ASM.o    

    global calcular_producto_cantidad_mayores_menores_05_ASM
    section .text

calcular_producto_cantidad_mayores_menores_05_ASM:
    ; rdi <- arreglo numeros
    ; rsi <- cantidad de numeros
    ; xmm0 <- constante 0.5

    ; r8 es contador de mayores a 0.5
    ; r9 es contador de menores a 0.5
    mov r8, 0
    mov r9, 0

    loop:
        movsd xmm1, [rdi]
        ucomisd xmm1, xmm0
        jg mayor_a_05

        ; si es menor a 0.5
        inc r9

        siguiente:
            add rdi, 8
            dec rsi
            jnz loop

    fin:
        mov rax, r8
        ; rdx : rax <- rax*r9
        mul r9
        ret
        

    mayor_a_05:
        inc r8
        jmp siguiente


