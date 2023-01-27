global asmFloatInnerProd
    section .text

asmFloatInnerProd:
	xorpd	xmm0,	xmm0
	xorpd	xmm1,	xmm1
	xorpd	xmm2,	xmm2
	cmp	rdx,	0
	je	done
next:
	movsd	xmm0,	[rdi]
	movsd	xmm1,	[rsi]
	mulsd	xmm0,	xmm1
	addsd	xmm2,	xmm0
	add	rdi,	8
	add	rsi,	8
	sub	rdx,	1
	jnz	next	
done:
	movsd	xmm0,	xmm2
	ret