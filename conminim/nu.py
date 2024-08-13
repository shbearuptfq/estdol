def product_of_digits(number):
    product = 1
    for digit in str(number):
        product *= int(digit)
    return product

input_number = 1234  # Example input number
result = product_of_digits(input_number)

print(f"The product of the digits in {input_number} is {result}")
