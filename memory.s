.code16
_data:
	.word 0xDEAD

.org 0x1000
xor %ax, %ax
mov %ax, %ds
mov %ax, %ss
mov %ax, %sp
pop %ax

