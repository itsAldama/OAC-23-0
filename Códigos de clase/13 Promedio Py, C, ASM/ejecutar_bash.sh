nasm -f elf64 promedio_asm.asm -o promedio_asm.o
gcc -shared promedio_asm.o lib_promedio_c.c -o lib_promedio.so