; Para ensamblar, ejecutamos:
;           form  arch           out name
;   nasm -f elf64 helloworld.asm -o helloworld.o
; Para enlazar diferentes archivos de salida (liberias), ejecutamos:
;   ld helloworld.o -o helloworld
; Para correr el ejecutable:
;   ./helloworld

; SEGMENTO DE DATOS
; Se empleara la etiqueta message y se reservaran elementos de 8 bits.
; Cada letra de la cadena se corresponde con un elemento de 8 bits.
; El número 10 se corresponde con el caracter '\n'
section .data
    message db "Hello World", 10
    ; equ es una equivalencia
    len equ $-message

; SEGMENTO DE TEXTO
section .text
    ; para que se sepa que acá arranca el código
    global _start
; etiqueta, texto que representa una dirección de memoria
_start:
    ; LLAMADA AL SISTEMA
    ; rax => ID <= 1 : sys_write
    ; rdi => Primer parámetro   : output
    ; rsi => Segundo parámetro  : dirrecion del mensaje
    ; rdx => Tercer parámetro   : longitud del mensaje
    mov rax, 1       ; 1 para imprimir
    mov rdi, 1
    mov rsi, message ; inicio de lo que imprime
    mov rdx, len     ; final de lo que imprime
    syscall

    ; LLAMADA AL SISTEMA
    ; rax => ID <= 60 : sys_exit
end:
    mov rax, 60
    mov rdi, 0
    syscall
    
