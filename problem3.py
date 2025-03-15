
### 🔹 Problem 3: Sum of Digits

def sum_of_digits(n: int) -> int:
    return sum(int(digit) for digit in str(n))

# Example usage
print(sum_of_digits(1234))  # Output: 10