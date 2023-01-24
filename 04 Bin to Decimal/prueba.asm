; Piden convertir un número string de 8 bits a decimal almacenando en memoria

section .data
    binstr db "10101010"; Número a evaluar
    result db 0

section .text
    global _start

_start:
    ; Guardamos la posición de memoeria en R15
    mov r15, binstr 
    ; Como son 8 bits, empezamos de 128
    mov r14, 128 
    ; Divisor de las potencias de 2
    mov r13, 2
    ; Acumulador del resultado
    mov r12, 0

mul_bucle:
    ; Guardamos los 8 bits en AL
    mov al, [r15]
    ; Restamos los valores ASCII
    sub al, 48
    ; RAX = RAX*R14
    mul r14
    ; Acumulamos en r12
    add r12, rax

sig_pa:
    ; Para dividir siempre tenemos que limpiar el registro que vamos a utilizar, Limpiamos RDX
    xor rdx, rdx
    ; Guardamos en RAX para dividir
    mov rax, r14
    ; Dividimos entre la potencia de 2
    div r13
    ; Devolvemos al divisor
    mov r14, rax
    ; Incrementamos posición de memoria
    inc r15
    ; Comparamos con 0 para ver si terminó la cadena
    cmp r14, 0
    jne mul_bucle

fin:
    mov [result], r12b
    
    mov rax, 60
    mov rdi, 0
    syscall