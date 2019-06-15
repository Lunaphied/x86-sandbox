from unicorn import *
from unicorn.x86_const import *

X86_CODE = open('move32.code.bin' ,'rb').read()
X86_DATA = open('move32.data.bin' ,'rb').read()

ADDRESS = 0x1000

def hook_code(uc, address, size, user_data):
    print(">>> Tracing instruction at 0x%x, size = 0x%x" % (address, size))
    eflags = uc.reg_read(UC_X86_REG_EFLAGS)
    print(">>> --- EFLAGS is 0x%x" %eflags)

def hook_out(uc, port, size, value, user_data):
    print(">>> PORT_WRITE: PORT = 0x%x, SIZE = 0x%x, VALUE = 0x%x" %
            (port, size, value))
def hook_mem_invalid(uc, access, address, size, value, user_data):
    print (">>> Invalid memory access at 0x%x, size = %u, value = 0x%x" \
            %(address, size, value))
    return False
def hook_interrupt(uc, except_idx, user_data):
    print (">>> Unhandled exception = 0x%x" %except_idx)

try:
    mu = Uc(UC_ARCH_X86, UC_MODE_16)
    #mu.mem_map(0x0, 2*1024)
    mu.mem_map(0x0, 2 * 1024 * 1024)
    mu.mem_write(0x0, X86_DATA)
    mu.mem_write(0x1000, X86_CODE)
    mu.hook_add(UC_HOOK_INSN, hook_out, None, 1, 0, UC_X86_INS_OUT)
    mu.hook_add(UC_HOOK_MEM_READ_UNMAPPED | UC_HOOK_MEM_WRITE_UNMAPPED, hook_mem_invalid)
    mu.hook_add(UC_HOOK_CODE, hook_code)
    mu.hook_add(UC_HOOK_INTR, hook_interrupt)
    mu.emu_start(ADDRESS, ADDRESS+len(X86_CODE))
    print("Emulation done. Printing CPU context")
    r_eax = mu.reg_read(UC_X86_REG_EAX)
    r_ebx = mu.reg_read(UC_X86_REG_EBX)
    r_sp = mu.reg_read(UC_X86_REG_SP)
    r_ip = mu.reg_read(UC_X86_REG_IP)
    r_ds = mu.reg_read(UC_X86_REG_DS)
    r_cs = mu.reg_read(UC_X86_REG_CS)
    r_gdtr = mu.reg_read(UC_X86_REG_GDTR)
    r_cr0 = mu.reg_read(UC_X86_REG_CR0)
    print(">>> EAX = 0x%x" %r_eax)
    print(">>> EBX = 0x%x" %r_ebx)
    print(">>> SP = 0x%x" %r_sp)
    print(">>> IP = 0x%x" %r_ip)
    print(">>> DS = 0x%x" %r_ds)
    print(">>> CS = 0x%x" %r_cs)
    print(">>> GDTR BASE = 0x%x, LIMIT = 0x%x" % (r_gdtr[1], r_gdtr[2]))
    print(">>> CR0 = %s" % bin(r_cr0))
except UcError as e:
    print("ERROR: %s" %e)
