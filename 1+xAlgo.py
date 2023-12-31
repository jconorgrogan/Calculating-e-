from decimal import Decimal, getcontext
import time

def calculate_expression(num_zeros, precision):
    """
    Calculate the expression (1+x)^(1/x) with high precision.

    :param num_zeros: The number of zeros in x (x = 0.00...01).
    :param precision: The number of decimal places for the output.
    :return: The calculated value as a string.
    """
    getcontext().prec = precision + num_zeros
    x = Decimal('0.' + '0' * (num_zeros - 1) + '1')
    result = (Decimal(1) + x) ** (Decimal(1) / x)
    return str(result)

def compare_with_e(result, e):
    """
    Compare the calculated result with the value of e and find the first differing digit.

    :param result: The calculated result as a string.
    :param e: The value of e as a string.
    :return: The position of the first differing digit.
    """
    for i in range(min(len(result), len(e))):
        if result[i] != e[i]:
            return i
    return -1

# Define input values
num_zeros_input = 4000
precision_value = 4000

# Calculate e
e = str(Decimal(1).exp())

# Measure execution time
start_time = time.time()
result_limit = calculate_expression(num_zeros_input, precision_value)
execution_time_limit = time.time() - start_time

# Find the first differing digit
first_differing_digit_limit = compare_with_e(result_limit, e)

print("Limit Method Result:", result_limit)
print("Execution Time:", execution_time_limit)
print("First Differing Digit Position:", first_differing_digit_limit)
