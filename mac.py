import random

def random_mac_address() :
    mac = [random.randint(0, 255) for a in range(6)]
    mac_address = ":".join(["{:02X}".format(byte) for byte in mac])
    return mac_address

allowed_devices = [
    "00:11:2A:3F:4E:5A",
    "AA:BB:C3:D4:E5:F6",
    "AB:BC:CD:DE:EF:FA",
    "1A:2B:3C:4D:5E:6F"
]

blocked_devices = [
    "11:22:33:44:55:66",
    "FF:EE:DD:CC:BB:AA",
    "23:43:3A:5F:62:FA"
]

device_mac = random_mac_address()
print("Generated MAC address:", device_mac)

if device_mac in allowed_devices:
    print("grant access.")
elif device_mac in blocked_devices:
    print("deny access.")
else:
    print("Further authentication required.")
