.code16
jmp main

gdt:
_gdt_null:
	.quad 0x0
_gdt_code:
	.word 0xFFFF
	.word 0x0
	.byte 0x0
	.byte 0b10011010
	.byte 0b10001111
	.byte 0x0
_gdt_data:
	.word 0xFFFF
	.word 0x0
	.byte 0x0
	.byte 0b10010010
	.byte 0b10001111
	.byte 0x0
gdt_end:
_data:
	.word gdt_end-gdt
	.long gdt
main:
	cli
	lgdt _data

	mov %cr0, %eax
	or $0x1, %eax
	mov %eax, %cr0
	ljmp $0x8, $main_p16
.code16
main_p16:
	mov $0x10, %ax
	mov %ax, %ds
	mov %ax, %ss
	mov %ax, %gs
	mov %ax, %es
	mov %ax, %fs
	movw $0x20, _data
	mov _data, %ax

