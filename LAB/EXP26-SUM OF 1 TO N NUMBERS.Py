# Sum of 1 to N Using Recursion

def sum_n(n):
    if n == 1:          # Base case
        return 1
    else:               # Recursive case
        return n + sum_n(n - 1)

# Input
n = int(input("Enter the value of N: "))

# Function call
result = sum_n(n)

# Output
print("Sum of first", n, "natural numbers is:", result)
