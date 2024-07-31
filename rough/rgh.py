def check_digits(number):
    # Ensure number is positive
    number = abs(number)
    
    # Get the ones digit
    ones = number % 10
    
    # Get the tens digit
    tens = (number // 10) % 10
    
    # Get the hundreds digit
    hundreds = (number // 100) % 10
    
    # Get the thousands digit
    thousands = (number // 1000) % 10
    
    return ones, tens, hundreds, thousands

# Example usage
number = 1234
ones, tens, hundreds, thousands = check_digits(number)
print(f"Number: {number}")
print(f"Ones: {ones}")
print(f"Tens: {tens}")
print(f"Hundreds: {hundreds}")
print(f"Thousands: {thousands}")

print(8//0)