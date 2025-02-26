def is_pythagorean_triplet(a, b, c):
    # Sort the numbers to ensure a and b are the legs and c is the hypotenuse
    a, b, c = sorted([a, b, c])
    
    # Check if the numbers satisfy the Pythagorean theorem
    return a**2 + b**2 == c**2

# Example usage:
a = 3
b = 4
c = 5
print(is_pythagorean_triplet(a, b, c))  # Output: True