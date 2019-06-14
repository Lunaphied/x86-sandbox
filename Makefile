all: samp.bin

%.o: %.s
	as --32 -o $@ $<
%.bin: %.o
	objcopy $< -O binary $@
