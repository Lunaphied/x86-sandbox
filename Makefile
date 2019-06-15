all: move32.data.bin move32.code.bin

%.o: %.s
	as --32 -o $@ $<
%.elf: %.o
	ld -T link.ld -o $@ $<
%.data.bin: %.elf
	objcopy $< -O binary -j .data $@
%.code.bin: %.elf
	objcopy $< -O binary -j .text $@
