R1 = 15  # Example input that is out of range

try:
    if isinstance(R1, int) and 0 <= R1 <= 12:
        x2 = RangedInt(R1, 12)
        print(f"RangedInt created successfully: {x2.value}")
    else:
        raise ValueError(f"The value {R1} is either not an integer or out of the allowed range 0-12.")
except ValueError as e:
    print(f"Caught an exception: {e}")
