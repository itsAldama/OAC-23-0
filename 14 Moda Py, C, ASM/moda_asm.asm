    global moda_asm
    section .text
moda_asm:
; RDI<- arreglo
; RSI<- N
mov r8, RDI     ;arreglo[0]>R8
mov r9, RDI     ;arreglo[0]>R9
mov rcx, RSI
mov rdx, RSI

xor rax, rax    ;   cont_max
xor rbx,rbx     ;   cont
xorpd xmm1,xmm1 ;   valor_max

for_n:
    xor rbx,rbx
    mov rcx, rsi
    movss XMM3, [R9]    ;n
    
    for_m:
        movss XMM2, [R8]    ;m
        ucomiss XMM2,XMM3
        je incrementar
        ret_m:
        add r8, 4
        dec rcx
        jnz for_m
    
    cmp rbx, rax
    jg incrementar2
    ret_n:
    mov r8,rdi
    add r9, 4
    dec rdx
    jnz for_n

fin:
    movss xmm0,xmm1
    ret


incrementar:
    inc rbx
    jmp ret_m

incrementar2:
    mov rax, rbx
    movss XMM1, XMM3
    jmp ret_n