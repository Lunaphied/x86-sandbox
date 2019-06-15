OUTPUT_FORMAT(elf32-i386)
OUTPUT_ARCH(i386)
SECTIONS {
	. = 0x1000;
	.text : {
		*(.text);
	}
	.data 0x0:
	{
		*(.data);
	}	
}
