    global promedio_asm
    section .text
; RDI<-*vector
; RSI<-size
promedio_asm:
    xor rax,rax
    mov rcx, rsi
    
lazo:
    add eax,[rdi]
    add rdi, 4
    dec rcx
    jnz lazo
    xor rdx,rdx
    
    div esi
    ret