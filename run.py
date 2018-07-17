import os
import libvirt

conn = libvirt.open(os.environ['QEMU_PATH'])
names = conn.listDefinedDomains()

print(names)