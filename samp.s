.code16
mov $0x4, %eax
mov $0x4, %ebx
add %ebx, %eax
inc %ebx
mov $0x4, %dx
a:
	dec %ebx
	mov %ebx, %eax
	out %eax, %dx
	out %ax, %dx
	out %al, %dx
	jne a
