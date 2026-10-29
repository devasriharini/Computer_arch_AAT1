# Rotate Left Without Carry (ROL)

def rol(value, positions):
    print("\n--- Rotate Left Without Carry (ROL) ---")
    print("Original number:", format(value, '08b'))

    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) & 0xFF) | msb

        print("After rotation", i + 1, ":", format(value, '08b'))

    print("Final result:", format(value, '08b'))


# Rotate Left Through Carry (RCL)

def rcl(value, carry, positions):
    print("\n--- Rotate Left Through Carry (RCL) ---")
    print("Original number:", format(value, '08b'))
    print("Initial carry:", carry)

    for i in range(positions):
        msb = (value >> 7) & 1
        value = ((value << 1) & 0xFF) | carry
        carry = msb

        print("After rotation", i + 1, ":", format(value, '08b'))
        print("Carry:", carry)

    print("Final result:", format(value, '08b'))
    print("Final carry:", carry)


# (a) ROL 11110110 by 2 positions
rol(0b11110110, 2)

# (b) RCL 10000110 by 2 positions
# Assume initial carry = 0
rcl(0b10000110, 0, 2)