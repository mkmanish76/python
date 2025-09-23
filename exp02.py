# WAP to find the square root of a no. by newtons method.
def newton_sqrt(number, tolerance=1e-10, max_iterations=1000):
    if number < 0:
        raise ValueError("Cannot compute square root of negative number.")
     # Initial guess (half of number or 1 for small numbers)
    guess = number / 2 if number > 1 else 1.0
    for _ in range(max_iterations):
        new_guess = 0.5 * (guess + number / guess)  # Newton's iteration
        if abs(new_guess - guess) < tolerance:
            return new_guess
        guess = new_guess
    return guess
# Example usage
num = float(input("Enter a number: "))
result = newton_sqrt(num)
print(f"Square root of {num} ≈ {result}")
