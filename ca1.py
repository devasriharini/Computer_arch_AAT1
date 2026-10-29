def to_twos_complement(value, bits=16):
  """Converts an integer to its 2's complement binary string of given bits."""
  if value < 0:
    value = (1 << bits) + value
  return format(value & ((1 << bits) - 1), f"0{bits}b")


def from_twos_complement(binary_str):
  """Converts a 2's complement binary string back to a signed integer."""
  bits = len(binary_str)
  value = int(binary_str, 2)
  if binary_str[0] == "1":
    value -= 1 << bits
  return value


def add_binary_signed(a, b, bits=16):
  """Performs signed addition in 16-bit 2's complement and checks for overflow."""
  mask = (1 << bits) - 1
  a_masked = a & mask
  b_masked = b & mask

  result = (a_masked + b_masked) & mask

  # Overflow detection for signed addition:
  # Occurs if operands have the same sign bit, but the result has a different sign bit.
  sign_a = (a_masked >> (bits - 1)) & 1
  sign_b = (b_masked >> (bits - 1)) & 1
  sign_res = (result >> (bits - 1)) & 1

  overflow = (sign_a == sign_b) and (sign_a != sign_res)
  return result, overflow


def evaluate_expression(op1, op, op2):
  # Subtraction a - b is computed as a + (-b)
  operand2_val = -op2 if op == "-" else op2

  # Perform 16-bit calculation
  res_16, overflow = add_binary_signed(op1, operand2_val, 16)
  decimal_result = from_twos_complement(format(res_16, "016b"))

  # 8-bit formatting for display purposes
  bin_8_op1 = to_twos_complement(op1, 8)
  bin_8_op2 = to_twos_complement(op2, 8)
  bin_16_res = to_twos_complement(res_16, 16)

  print(f"Expression: {op1} {op} ({op2})")
  print(f"  Operand 1 ({op1}) in 8-bit 2's complement : {bin_8_op1}")
  print(f"  Operand 2 ({op2}) in 8-bit 2's complement : {bin_8_op2}")
  print(
      f"  Result in 16-bit binary                  :"
      f" {bin_16_res[:8]} {bin_16_res[8:]}"
  )
  print(f"  Result in decimal                        : {decimal_result}")
  print(f"  Arithmetic Overflow                      :"
        f" {'Yes' if overflow else 'No'}")
  print("-" * 65)


if __name__ == "__main__":
  print("=== Signed Binary Arithmetic Verification (16-bit 2's Complement) ===")
  print("-" * 65)

  # Test cases
  evaluate_expression(35, "-", 29)
  evaluate_expression(-35, "-", -12)