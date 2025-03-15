### 🔹 Problem 2: Count Vowels in a String

def count_vowels(s: str) -> int:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for char in s.lower() if char in vowels)

# Example usage
print(count_vowels("Apple"))  # Output: 2